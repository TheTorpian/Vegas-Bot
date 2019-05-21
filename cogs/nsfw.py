import random
from discord.ext import commands
from sql import sql_modes
from tokenfile import Vars

vegas_bot_tag = Vars.vegas_bot_tag


class NsfwCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # rapes the tagged user or whatever gets typed
    async def rape(self, ctx, *args):
        mode = sql_modes.check_mode(sv=ctx.guild.id)[0][0]   # returns list of tuples, use double index to get actual values
        if mode == 'sfw':
            await ctx.send('You\'re not supposed to use this command.')
        else:
            if not args:  # checks if arguments are passed or tuple is empty
                await ctx.send('Who you gonna rape dumbass')
            else:
                possible_responses = [
                    ' raped ',
                    ' went to town with ',
                    ' creepy uncle\'d ',
                    ' priested ',
                    ' step dadded '
                ]
                # self rape
                if args[0] == ctx.author.mention or args[0] == 'myself':
                    await ctx.send('ya nasty')
                # Vegas Bot rape
                elif args[0] == vegas_bot_tag:
                    await ctx.send('You can\'t rape the Vegas Bot.')
                # all other rapes
                else:
                    msg = ctx.author.mention + random.choice(possible_responses)
                    msg += ' '.join(args)
                    await ctx.send(msg)

    @commands.command()  # rape command clone
    async def molest(self, ctx, *args):
        mode = sql_modes.check_mode(sv=ctx.guild.id)[0][0]   # returns list of tuples, use double index to get actual values
        if mode == 'sfw':
            await ctx.send('You\'re not supposed to use this command.')
        else:
            if not args:
                await ctx.send('Who you gonna molest dumbass')
            else:
                # tag self
                if args[0] == ctx.author.mention or args[0] == 'myself':
                    await ctx.send(f'{ctx.author.mention} tried to molest themselves.')
                # tag vegas bot
                elif args[0] == vegas_bot_tag:
                    await ctx.send('You cannot molest the Vegas Bot.')
                else:
                    msg = f'{ctx.author.mention} molested '
                    msg += ' '.join(args)
                    await ctx.send(msg)

    @commands.command()  # rape command clone
    async def fill(self, ctx, *args):
        mode = sql_modes.check_mode(sv=ctx.guild.id)[0][0]   # returns list of tuples, use double index to get actual values
        if mode == 'sfw':
            await ctx.send('You\'re not supposed to use this command.')
        else:
            if not args:  # checks if arguments are passed or tuple is empty
                await ctx.send('Who you gonna fill dumbass')
            else:
                # tag self
                if args[0] == ctx.author.mention or args[0] == 'myself':
                    await ctx.send(f'{ctx.author.mention} filled... themselves up?')
                # tag vegas bot
                elif args[0] == vegas_bot_tag:
                    await ctx.send('You cannot fill the Vegas Bot.')
                else:
                    msg = f'{ctx.author.mention} filled '
                    msg += ' '.join(args)
                    msg += ' all the way up ;))'
                    await ctx.send(msg)

    # @commands.command()  # rape for 2 tags
    # async def gangrape(self, ctx, *args):
    #     mode = sql_modes.check_mode(sv=ctx.guild.id)[0][0]   # returns dict of tuples, use double index to get actual values
    #     if mode == 'sfw':
    #         await ctx.send("You're not supposed to use this command.")
    #     else:
    #         if not args or len(args) < 2:  # checks if arguments are passed or tuple is empty
    #             await ctx.send('Who you gonna gangrape dumbass')
    #         else:
    #             possible_responses = [
    #                 ' raped ',
    #                 ' touched ',
    #                 ' molested ',
    #                 ' went to town with ',
    #                 " creepy uncle'd ",
    #                 ' filled the holes of ',
    #                 ' priested ',
    #                 ' step dadded '
    #             ]
    #             msg = ctx.author.mention + random.choice(possible_responses) + args[0]
    #             for arg in args[1:]:
    #                 if arg == ' ':  # removes blank spaces
    #                     break
    #                 else:
    #                     msg += f' and {arg}'
    #             await ctx.send(msg)


def setup(bot):
    bot.add_cog(NsfwCog(bot))
