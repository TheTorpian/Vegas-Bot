import discord
# import asyncio
from discord.ext import commands
from sql import sql_modes
from tokenfile import Vars

TOKEN = Vars.TOKEN


def get_pref(bot, message):
    prefix = sql_modes.get_prefix(message.guild.id)
    return prefix


initial_extensions = [
    'cogs.sfw',
    'cogs.nsfw',
    'cogs.quotes',
    'cogs.ricardo',
    'cogs.help',
    'cogs.debug',
    'cogs.admin'
]

bot = commands.Bot(command_prefix=get_pref)
bot.remove_command('help')  # removes default help command

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


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
    game = discord.Game('with the big boys')
    await bot.change_presence(status=discord.Status.online, activity=game)
    print(f'Logged in as {bot.user.name}')
    print('Current servers:')
    for server in bot.guilds:
        print(f'{server.name}: {server.id}')
    print(f'\n{sql_modes.db}\n\n')

bot.run(TOKEN, reconnect=True)


# def handle_exit():
#     print("Handling")
#     bot.loop.run_until_complete(bot.logout())
#     for t in asyncio.Task.all_tasks(loop=bot.loop):
#         if t.done():
#             t.exception()
#             continue
#         t.cancel()
#         try:
#             bot.loop.run_until_complete(asyncio.wait_for(t, 5, loop=bot.loop))
#             t.exception()
#         except asyncio.InvalidStateError:
#             pass
#         except asyncio.TimeoutError:
#             pass
#         except asyncio.CancelledError:
#             pass


# while True:
#     try:
#         bot.loop.run_until_complete(bot.start(TOKEN))
#     except SystemExit:
#         handle_exit()
#     except KeyboardInterrupt:
#         handle_exit()
#         bot.loop.close()
#         print("Program ended")
#         break

#     print("Bot restarting")
#     bot = discord.Client(loop=bot.loop)
