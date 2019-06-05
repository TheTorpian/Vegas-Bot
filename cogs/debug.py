import re
from discord.ext import commands
from tokenfile import Vars
from sql import sql_modes

vegas_bot_tag = Vars.vegas_bot_tag
torp_tag = Vars.torp_tag


class DebugCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # ping command
    async def ping(self, ctx):
        if ctx.author == ctx.guild.get_member(torp_tag):
            await ctx.send('pong')

    @commands.command()  # say args
    async def say(self, ctx, *args):
        if ctx.author == ctx.guild.get_member(torp_tag):
            await ctx.send(' '.join(args))

    @commands.command()  # just like say but in a specified channel
    async def says(self, ctx, ch, *args):
        if ctx.author == ctx.guild.get_member(torp_tag):
            channel = self.bot.get_channel(int(ch))
            await channel.send(' '.join(args))

    @commands.command()  # says args in code block
    async def get_args(self, ctx, *args):
        if ctx.author == ctx.guild.get_member(torp_tag):
            tag = ' '.join(args)
            await ctx.send(f'`{tag}`')

    @commands.command()  # get ctx.author member object
    async def get_member(self, ctx):
        if ctx.author == ctx.guild.get_member(torp_tag):
            await ctx.send(ctx.author)

    @commands.command()  # get current server id
    async def get_guild(self, ctx):
        if ctx.author == ctx.guild.get_member(torp_tag):
            await ctx.send(ctx.guild.id)

    @commands.command()  # emote testing
    async def test_emote(self, ctx, tag):
        if ctx.author == ctx.guild.get_member(torp_tag):
            await ctx.send('<a:Nig:557976066828926986>')

    @commands.command()  # testing for regex functions
    async def test_regex(self, ctx):
        if ctx.author == ctx.guild.get_member(torp_tag):
            author = re.search(r'(\s[^-"]*$)', ctx.message.content)
            quote = re.search(r'("[^"]*")', ctx.message.content)
            if author and quote:
                await ctx.send(ctx.message.content)
                await ctx.send(quote.group(0))
                await ctx.send(author.group(0)[1:])
            else:
                await ctx.send('Wrong format')

    @commands.command()  # manually adds server where command was called
    async def add_server_db(self, ctx):
        if ctx.author == ctx.guild.get_member(torp_tag):
            sql_modes.new_server(sv=ctx.guild.id, md='sfw')
            print(f'Added \'{ctx.guild.id}\' to db\n\n')
        else:
            await ctx.send('You do not have permission to use this command.')

    @commands.command()  # sends query
    async def query(self, ctx, *args):
        if ctx.author == ctx.guild.get_member(torp_tag):
            query = ' '.join(args)
            sql_modes.send_query(query)

    @commands.command()  # leaves guild specified and prints in console
    async def leave(self, ctx, arg):
        if ctx.author == ctx.guild.get_member(torp_tag):
            for server in self.bot.guilds:
                if str(server.id) == str(arg):
                    await server.leave()
                    print(f'Left \'{server.name}\': {server.id}')
        else:
            await ctx.send('You do not have permission to use this command.')


def setup(bot):
    bot.add_cog(DebugCog(bot))
