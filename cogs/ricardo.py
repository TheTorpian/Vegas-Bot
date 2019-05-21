import random
from discord.ext import commands
from tokenfile import Vars

bigric = Vars.bigric


class RicardoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # random ricardo gif or meme
    async def ricardo(self, ctx):
        possible_ricardos = [
            'https://tenor.com/2Aql.gif',
            'https://tenor.com/4f6F.gif',
            'https://tenor.com/3KGw.gif',
            'https://tenor.com/3WCg.gif',
            'https://tenor.com/3oVt.gif',
            'https://imgur.com/a/pM5R4UM',
            'https://imgur.com/a/3qtdO1e',
            '<a:ricardoBear:564806311791820810>',
            bigric
        ]
        await ctx.send(random.choice(possible_ricardos))

    @commands.command()  # ricardo bear
    async def ricardobear(self, ctx):
        await ctx.send('<a:ricardoBear:564806311791820810>')

    @commands.command()  # big ricardo
    async def bigricardo(self, ctx):
        await ctx.send(bigric)


def setup(bot):
    bot.add_cog(RicardoCog(bot))
