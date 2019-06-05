import traceback
import sys
from discord.ext import commands


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        ctx   : Context
        error : Exception"""

        if hasattr(ctx.command, 'on_error'):  # return if command has local error handler
            return

        ignored = (commands.CommandNotFound, commands.UserInputError)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):  # return if error should just be ignored
            return

        elif isinstance(error, commands.MissingPermissions):  # user missing perms to use command
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = f'{"**, **".join(missing[:-1])}, and {missing[-1]}'
            else:
                fmt = ' and '.join(missing)
            _message = f'You talk a lotta shit for someone who doesn\'t have the {fmt} permission(s).'
            await ctx.send(_message)

        print(f'Ignoring exception in command {ctx.command}:', file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        print('\n\n')


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
