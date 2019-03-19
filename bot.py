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
    if message.content.startswith('.'): # actual working prefix
        if message.author.bot: return # blocks bots from using commands

        cmd = message.content.split()[0].lower()[1:] # get the command from user message
        args = message.content.split(' ')[1:] # split the rest of the message

        for argCounter in range(0, len(args)):
            try:
                args.remove('')
            except Exception:
                pass

        # rape command
        if cmd == 'rape':
            possible_responses = [
            ' raped ',
            ' went to town with ',
            " creepy uncle'd ",
            ' priested ',
            ' step dadded '
            ]
            possible_responses_self = [
            'ya nasty',
            'ya nasty, but still raped yourself',
            'future you came to, well, cum.',
            'you went in the past to rape yourself',
            'you went to the future, to come back in the present to fuck yourself.'
            ]
            # self rape
            if args[0].replace('!', '') == message.author.mention.replace('!', '') or args[0] == message.author.mention.replace('!', ''):
                await client.send_message(message.channel, random.choice(possible_responses_self))
            # Vegas Bot rape
            elif args[0].replace('!', '') == '<@542697185339375616>':
                await client.send_message(message.channel, "You can't rape the Vegas Bot.")
            # other bots rape
            elif args[0].replace('!', '') == '<@367835200916291586>' or args[0].replace('!', '') == '<@389937555853934593>':
                await client.send_message(message.channel, 'Not a good idea to fuck a bot.')
            # all other rapes
            else:
                await client.send_message(message.channel, message.author.mention + random.choice(possible_responses) + ' '.join(args))

        if cmd == 'molest':
            # tag self
            if args[0].replace('!', '') == message.author.mention.replace('!', '') or args[0] == message.author.mention.replace('!', ''):
                await client.send_message(message.channel, message.author.mention + ' tried to molest themselves.')
            # tag vegas bot
            elif args[0].replace('!', '') == '<@542697185339375616>':
                await client.send_message(message.channel, 'You cannot molest the Vegas Bot.')
            else:
                await client.send_message(message.channel, message.author.mention + ' molested ' + ' '.join(args))

        if cmd == 'touch':
            # tag self
            if args[0].replace('!', '') == message.author.mention.replace('!', '') or args[0] == message.author.mention.replace('!', ''):
                await client.send_message(message.channel, message.author.mention + ' touched themselves reaaaaaal good.')
            # tag vegas bot
            elif args[0].replace('!', '') == '<@542697185339375616>':
                await client.send_message(message.channel, 'You may touch the Vegas Bot.')
            else:
                await client.send_message(message.channel, message.author.mention + ' touched ' + ' '.join(args))

        if cmd == 'fill':
            # tag self
            if args[0].replace('!', '') == message.author.mention.replace('!', '') or args[0] == message.author.mention.replace('!', ''):
                await client.send_message(message.channel, message.author.mention + ' filled... themselves up?')
            # tag vegas bot
            elif args[0].replace('!', '') == '<@542697185339375616>':
                await client.send_message(message.channel, 'You cannot fill the Vegas Bot.')
            else:
                await client.send_message(message.channel, message.author.mention + ' filled ' + ' '.join(args) + ' all the way up ;))')

        if cmd == 'succ':
            # tag self
            if args[0].replace('!', '') == message.author.mention.replace('!', '') or args[0] == message.author.mention.replace('!', ''):
                await client.send_message(message.channel, message.author.mention + ' got their own succ')
            # tag vegas bot
            elif args[0].replace('!', '') == '<@542697185339375616>':
                await client.send_message(message.channel, 'The Vegas Bot gave you the succ.')
            else:
                await client.send_message(message.channel, message.author.mention + ' gave ' + ' '.join(args) + ' dat good succ')

        if cmd == 'banana':
            await client.send_message(message.channel, ':banana: <:devinisdaddy:509088268420251650>')

        # rape for 2 tags or more
        if cmd == 'gangrape':
            possible_responses = [
            ' raped ',
            ' touched ',
            ' molested ',
            ' went to town with ',
            " creepy uncle'd ",
            ' filled the holes of ',
            ' priested ',
            ' step dadded '
            ]
            msg = message.author.mention + random.choice(possible_responses) + args[0]
            for argCounter in range(1, len(args)):
                msg += ' and ' + args[argCounter]
            await client.send_message(message.channel, msg)

        if cmd == 'bitchslap':
            #tag self
            if args[0].replace('!', '') == message.author.mention.replace('!', '') or args[0] == message.author.mention.replace('!', ''):
                await client.send_message(message.channel, message.author.mention + ' bitchslapped themselves')
            #tag vegas bot
            elif args[0].replace('!', '') == '<@542697185339375616>':
                await client.send_message(message.channel, 'You cannot bitchslap the Vegas Bot.')
            else:
                msg = message.author.mention + ' bitchslapped ' + ' '.join(args)
                await client.send_message(message.channel, msg)

        # random ricardo gif or meme
        if cmd == 'ricardo':
            possible_ricardos = [
            'https://tenor.com/2Aql.gif',
            'https://tenor.com/4f6F.gif',
            'https://tenor.com/3KGw.gif',
            'https://tenor.com/3WCg.gif',
            'https://tenor.com/3oVt.gif',
            'https://imgur.com/a/pM5R4UM',
            ]
            # if message.author.mention.replace('!', '') == '<@162966505430974464>':
            #     await client.send_message(message.channel, 'bad Arassii')
            # else:
            await client.send_message(message.channel, random.choice(possible_ricardos))

        # ricardo bear
        if cmd == 'ricardobear':
            await client.send_message(message.channel, '<a:ricardoBear:547813324079759360>')

        # fuck off meme
        if cmd == 'fuckoff':
            await client.send_message(message.channel, 'https://imgur.com/a/RMXA4xP')            

        # debug command to print all message args
        if cmd == 'getargs':
            for argCounter in range(0, len(args)):
                await client.send_message(message.channel, '`' + args[argCounter] + '`')

        # debug command for emotes
        if cmd == 'testemote':
            await client.send_message(message.channel, '<a:ricardoBear:547813324079759360>')

        if cmd == 'testsender':
            await client.send_message(message.channel, '`' + message.author.mention + '`')

        # invite link
        if cmd == 'invite':
            await client.send_message(message.channel, 'https://discordapp.com/api/oauth2/authorize?client_id=542697185339375616&permissions=379968&scope=bot')

        # help message with all the commands available
        if cmd == 'help':
            msg = '``` ```'

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with torp's ass"))
    print("Logged in as " + client.user.name)
    print("Current servers:")
    for server in client.servers:
        print(server.name)

# async def list_servers():
#     await client.wait_until_ready()
#     while not client.is_closed:
#         print("Current servers:")
#         for server in client.servers:
#             print(server.name)
#         await asyncio.sleep(600)


# client.loop.create_task(list_servers())
client.run(TOKEN)