import db_queries
import discord
from discord.ext import commands
from tokenfile import Vars


def get_pref(bot, message):
    prefix = db_queries.get_prefix(message.guild.id)
    return prefix


initial_extensions = [
    'cogs.sfw',
    'cogs.nsfw',
    'cogs.ricardo',
    'cogs.help',
    'cogs.debug',
    'cogs.admin'
]

TOKEN = Vars.TOKEN  # bot app token

bot = commands.Bot(command_prefix=get_pref)
bot.remove_command('help')  # removes default help command

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


@bot.event  # prints message in console with name and id of guild joined
async def on_guild_join(guild):
    print(f'Joined \'{guild.name}\': {guild.id}\n')
    db_queries.new_server(sv=str(guild.id), md='sfw')
    print(f'Added \'{guild.id}\' to db\n\n')


@bot.event
async def on_ready():
    game = discord.Game('pretend I\'m offline')
    await bot.change_presence(status=discord.Status.dnd, activity=game)
    print(f'Logged in as {bot.user.name}')
    print('Current servers:')
    for server in bot.guilds:
        print(f'{server.name}: {server.id}')
    print(f'\n{db_queries.db}\n\n')

bot.run(TOKEN)
