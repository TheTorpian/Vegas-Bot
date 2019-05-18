from discord.ext import commands
from tokenfile import Vars

torp_tag = Vars.torp_tag  # big torpo's discord tag


class DebugCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # ping command
    async def ping(self, ctx):
        await ctx.send("pong")

    @commands.command()  # say args
    async def say(self, ctx, *args):
        if ctx.author.mention == torp_tag:
            await ctx.send(' '.join(args))
        else:
            await ctx.send('You do not have permission to use this command.')

    @commands.command()  # sends first word from message
    async def getargs(self, ctx, tag):
        if ctx.author.mention == torp_tag:
            await ctx.send(f'`{tag}`')
        else:
            await ctx.send('You do not have permission to use this command.')

    @commands.command()  # get current server id
    async def getguild(self, ctx):
        if ctx.author.mention == torp_tag:
            await ctx.send(ctx.guild.id)
        else:
            await ctx.send('You do not have permission to use this command.')

    @commands.command()  # emote testing
    async def testemote(self, ctx, tag):
        if ctx.author.mention == torp_tag:
            await ctx.send('<a:Nig:557976066828926986>')
        else:
            await ctx.send('You do not have permission to use this command.')

    @commands.command()  # leaves guild specified and prints in console
    async def leave(self, ctx, arg):
        if ctx.author.mention == torp_tag:
            for server in self.bot.guilds:
                if str(server.id) == str(arg):
                    await server.leave()
                    print(f'Left "{server.name}": {server.id}')
        else:
            await ctx.send('You do not have permission to use this command.')


def setup(bot):
    bot.add_cog(DebugCog(bot))
