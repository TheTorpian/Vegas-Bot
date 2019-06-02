from discord.ext import commands
from discord.ext.commands import has_permissions
from sql import sql_modes


class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # changes nsfw on or off
    @has_permissions(administrator=True)
    async def nsfw(self, ctx, arg):
        mode = sql_modes.check_mode(sv=ctx.guild.id)[0][0]  # returns list of tuples, use double index to get actual values
        if arg == 'on':
            if mode == 'nsfw':
                await ctx.send('Nsfw is already on')
            else:
                sql_modes.change_mode(sv=ctx.guild.id, md='nsfw')
                await ctx.send('Gettin\' extra naughty now :))')
        elif arg == 'off':
            if mode == 'sfw':
                await ctx.send('Nsfw is already off')
            else:
                sql_modes.change_mode(sv=ctx.guild.id, md='sfw')
                await ctx.send('Don\'t tell mommy')
        else:
            await ctx.send("Invalid argument")

    @commands.command()  # changes prefix for server where it was called
    @has_permissions(administrator=True)
    async def change_prefix(self, ctx, prefix):
        sql_modes.change_prefix(sv=ctx.guild.id, pf=prefix)
        await ctx.send(f'Prefix changed to \'{prefix}\'')


def setup(bot):
    bot.add_cog(AdminCog(bot))
