from collections import OrderedDict
from discord.ext import commands
from sql import sql_modes
from tokenfile import Vars

INVITE = Vars.INVITE


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(when_mentioned=True, aliases=['commands'])
    async def help(self, ctx, *args):
        commands = OrderedDict()
        commands['touch'] = ['Touchy touchy', '<mention>', '']
        commands['bitchslap'] = ['Exactly what it sounds like', '<mention>', '']
        commands['challenge'] = ['Challenge another user', '<mention>', '']
        commands['banana'] = ['If you really need potassium', '', '']
        commands['fuckoff'] = ['Just fuck off mate', '', '']
        commands['pro'] = ['Professionals have standards', '', '']
        commands['reee'] = ['Autistic screeching of the highest quality', '', '']
        commands['yw'] = ['What can I say except you\'re welcome!', '', '']
        commands['f'] = ['Press F to pay respects', '', '']
        commands['banned'] = ['Doesn\'t actually ban but you get a cool gif', '', '']
        commands['rape, molest'] = ['Non consensual sex with your preferred person/object (nsfw only)', '<mention>', 'nsfw']
        commands['succ'] = ['Give someone of your choosing dat good succ (nsfw only)', '<mention>', 'nsfw']
        commands['fill'] = [';)) (nsfw only)', '<mention>', 'nsfw']
        commands['disable'] = ['Disables the tagged user (nsfw only)', '<mention>', 'nsfw']
        commands['enable'] = ['Enables the tagged user (nsfw only)', '<mention>', 'nsfw']
        commands['quote'] = ['Posts a random or selected quote from this server', '[quote number]', '']
        commands['quote_list'] = ['Posts all the quotes from this server', '', '']
        commands['add_quote'] = ['Adds the specified quote', '<"quote" - user>', '']
        commands['ricardo'] = ['Posts a random ricardo gif', '', '']
        commands['ricardobear'] = ['Posts the mighty ricardo bear', '', '']
        commands['bigricardo'] = ['Summons big ricardo', '', '']
        commands['wumpardo'] = ['Daddy Jack\'s wumpardo', '', '']
        commands['check_nsfw'] = ['Checks if nsfw is enabled on this server or not', '', '']
        commands['nsfw'] = ['Turns nsfw mode on or off (admin only)', '<on|off>', '']
        commands['change_prefix'] = ['Changes the command prefix on this server (admin only)', '<prefix>', '']
        commands['help, commands'] = ['It\'s this command', '[command]', '']
        commands['invite'] = ['Get the invite link', '', '']

        mode = sql_modes.check_mode(sv=ctx.guild.id)[0][0]   # returns list of tuples, use double index to get actual values
        prefix = sql_modes.get_prefix(ctx.guild.id)
        prefix = '.'

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
            msg += f'''\n\n<required parameter>; [optional parameter]; \'...\' variable number of parameters; \'|\' OR operator\n
This server\'s prefix is {prefix}
Type {prefix}help [command] for more info on a command.

Database is down, idk when it's gonna be back up, some functionality won't be available til then.```'''

        elif args[0] in commands:
            msg = f'```{prefix}{args[0]} {commands[args[0]][1]}\n\n{commands[args[0]][0]}```'  # command name and arguments (if needed)

        else:
            msg = 'No command called "'
            msg += ' '.join(args)
            msg += '" found.'
        await ctx.send(msg)

    @commands.command(when_mentioned=True)
    async def prefix(self, ctx):  # get the prefix for this server
        prefix = sql_modes.get_prefix(ctx.guild.id)
        await ctx.send(f'This server\'s prefix is `{prefix}`\nType {prefix}help to see a list of commands.')

    @commands.command()  # invite link
    async def invite(self, ctx):
        await ctx.send(INVITE)


def setup(bot):
    bot.add_cog(HelpCog(bot))
