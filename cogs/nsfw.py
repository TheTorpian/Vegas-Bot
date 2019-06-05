import random
import discord
from discord.ext import commands
from sql import sql_modes
from tokenfile import Vars

vegas_bot_tag = Vars.vegas_bot_tag


class NsfwCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['molest'])  # rapes the tagged user
    async def rape(self, ctx, tag: discord.Member):
        mode = sql_modes.check_mode(sv=ctx.guild.id)[0][0]   # returns list of tuples, use double index to get actual values
        vegas_bot_user = ctx.guild.get_member(vegas_bot_tag)
        if mode == 'sfw':
            await ctx.send('You\'re not supposed to use this command.')
        else:
            if not tag:  # checks for tag
                await ctx.send('Who you gonna rape dumbass')
            else:
                possible_responses = [
                    f'raped {tag.display_name}',
                    f'molested {tag.display_name}',
                    f'went to town with {tag.display_name}',
                    f'creepy uncle\'d {tag.display_name}',
                    f'priested {tag.display_name}',
                    f'step dadded {tag.display_name}',
                    f'tore {tag.display_name} a new one',
                    f'went into {tag.display_name}\'s every hole'
                ]
                # self rape
                if tag == ctx.author:
                    await ctx.send('ya nasty')
                # tag is Vegas Bot
                elif tag == vegas_bot_user:
                    await ctx.send('You can\'t rape the Vegas Bot.')
                # all other rapes
                else:
                    msg = f'{ctx.author.display_name} {random.choice(possible_responses)}'
                    await ctx.send(msg)

    @commands.command()  # rape command clone
    async def fill(self, ctx, tag: discord.Member):
        mode = sql_modes.check_mode(sv=ctx.guild.id)[0][0]   # returns list of tuples, use double index to get actual values
        vegas_bot_user = ctx.guild.get_member(vegas_bot_tag)
        if mode == 'sfw':
            await ctx.send('You\'re not supposed to use this command.')
        else:
            if not tag:  # checks for tag
                await ctx.send('Who you gonna fill dumbass')
            else:
                # tag self
                if tag == ctx.author:
                    await ctx.send(f'{ctx.author.display_name} filled... themselves up?')
                # tag is Vegas Bot
                elif tag == vegas_bot_user:
                    await ctx.send('You cannot fill the Vegas Bot.')
                else:
                    msg = f'{ctx.author.display_name} filled {tag.display_name} all the way up ;))'
                    await ctx.send(msg)


def setup(bot):
    bot.add_cog(NsfwCog(bot))
