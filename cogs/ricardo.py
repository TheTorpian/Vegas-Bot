import random
import requests
from discord.ext import commands
from tokenfile import Vars

bigric = Vars.bigric
apikey = Vars.apikey


class RicardoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # random ricardo gif or meme
    async def ricardo(self, ctx):
        search = f'https://api.tenor.com/v1/search?q=ricardo&key={apikey}'  # searches tenor for ricardo with my apikey
        get = requests.get(search)
        if get.status_code == 200:  # get successful
            json_search = get.json()
            json_check = json_search['next']  # number of results, is string
            if json_check == '0':
                await ctx.send('No gifs found.')
            else:
                rand_gif = random.randint(1, int(json_check))  # random gif from those found
                json_s = json_search['results']  # get the results
                gif = json_s[rand_gif]  # get the random gif
                gif = gif.get('media')  # go into media, various file types etc
                gif = gif[0]  # has to get the first element
                gif = gif.get('gif')  # get the gif element
                gif = gif.get('url')  # get url of gif
                await ctx.send(gif)
        elif get.status_code == 404:
            await ctx.send('Error 404!')

    @commands.command()  # ricardo bear
    async def ricardobear(self, ctx):
        await ctx.send('<a:ricardoBear:564806311791820810>')

    @commands.command()  # big ricardo
    async def bigricardo(self, ctx):
        await ctx.send(bigric)


def setup(bot):
    bot.add_cog(RicardoCog(bot))
