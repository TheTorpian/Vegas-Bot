import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ('.', '$') #currently useless
TOKEN = 'NTQyNjk3MTg1MzM5Mzc1NjE2.Dz-SCg._sflidalhgN-_Upl6W9OPX1w1o4'  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
    if message.content.startswith('.'): #actual working prefix
        if message.author.bot: return # blocks bots from using commands

        usrTag = 0
        cmd = message.content.split()[0].lower()[1:] #get the command from user message
        args = message.content.split(' ')[1:] #split the rest of the message

        #rape command
        if cmd == 'rape' or cmd == 'molest' or cmd == 'touch':
            possible_responses = [
            'raped ',
            'touched ',
            'molested ',
            'went to town with ',
            "creepy uncle'd ",
            'filled the holes of ',
            'priested ',
            'step dadded '
            ]
            # while args[usrTag] == ' ':
            #     usrTag += 1
            #self rape
            if args[usrTag].replace('!', '') == message.author.mention.replace('!', '') or args[usrTag] == message.author.mention.replace('!', ''):
                await client.send_message(message.channel, 'ya nasty')
            #Vegas Bot rape
            elif args[usrTag].replace('!', '') == '<@542697185339375616>':
                await client.send_message(message.channel, "Don't try to rape the Vegas Bot.")
            #other bots rape
            elif args[usrTag].replace('!', '') == '<@367835200916291586>' or args[usrTag].replace('!', '') == '<@389937555853934593>':
                await client.send_message(message.channel, "Not a good idea to fuck a bot.")
            #all other rapes
            else:
                await client.send_message(message.channel, message.author.mention + ' ' + random.choice(possible_responses) + ' '.join(args))

        #rape for 2 tags
        if cmd == 'gangrape':
            possible_responses = [
            'raped ',
            'touched ',
            'molested ',
            'went to town with ',
            "creepy uncle'd ",
            'filled the holes of ',
            'priested ',
            'step dadded'
            ]
            await client.send_message(message.channel, message.author.mention + ' ' +
            random.choice(possible_responses) + args[0] + ' and ' + args[1])

        if cmd == 'getid':           
            await client.send_message(message.channel, '`' + message.author.mention + '`')
            await client.send_message(message.channel, '`' + args[0] + '`')

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with more bitches"))
    print("Logged in as " + client.user.name)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)