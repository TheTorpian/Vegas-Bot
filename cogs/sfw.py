import random
from discord.ext import commands
from tokenfile import Vars

vegas_bot_tag = Vars.vegas_bot_tag  # vegas bot's discord tag
torp_tag = Vars.torp_tag  # big torpo's discord tag


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
                'slapped the bitch out of'
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
    async def challenge(self, ctx, tag):
        if not tag:  # checks if arguments are passed or tuple is empty
            await ctx.send('Who you gonna challenge dumbass')
        else:
            outcome = random.randint(0, 2)

            if tag == vegas_bot_tag:
                await ctx.send("You always lose against Vegas Bot.")
            else:
                if outcome == 0:
                    if tag == ctx.author.mention:
                        await ctx.send('You lost against... yourself?')
                    else:
                        await ctx.send(f'{tag} won!')
                        await ctx.send(f'{ctx.author.mention} lost!')
                if outcome == 1:
                    if tag == ctx.author.mention:
                        await ctx.send('You won! But also lost...?')
                    else:
                        await ctx.send(f'{ctx.author.mention} won!')
                        await ctx.send(f'{tag} lost!')
                if outcome == 2:
                    if tag == ctx.author.mention:
                        await ctx.send(f'Both {ctx.author.mention} and {tag} lost!')

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


def setup(bot):
    bot.add_cog(SfwCog(bot))
