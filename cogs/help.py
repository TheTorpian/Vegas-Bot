from collections import OrderedDict
from discord.ext import commands
from sql import sql_modes
from tokenfile import Vars

INVITE = Vars.INVITE


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *args):
        commands = OrderedDict()
        commands['touch'] = ['Touchy touchy', '[arg]', '']
        commands['succ'] = ['Give someone of your choosing dat good succ', '[arg]', '']
        commands['bitchslap'] = ['Exactly what it sounds like', '', '']
        commands['challenge'] = ['Challenge another user', '[arg]', '']
        commands['banana'] = ['If you really need potassium', '', '']
        commands['fuckoff'] = ['Just fuck off mate', '', '']
        commands['pro'] = ['Professionals have standards', '', '']
        commands['reee'] = ['Autistic screeching of the highest quality', '', '']
        commands['rape'] = ['Non consensual sex with your preferred person/object (nsfw only)', '[arg]', 'nsfw']
        commands['molest'] = ['Same as .rape, but different reply (nsfw only)', '[arg]', 'nsfw']
        commands['fill'] = [';)) (nsfw only)', '[arg]', 'nsfw']
        # commands['gangrape'] = ['When one is not enough (nsfw only)', '[args...]', 'nsfw']
        commands['quote'] = ['Posts a random quote from this server', '', '']
        commands['add_quote'] = ['Adds the specified quote', '"quote" - <user>', '']
        commands['ricardo'] = ['Posts a random ricardo gif', '', '']
        commands['ricardobear'] = ['Posts the mighty ricardo bear', '', '']
        commands['bigricardo'] = ['Summons big ricardo', '', '']
        commands['check_nsfw'] = ['Checks if nsfw is enabled on this server or not', '', '']
        commands['nsfw'] = ['Turns nsfw mode on or off (admin only)', '<on>/<off>', '']
        commands['change_prefix'] = ['Changes the command prefix on this server (admin only)', '', '']
        commands['help'] = ['It\'s this command', '', '']
        commands['invite'] = ['Get the invite link', '', '']

        mode = sql_modes.check_mode(sv=ctx.guild.id)[0][0]   # returns list of tuples, use double index to get actual values
        prefix = sql_modes.get_prefix(ctx.guild.id)

        if not args:  # get longest command name, to have evenly spaced help message
            max_len = 0
            for cmd in commands:
                if len(cmd) > max_len:
                    max_len = len(cmd)

            msg = '```'
            for command, desc in commands.items():  # for every command in the commands dict
                if mode != 'nsfw' and desc[2] == 'nsfw':
                    continue
                msg += f'{command} '  # command name
                for _ in range(len(command), max_len):  # extra spaces
                    msg += ' '
                msg += f'{desc[0]}\n'  # add the description
            msg += f'\n\nThis server\'s prefix is {prefix}\nType {prefix}help [command] for more info on a command.```'

        elif args[0] in commands:
            msg = f'```Use: {prefix}{args[0]} {commands[args[0]][1]}\n\n{commands[args[0]][0]}```'  # command name and arguments (if needed)

        else:
            msg = 'No command called "'
            msg += ' '.join(args)
            msg += '" found.'
        await ctx.send(msg)

    @commands.command()  # invite link
    async def invite(self, ctx):
        await ctx.send(INVITE)


def setup(bot):
    bot.add_cog(HelpCog(bot))
