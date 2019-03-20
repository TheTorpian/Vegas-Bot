import random
import asyncio
import aiohttp
import json
import discord
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ('.', '$') # currently useless
TOKEN = 'NTQyNjk3MTg1MzM5Mzc1NjE2.Dz-SCg._sflidalhgN-_Upl6W9OPX1w1o4' # Get at discordapp.com/developers/applications/me
INVITE = 'https://discordapp.com/api/oauth2/authorize?client_id=542697185339375616&permissions=379968&scope=bot' # bot invite link

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
    if message.content.startswith('.'): # actual working prefix
        if message.author.bot: return # blocks bots from using commands

        cmd = message.content.split()[0].lower()[1:] # get the command from user message
        args = message.content.split(' ')[1:] # split the rest of the message

        authorTag = message.author.mention.replace('!', '')
        vegasBotTag = '<@542697185339375616>'
        tag = ' '
        try:
            if args[0][:1] == '<': # if first arg is a tag, make a variable
                tag = args[0].replace('!', '')
        except Exception:
            pass

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
            if tag == authorTag:
                await client.send_message(message.channel, random.choice(possible_responses_self))
            # Vegas Bot rape
            elif tag == vegasBotTag:
                await client.send_message(message.channel, "You can't rape the Vegas Bot.")
            # all other rapes
            else:
                await client.send_message(message.channel, message.author.mention + random.choice(possible_responses) + ' '.join(args))

        if cmd == 'molest':
            # tag self
            if tag == authorTag:
                await client.send_message(message.channel, message.author.mention + ' tried to molest themselves.')
            # tag vegas bot
            elif tag == vegasBotTag:
                await client.send_message(message.channel, 'You cannot molest the Vegas Bot.')
            else:
                await client.send_message(message.channel, message.author.mention + ' molested ' + ' '.join(args))

        if cmd == 'touch':
            # tag self
            if tag == authorTag:
                await client.send_message(message.channel, message.author.mention + ' touched themselves reaaaaaal good.')
            # tag vegas bot
            elif tag == vegasBotTag:
                await client.send_message(message.channel, 'You may touch the Vegas Bot.')
            else:
                await client.send_message(message.channel, message.author.mention + ' touched ' + ' '.join(args))

        if cmd == 'fill':
            # tag self
            if tag == authorTag:
                await client.send_message(message.channel, message.author.mention + ' filled... themselves up?')
            # tag vegas bot
            elif tag == vegasBotTag:
                await client.send_message(message.channel, 'You cannot fill the Vegas Bot.')
            else:
                await client.send_message(message.channel, message.author.mention + ' filled ' + ' '.join(args) + ' all the way up ;))')

        if cmd == 'succ':
            # tag self
            if tag == authorTag:
                await client.send_message(message.channel, message.author.mention + ' got their own succ')
            # tag vegas bot
            elif tag == vegasBotTag:
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
            # if authorTag == '<@162966505430974464>':
            #     await client.send_message(message.channel, 'bad Arassii')
            # else:
            await client.send_message(message.channel, random.choice(possible_ricardos))

        # ricardo bear
        if cmd == 'ricardobear':
            await client.send_message(message.channel, '<a:ricardoBear:547813324079759360>')

        # bitchslaps the tagged user
        if cmd == 'bitchslap':
            #tag self
            if tag == authorTag:
                await client.send_message(message.channel, message.author.mention + ' bitchslapped themselves')
            #tag vegas bot
            elif tag == vegasBotTag:
                await client.send_message(message.channel, 'You cannot bitchslap the Vegas Bot.')
            else:
                msg = message.author.mention + ' bitchslapped ' + ' '.join(args)
                await client.send_message(message.channel, msg)

        # fuck off meme
        if cmd == 'fuckoff':
            await client.send_message(message.channel, 'https://imgur.com/a/RMXA4xP')

        # challenge the tagged user
        if cmd == 'challenge':
            possible_outcomes = [
            'tagged',
            'tagger',
            'no one',
            ]

            outcome = random.choice(possible_outcomes)

            if tag == vegasBotTag:
                await client.send_message(message.channel, "You always lose against Vegas Bot.")
            else:
                if outcome == 'tagged':
                    if tag == authorTag:
                        await client.send_message(message.channel, 'You lost against... yourself?')
                    else:
                        await client.send_message(message.channel, tag + ' won!')
                if outcome == 'tagger':
                    if tag == authorTag:
                        await client.send_message(message.channel, 'You won! But also lost...?')
                    else:
                        await client.send_message(message.channel, message.author.mention + ' won!')
                if outcome == 'no one':
                    if tag == authorTag:
                        await client.send_message(message.channel, 'You REALLY lost against yourself')
                    else:
                        await client.send_message(message.channel, 'You both lost!')

        # invite link
        if cmd == 'invite':
            await client.send_message(message.channel, INVITE)

        # debug command to print all message args
        if cmd == 'getargs':
            for arg in args:
                await client.send_message(message.channel, '`' + arg + '`')

        # debug command for emotes
        if cmd == 'testemote':
            await client.send_message(message.channel, '<a:Nig:557976066828926986>')

        # get the message sender ID
        if cmd == 'testsender':
            await client.send_message(message.channel, '`' + message.author.mention + '`')

        # for lil gay boy arassii
        if cmd == 'ass':
            await client.send_message(message.channel, '<@162966505430974464>')
            await client.send_message(message.channel, '<@162966505430974464>')
            await client.send_message(message.channel, '<@162966505430974464>')

        # embed with all the commands available
        if cmd == 'help':
            commands = {}
            commands['.rape'] = "Non consensual sex with your preferred person/object (no judgin')"
            commands['.molest'] = 'Same as .rape, but different reply'
            commands['.touch'] = 'Same as .rape, but different reply'
            commands['.fill'] = ';))'
            commands['.succ'] = 'Give someone of your choosing dat good succ'
            commands['.banana'] = 'If you really need potassium'
            commands['.gangrape'] = 'When one is not enough'
            commands['.ricardo'] = 'Posts a random ricardo gif'
            commands['.ricardobear'] = 'Posts the mighty ricardo bear'
            commands['.bitchslap'] = 'Exactly what it sounds like'
            commands['.fuckoff'] = 'Just fuck off mate'
            commands['.challenge'] = 'Challenge another user'
            commands['.invite'] = 'Get the invite link'
            commands['.help'] = "It's this command you dummy"
            commands['.newcommands'] = 'See if any new commands have been added'

            msg = discord.Embed(title = 'Vegas Bot commands:', description = '', color = 0x0000ff)
            for command, descr in commands.items():
                msg.add_field(name = command, value = descr, inline = False)
            await client.send_message(message.channel, embed = msg)

        # embed with the latest commands added
        if cmd == 'newcommands':
            commands = {}
            commands['.help'] = 'Now you can finally see all of the available commands!'
            commands['.challenge'] = 'Challenge another user'
            msg = discord.Embed(title = 'New commands:', description = '', color = 0x0000ff)
            for command, descr in commands.items():
                msg.add_field(name = command, value = descr, inline = False)
            await client.send_message(message.channel, embed = msg)


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