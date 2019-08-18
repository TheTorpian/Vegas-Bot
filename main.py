import discord
from datetime import datetime
from discord.ext import commands
from sql import sql_modes
from tokenfile import Vars
import subprocess

TOKEN = Vars.TOKEN
torp_tag = Vars.torp_tag
restart_bat = Vars.restart_bat


def get_prefix(bot, message):
    prefix = sql_modes.get_prefix(message.guild.id)
    return commands.when_mentioned_or(prefix)(bot, message)


cogs = [
    'cogs.sfw',
    'cogs.nsfw',
    'cogs.quotes',
    'cogs.ricardo',
    'cogs.help',
    'cogs.debug',
    'cogs.admin',
    'cogs.error_handler'
]

bot = commands.Bot(command_prefix=get_prefix)
bot.remove_command('help')  # removes default help command

if __name__ == '__main__':
    for cog in cogs:
        bot.load_extension(cog)


@bot.command(name='reload', pass_context=True)  # reloads all cogs
@commands.check(Vars.user_is_me)
async def _reload(ctx):
    try:
        for cog in cogs:
            bot.unload_extension(cog)
            bot.load_extension(cog)
        await ctx.send('Cogs reloaded successfully!')
    except Exception:
        await ctx.send('An error occurred')


@bot.command(name='restart', pass_context=True)  # restarts bot app
@commands.check(Vars.user_is_me)
async def _restart(ctx):
    channel = bot.get_channel(581478717046521880)
    await channel.send('Restarting...')
    print('Logging out...\n')
    subprocess.call(restart_bat)  # calls batch file (it runs the main .py file)
    await bot.logout()  # logs out the app


@bot.event  # prints message in console with name and id of guild joined
async def on_guild_join(guild):
    print(f'Joined \'{guild.name}\': {guild.id}\n')
    sql_modes.new_server(sv=str(guild.id), md='sfw')
    print(f'Added \'{guild.id}\' to db\n')
    print('Current servers:')
    for server in bot.guilds:
        print(f'{server.name}: {server.id}')
    print('\n\n')


@bot.event
async def on_ready():
    game = discord.Activity(name='Torp wasting his life', type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.online, activity=game)
    print(f'{datetime.now()}')
    print(f'Logged in as {bot.user.name}')
    print('Current servers:')
    for server in bot.guilds:
        print(f'{server.name}: {server.id}')
    print(f'\n{sql_modes.db}\n\n')
    channel = bot.get_channel(581478717046521880)
    await channel.send('Ready!')

bot.run(TOKEN, bot=True, reconnect=True)
