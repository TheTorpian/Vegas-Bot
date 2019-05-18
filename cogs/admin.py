from discord.ext import commands
from discord.ext.commands import has_permissions
from sql import sql_modes
from tokenfile import Vars

torp_tag = Vars.torp_tag  # big torpo's discord tag


class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # changes nsfw on or off
    @has_permissions(administrator=True)
    async def nsfw(self, ctx, arg):
        if arg == 'on':
            sql_modes.change_mode(sv=ctx.guild.id, md='nsfw')
            await ctx.send('Gettin\' extra naughty now :))')
        elif arg == 'off':
            await ctx.send('Don\'t tell mommy')
            sql_modes.change_mode(sv=ctx.guild.id, md='sfw')
        else:
            await ctx.send("Invalid argument")

    @commands.command()  # checks mode of server where command was called
    async def check_nsfw(self, ctx):
        mode = sql_modes.check_mode(sv=ctx.guild.id)[0][0]   # returns dict of tuples, use double index to get actual values
        if mode == 'nsfw':
            await ctx.send('I can be very naughty :))')
        else:
            await ctx.send('I\'m innocent, I swear')

    @commands.command()  # manually adds server where command was called
    async def add_server_db(self, ctx):
        if ctx.author.mention == torp_tag:
            sql_modes.new_server(sv=ctx.guild.id, md='sfw')
            print(f'Added \'{ctx.guild.id}\' to db\n\n')
        else:
            await ctx.send('You do not have permission to use this command.')

    @commands.command()  # changes prefix for server where it was called
    @has_permissions(administrator=True)
    async def change_prefix(self, ctx, prefix):
        sql_modes.change_prefix(sv=ctx.guild.id, pf=prefix)
        await ctx.send(f'Prefix changed to \'{prefix}\'')

    ### error handlers ###

    @change_prefix.error
    async def change_prefix_handler(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have permission to use this command.')

    @nsfw.error
    async def nsfw_handler(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have permission to use this command.')


def setup(bot):
    bot.add_cog(AdminCog(bot))
