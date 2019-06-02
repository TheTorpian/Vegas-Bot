import discord
from discord.ext import commands
from sql import sql_modes
from tokenfile import Vars

TOKEN = Vars.TOKEN
torp_tag = Vars.torp_tag


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
    for cog in cogs:
        bot.load_extension(cog)
    game = discord.Game('with the big boys')
    await bot.change_presence(status=discord.Status.online, activity=game)
    print(f'Logged in as {bot.user.name}')
    print('Current servers:')
    for server in bot.guilds:
        print(f'{server.name}: {server.id}')
    print(f'\n{sql_modes.db}\n\n')

bot.run(TOKEN, reconnect=True)
