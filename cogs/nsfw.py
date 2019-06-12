import random
import discord
from discord.ext import commands
import mysql.connector as mysql
from sql import sql_modes, sql_handicap
from tokenfile import Vars

vegas_bot_tag = Vars.vegas_bot_tag


class NsfwCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['molest'])  # rapes the tagged user
    async def rape(self, ctx, tag: discord.Member):
        mode = sql_modes.check_mode(sv=ctx.guild.id)
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
    async def succ(self, ctx, tag: discord.member):
        mode = sql_modes.check_mode(sv=ctx.guild.id)
        vegas_bot_user = ctx.guild.get_member(vegas_bot_tag)
        if mode == 'sfw':
            await ctx.send('You\'re not supposed to use this command.')
        else:
            if not tag:  # checks for tag
                await ctx.send('Who you gonna succ dumbass')
            else:
                # tag self
                if tag == ctx.author:
                    await ctx.send(f'{ctx.author.display_name} got their own succ')
                # tag is Vegas Bot
                elif tag == vegas_bot_user:
                    await ctx.send('The Vegas Bot gave you the succ.')
                else:
                    msg = f'{ctx.author.display_name} gave {tag.display_name} dat good succ'
                    await ctx.send(msg)

    @commands.command()  # rape command clone
    async def fill(self, ctx, tag: discord.Member):
        mode = sql_modes.check_mode(sv=ctx.guild.id)
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

    @commands.command()  # removes any disability of the tagged user
    async def enable(self, ctx, tag: discord.Member):
        mode = sql_modes.check_mode(sv=ctx.guild.id)
        if mode == 'sfw':
            await ctx.send('You\'re not supposed to use this command.')
        else:
            if tag == ctx.author:  # checks for self tag
                await ctx.send('You can\'t enable yourself')
            else:
                hcap = sql_handicap.select_handicap(user=tag.id)
                try:
                    sql_handicap.insert_handicap(user=tag.id, handicap='disabled')
                    await ctx.send('They haven\'t been disabled yet, so I just went ahead and did it for you.')
                except mysql.errors.IntegrityError:
                    if hcap == 'enabled':
                        await ctx.send('User isn\'t disabled yet.')
                    elif hcap == 'disabled':
                        sql_handicap.change_handicap(user=tag.id, handicap='enabled')
                        responses = [
                            f'Congrats {tag.display_name}, you\'re not disabled!'
                        ]
                        await ctx.send(random.choice(responses))

    @commands.command()  # disables the tagged user
    async def disable(self, ctx, tag: discord.Member):
        mode = sql_modes.check_mode(sv=ctx.guild.id)
        if mode == 'sfw':
            await ctx.send('You\'re not supposed to use this command.')
        else:
            if tag == ctx.author:  # checks for self tag
                await ctx.send('You can\'t disable yourself.')
            else:
                hcap = sql_handicap.select_handicap(user=tag.id)
                try:
                    sql_handicap.insert_handicap(user=tag.id, handicap='disabled')
                    await ctx.send(f'{tag.display_name}, you just got disabled!')
                except mysql.errors.IntegrityError:
                    if hcap == 'disabled':
                        await ctx.send('Can\'t get more disabled than they already are.')
                    elif hcap == 'enabled':
                        sql_handicap.change_handicap(user=tag.id, handicap='disabled')
                        responses = [
                            f'Enjoy your free parking spot, {tag.display_name}.',
                            f'Enjoy your disability checks, {tag.display_name}.'
                        ]
                        await ctx.send(random.choice(responses))


def setup(bot):
    bot.add_cog(NsfwCog(bot))
