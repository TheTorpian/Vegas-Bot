import re
import requests
import random
from discord.ext import commands
from tokenfile import Vars
from sql import sql_modes

vegas_bot_tag = Vars.vegas_bot_tag
torp_tag = Vars.torp_tag
apikey = Vars.apikey


class DebugCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)  # ping command
    @commands.check(Vars.user_is_me)
    async def ping(self, ctx):
        await ctx.send('pong')

    @commands.command(pass_context=True)  # say args
    @commands.check(Vars.user_is_me)
    async def say(self, ctx, *args):
        await ctx.send(' '.join(args))

    @commands.command(pass_context=True)  # just like say but in a specified channel
    @commands.check(Vars.user_is_me)
    async def says(self, ctx, ch, *args):
        channel = self.bot.get_channel(int(ch))
        await channel.send(' '.join(args))

    @commands.command(pass_context=True)  # says args in code block
    @commands.check(Vars.user_is_me)
    async def get_args(self, ctx, *args):
        tag = ' '.join(args)
        await ctx.send(f'`{tag}`')

    @commands.command(pass_context=True)  # get ctx.author member object
    @commands.check(Vars.user_is_me)
    async def get_member(self, ctx):
        await ctx.send(ctx.author)

    @commands.command(pass_context=True)  # get current server id
    @commands.check(Vars.user_is_me)
    async def get_guild(self, ctx):
        await ctx.send(ctx.guild.id)

    @commands.command(pass_context=True)  # emote testing
    @commands.check(Vars.user_is_me)
    async def test_emote(self, ctx, tag):
        await ctx.send('<a:Nig:557976066828926986>')

    @commands.command(pass_context=True)  # testing for regex functions
    @commands.check(Vars.user_is_me)
    async def test_regex(self, ctx):
        author = re.search(r'(\s[^-"]*$)', ctx.message.content)
        quote = re.search(r'("[^"]*")', ctx.message.content)
        if author and quote:
            await ctx.send(ctx.message.content)
            await ctx.send(quote.group(0))
            await ctx.send(author.group(0)[1:])
        else:
            await ctx.send('Wrong format')

    @commands.command(pass_context=True)  # tests tenor gif
    @commands.check(Vars.user_is_me)
    async def test_tenor(self, ctx):
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
                gif = json_s[rand_gif].get('media')[0].get('gif').get('url')  # get the actual gif
                await ctx.send(gif)  # finally send the fuckin thing
        elif get.status_code == 404:
            await ctx.send('Error 404!')

    @commands.command(pass_context=True)  # manually adds server where command was called
    @commands.check(Vars.user_is_me)
    async def add_server_db(self, ctx):
        sql_modes.new_server(sv=ctx.guild.id, md='sfw')
        print(f'Added \'{ctx.guild.id}\' to db\n\n')

    @commands.command(pass_context=True)  # sends query
    @commands.check(Vars.user_is_me)
    async def query(self, ctx, *args):
        query = ' '.join(args)
        sql_modes.send_query(query)
        await ctx.send(f'Query `{query}` sent')

    @commands.command(pass_context=True)  # leaves guild specified and prints in console
    @commands.check(Vars.user_is_me)
    async def leave(self, ctx, arg):
        for server in self.bot.guilds:
            if str(server.id) == str(arg):
                await server.leave()
                print(f'Left \'{server.name}\': {server.id}')


def setup(bot):
    bot.add_cog(DebugCog(bot))
