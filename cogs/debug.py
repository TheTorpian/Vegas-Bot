import re
from discord.ext import commands
from tokenfile import Vars
from sql import sql_modes

torp_tag = Vars.torp_tag


class DebugCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # ping command
    async def ping(self, ctx):
        await ctx.send('pong')

    @commands.command()  # say args
    async def say(self, ctx, *args):
        if ctx.author.mention == torp_tag:
            await ctx.send(' '.join(args))

    @commands.command()  # sends first word from message
    async def getargs(self, ctx, *args):
        if ctx.author.mention == torp_tag:
            tag = ' '.join(args)
            await ctx.send(f'`{tag}`')

    @commands.command()  # get current server id
    async def getguild(self, ctx):
        if ctx.author.mention == torp_tag:
            await ctx.send(ctx.guild.id)

    @commands.command()  # emote testing
    async def testemote(self, ctx, tag):
        if ctx.author.mention == torp_tag:
            await ctx.send('<a:Nig:557976066828926986>')

    @commands.command()  # testing for regex functions
    async def test_regex(self, ctx):
        if ctx.author.mention == torp_tag:
            msg = ctx.message.content
            author = re.findall(r'(\s[^-"]*$)', msg)
            quote = re.findall(r'"[^"]*"', msg)
            if len(author) == 1 and len(quote) == 1:
                await ctx.send(ctx.message.content)
                await ctx.send(quote[0])
                await ctx.send(author[0][1:])
            else:
                await ctx.send('Wrong format')

    @commands.command()  # sends query
    async def query(self, ctx, *args):
        if ctx.author.id == torp_tag:
            query = ' '.join(args)
            sql_modes.send_query(query)

    @commands.command()  # leaves guild specified and prints in console
    async def leave(self, ctx, arg):
        if ctx.author.mention == torp_tag:
            for server in self.bot.guilds:
                if str(server.id) == str(arg):
                    await server.leave()
                    print(f'Left \'{server.name}\': {server.id}')
        else:
            await ctx.send('You do not have permission to use this command.')


def setup(bot):
    bot.add_cog(DebugCog(bot))
