import re
import random
import requests
import discord
from datetime import datetime
from discord.ext import commands
from tokenfile import Vars
# from sql import sql_modes

vegas_bot_tag = Vars.vegas_bot_tag
torp_tag = Vars.torp_tag
apikey = Vars.apikey
f_dict = Vars.f_dict


class SfwCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # rape command clone
    async def touch(self, ctx, tag: discord.Member):
        torp_user = ctx.guild.get_member(torp_tag)
        vegas_bot_user = ctx.guild.get_member(vegas_bot_tag)
        if not tag:  # checks for tag
            await ctx.send('Who you gonna touch dumbass')
        else:
            # tag self
            if tag == ctx.author:
                await ctx.send(f'{ctx.author.display_name} touched themselves reaaaaaal good.')
            # tag is Vegas Bot
            elif tag == vegas_bot_user:
                if ctx.author == torp_user:  # torp tag
                    await ctx.send('mmm yes daddy')
                else:  # non-torp tags
                    await ctx.send('Only Torp can touch the Vegas Bot.')
            else:
                msg = f'{ctx.author.display_name} touched {tag.display_name}'
                await ctx.send(msg)

    @commands.command()  # bitchslaps the tagged user
    async def bitchslap(self, ctx, tag: discord.Member):
        vegas_bot_user = ctx.guild.get_member(vegas_bot_tag)
        # if not tag.mentioned_in(ctx.content):  # checks for tag
        #     await ctx.send('Who you gonna bitchslap dumbass')
        # else:
        possible_outcomes = [
            'bitchslapped',
            'slapped the fuck out of'
        ]
        # tag self
        if tag == ctx.author:
            await ctx.send(f'{ctx.author.display_name} bitchslapped themselves')
        # tag is Vegas Bot
        elif tag == vegas_bot_user:
            await ctx.send('You cannot bitchslap the Vegas Bot.')
        else:
            msg = f'{ctx.author.display_name} {random.choice(possible_outcomes)} {tag.display_name}'
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
                    await ctx.send('dude it\'s rigged lmao')
                else:
                    if outcome == 0:  # tagged user wins
                        await ctx.send(f'{tag.display_name} won!')
                        await ctx.send(f'{ctx.author.display_name} lost!')
                    elif outcome == 1:  # author wins
                        await ctx.send(f'{ctx.author.display_name} won!')
                        await ctx.send(f'{tag.display_name} lost!')
                    else:  # both lose
                        await ctx.send(f'Both {ctx.author.display_name} and {tag.display_name} lost!')

    # @commands.command()  # checks mode of server where command was called
    # async def check_nsfw(self, ctx):
    #     mode = sql_modes.check_mode(sv=ctx.guild.id)[0][0]   # returns list of tuples, use double index to get actual values
    #     if mode == 'nsfw':
    #         await ctx.send('I can be very naughty :))')
    #     else:
    #         await ctx.send('I\'m innocent, I swear')

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

    @commands.command()  # sends a random f ascii art
    async def f(self, ctx):
        f = random.choice(list(f_dict))
        await ctx.send(f_dict[f])

    @commands.command()
    async def lee_banned(self, ctx):
        await ctx.send('https://giphy.com/gifs/S451Y846IMnWwKDKug')

    @commands.command()  # random banned gif
    async def banned(self, ctx):
        search = f'https://api.tenor.com/v1/search?q=banned&key={apikey}'  # searches tenor for banned gifs with my apikey
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

    @commands.Cog.listener()  # listener, checks every message
    async def on_message(self, ctx):
        x = random.choice(range(0, 69))
        if x >= 60 and not ctx.author.bot:
            await dadjoke(ctx)
        await name_mention(ctx)


async def dadjoke(ctx):  # it's a fuckin dad joke
    words = re.search(r'\b(i\'?m|i\sam)\s+(.*)', ctx.content, re.IGNORECASE)
    if words is not None:
        words = words.group(2)
        await ctx.channel.send(f'Hi {words}, I\'m dad!')


async def name_mention(ctx):  # prints to console when my name is said
    s = re.search(r'(t\w*rp)|(tr\w*p)', ctx.content, re.IGNORECASE)
    torp_user = ctx.guild.get_member(torp_tag)
    if s is not None and ctx.author is not torp_user:
        message = f'Server: {ctx.guild} | Channel: {ctx.channel}\n{ctx.author}: {ctx.content}'
        print(f'\'{s.group(0)}\'')
        print(message)
        print(f'{datetime.now()}\n\n')


def setup(bot):
    bot.add_cog(SfwCog(bot))
