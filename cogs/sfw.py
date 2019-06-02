import re
import random
import discord
from datetime import datetime
from discord.ext import commands
from tokenfile import Vars
from sql import sql_modes

vegas_bot_tag = Vars.vegas_bot_tag
torp_tag = Vars.torp_tag


class SfwCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # rape command clone
    async def touch(self, ctx, *args):
        if not args:  # checks if arguments are passed or tuple is empty
            await ctx.send('Who you gonna touch dumbass')
        else:
            # tag self
            if args[0] == ctx.author.mention or args[0] == 'myself':
                await ctx.send(f'{ctx.author.mention} touched themselves reaaaaaal good.')
            # tag vegas bot
            elif args[0] == vegas_bot_tag:
                if ctx.author.mention == torp_tag:  # torp tag
                    await ctx.send('mmm yes daddy')
                else:  # non-torp tags
                    await ctx.send('Only Torp can touch the Vegas Bot.')
            else:
                msg = f'{ctx.author.mention} touched '
                msg += ' '.join(args)
                await ctx.send(msg)

    @commands.command()  # rape command clone
    async def succ(self, ctx, *args):
        if not args:  # checks if arguments are passed or tuple is empty
            await ctx.send('Who you gonna succ dumbass')
        else:
            # tag self
            if args[0] == ctx.author.mention or args[0] == 'myself':
                await ctx.send(f'{ctx.author.mention} got their own succ')
            # tag vegas bot
            elif args[0] == vegas_bot_tag:
                await ctx.send('The Vegas Bot gave you the succ.')
            else:
                msg = f'{ctx.author.mention} gave '
                msg += ' '.join(args)
                msg += ' dat good succ'
                await ctx.send(msg)

    @commands.command()  # bitchslaps the tagged user or whatever gets typed
    async def bitchslap(self, ctx, *args):
        if not args:  # checks if arguments are passed or tuple is empty
            await ctx.send('Who you gonna bitchslap dumbass')
        else:
            possible_outcomes = [
                'bitchslapped',
                'slapped the fuck out of'
            ]
            # tag self
            if args[0] == ctx.author.mention or args[0] == 'myself':
                await ctx.send(f'{ctx.author.mention} bitchslapped themselves')
            # tag vegas bot
            elif args[0] == vegas_bot_tag:
                await ctx.send('You cannot bitchslap the Vegas Bot.')
            else:
                msg = f'{ctx.author.mention} {random.choice(possible_outcomes)} '
                msg += ' '.join(args)
                await ctx.send(msg)

    @commands.command()  # challenge the tagged user
    async def challenge(self, ctx, tag: discord.Member):
        torp_user = ctx.guild.get_member(torp_tag)
        vegas_bot_user = ctx.guild.get_member(vegas_bot_tag)
        outcome = random.randint(0, 2)
        if tag == vegas_bot_user:  # Vegas Bot never loses
            await ctx.send('You always lose against Vegas Bot.')
        else:
            if tag == ctx.author:  # user tags themselves
                await ctx.send('You lost against... yourself?')
            else:
                if torp_user.mentioned_in(ctx.message):  # I win if I get challenged
                    outcome = 0
                if torp_user == ctx.author:  # I win if I challenge
                    outcome = 1
                if outcome == 0:  # tagged user wins
                    await ctx.send(f'{tag.display_name} won!')
                    await ctx.send(f'{ctx.author.display_name} lost!')
                elif outcome == 1:  # author wins
                    await ctx.send(f'{ctx.author.display_name} won!')
                    await ctx.send(f'{tag.display_name} lost!')
                else:  # both lose
                    await ctx.send(f'Both {ctx.author.mention} and {tag.display_name} lost!')

    @commands.command()  # WIP
    async def enable(self, ctx, user: discord.Member):
        await ctx.send(f'Congrats {user.display_name}, you\'re not disabled anymore!')

    @commands.command()  # WIP
    async def disable(self, ctx, user: discord.Member):
        await ctx.send(f'I\'m sorry {user.display_name}, but you\'re now disabled.')

    @commands.command()  # checks mode of server where command was called
    async def check_nsfw(self, ctx):
        mode = sql_modes.check_mode(sv=ctx.guild.id)[0][0]   # returns list of tuples, use double index to get actual values
        if mode == 'nsfw':
            await ctx.send('I can be very naughty :))')
        else:
            await ctx.send('I\'m innocent, I swear')

    @commands.command()  # banan
    async def banana(self, ctx):
        await ctx.send(':banana: <:medaddy:564806501215240192>')

    @commands.command()  # fuck off meme
    async def fuckoff(self, ctx):
        await ctx.send('https://imgur.com/a/RMXA4xP')

    @commands.command()  # professional have standards meme
    async def pro(self, ctx):
        await ctx.send('https://imgur.com/a/TE06C5s')

    @commands.command()  # reeeeeeee
    async def reee(self, ctx):
        await ctx.send('https://imgur.com/a/0QeJEHa')

    @commands.command()  # sends you're welcome gif
    async def yw(self, ctx):
        await ctx.send('https://tenor.com/view/youre-welcome-maui-moana-gif-8323041')

    @commands.Cog.listener()  # listener, checks every message
    async def on_message(self, ctx):
        x = random.choice(range(0, 69))
        if x >= 60 and not ctx.author.bot:
            await dadjoke(ctx)
        await name_mention(ctx)


async def dadjoke(ctx):
    words = re.search(r'\b(i\'?m|i\sam)\s+(.*)', ctx.content, re.IGNORECASE)
    if words is not None:
        words = words.group(2)
        await ctx.channel.send(f'Hi {words}, I\'m dad!')


async def name_mention(ctx):
    s = re.search(r'(\w*rp)|(tr\w*p)', ctx.content, re.IGNORECASE)
    if s is not None and ctx.author.id is not torp_tag:
        message = f'Server: {ctx.guild} | Channel: {ctx.channel}\n{ctx.author}: {ctx.content}'
        print(f'\'{s.group(0)}\'')
        print(message)
        print(f'{datetime.now().time()}\n\n')


def setup(bot):
    bot.add_cog(SfwCog(bot))
