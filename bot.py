import random
# import asyncio
# import aiohttp
# import json
import discord
from discord import Game
from discord.ext import commands
# from discord.ext.commands import Bot

BOT_PREFIX = ('.', '$') # not useless anymore
TOKEN = 'NTQyNjk3MTg1MzM5Mzc1NjE2.D3pP8Q.drE_pnxP5brFR_JIDvDY-IjvTWw' # Get at discordapp.com/developers/applications/me
INVITE = 'https://discordapp.com/api/oauth2/authorize?client_id=542697185339375616&permissions=379968&scope=bot' # bot invite link
vegasBotTag = '<@542697185339375616>'

bot = commands.Bot(command_prefix = BOT_PREFIX)
# bot.remove_command("help")

@bot.command()
async def rape(ctx, *args):
    '''
    Non consensual sex with your preferred person/object (no judgin')
    '''
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
    if args[0] == ctx.author.mention:
        await ctx.send(random.choice(possible_responses_self))
    # Vegas Bot rape
    elif args[0] == vegasBotTag:
        await ctx.send("You can't rape the Vegas Bot.")
    # all other rapes
    else:
        msg = ctx.author.mention + random.choice(possible_responses)
        for arg in args:
            msg += arg + ' '   
        await ctx.send(msg)

@bot.command()
async def molest(ctx, *args):
    '''
    Same as .rape, but different reply
    '''
    # tag self
    if args[0] == ctx.author.mention:
        await ctx.send(ctx.author.mention + ' tried to molest themselves.')
    # tag vegas bot
    elif args[0] == vegasBotTag:
        await ctx.send('You cannot molest the Vegas Bot.')
    else:
        msg = ctx.author.mention + ' molested '
        for arg in args:
            msg += arg + ' '  
        await ctx.send(msg)

@bot.command()
async def touch(ctx, *args):
    '''
    Same as .rape, but different reply
    '''
    # tag self
    if args[0] == ctx.author.mention:
        await ctx.send(ctx.author.mention + ' touched themselves reaaaaaal good.')
    # tag vegas bot
    elif args[0] == vegasBotTag:
        if ctx.author.mention == '<@249550049564950530>': # torp tag
            await ctx.send('mmm yes daddy')
        else: # non-torp tags
            await ctx.send('Only Torp can touch the Vegas Bot.')
    else:
        msg = ctx.author.mention + ' touched '
        for arg in args:
            msg += arg + ' '  
        await ctx.send(msg)

@bot.command()
async def fill(ctx, *args):
    '''
    ;))
    '''
    # tag self
    if args[0] == ctx.author.mention:
        await ctx.send(ctx.author.mention + ' filled... themselves up?')
    # tag vegas bot
    elif args[0] == vegasBotTag:
        await ctx.send('You cannot fill the Vegas Bot.')
    else:
        msg = ctx.author.mention + ' filled '
        for arg in args:
            msg += arg + ' '
        msg += ' all the way up ;))'
        await ctx.send(msg)

@bot.command()
async def succ(ctx, *args):
    '''
    Give someone of your choosing dat good succ
    '''
    # tag self
    if args[0] == ctx.author.mention:
        await ctx.send(ctx.author.mention + ' got their own succ')
    # tag vegas bot
    elif args[0] == vegasBotTag:
        await ctx.send('The Vegas Bot gave you the succ.')
    else:
        msg = ctx.author.mention + ' gave '
        for arg in args:
            msg += arg + ' '
        msg += ' dat good succ'
        await ctx.send(msg)

@bot.command()
async def banana(ctx):
    '''
    If you really need some potassium
    '''
    await ctx.send(':banana: <:devinisdaddy:509088268420251650>')

# rape for 2 tags
@bot.command()
async def gangrape(ctx, *args):
    '''
    Currently reworking
    '''
    # possible_responses = [
    # ' raped ',
    # ' touched ',
    # ' molested ',
    # ' went to town with ',
    # " creepy uncle'd ",
    # ' filled the holes of ',
    # ' priested ',
    # ' step dadded '
    # ]
    # msg = ctx.author.mention + random.choice(possible_responses) + args[0]
    # for arg in args[1:]:
    #     msg += ' and ' + arg
    # await ctx.send(msg)

    ### legacy code for variable number of args ###

    # msg = ctx.author.mention + random.choice(possible_responses) + arg1
    # for argCounter in range(1, len(args)):
    #     msg += ' and ' + args[argCounter]
    # await ctx.send(ctx.author.mention + random.choice(possible_responses) + arg1 + ' and ' + arg2)

    await ctx.send('nah')

# random ricardo gif or meme
@bot.command()
async def ricardo(ctx):
    '''
    Posts a random ricardo gif
    '''
    possible_ricardos = [
    'https://tenor.com/2Aql.gif',
    'https://tenor.com/4f6F.gif',
    'https://tenor.com/3KGw.gif',
    'https://tenor.com/3WCg.gif',
    'https://tenor.com/3oVt.gif',
    'https://imgur.com/a/pM5R4UM',
    ]

    # if ctx.author.mention == '<@162966505430974464>':
    #     await ctx.send('bad Arassii')
    # else:
    await ctx.send(random.choice(possible_ricardos))

# ricardo bear
@bot.command()
async def ricardobear(ctx):
    '''
    Summons the mighty ricardo bear
    '''
    # await ctx.send('<a:ricardoBear:547813324079759360>')
    await ctx.send('Mighty ricardo bear cannot be summoned at the moment :(')

# bitchslaps the tagged user
@bot.command()
async def bitchslap(ctx, *args):
    '''
    Exactly what it sounds like
    '''
    #tag self
    if arg[0] == ctx.author.mention or arg[0] == 'myself':
        await ctx.send(ctx.author.mention + ' bitchslapped themselves')
    #tag vegas bot
    elif arg[0] == vegasBotTag:
        await ctx.send('You cannot bitchslap the Vegas Bot.')
    else:
        msg = ctx.author.mention + ' bitchslapped '
        for arg in args:
            msg += arg + ' '
        await ctx.send(msg)

# fuck off meme
@bot.command()
async def fuckoff(ctx):
    '''
    Just fuck off mate
    '''
    await ctx.send('https://imgur.com/a/RMXA4xP')

# professional have standards meme
@bot.command()
async def pro(ctx):
    '''
    Professionals have standards
    '''
    await ctx.send('https://imgur.com/a/TE06C5s')

# reeeeeeee
@bot.command()
async def reee(ctx):
    '''
    Autistic screeching of the highest quality
    '''
    await ctx.send('https://imgur.com/a/0QeJEHa')

# challenge the tagged user
@bot.command()
async def challenge(ctx, tag):
    '''
    Challenge another user
    '''
    possible_outcomes = [
    'tagged',
    'tagger',
    'no one'
    ]

    outcome = random.choice(possible_outcomes)

    if tag == vegasBotTag:
        await ctx.send("You always lose against Vegas Bot.")
    else:
        if outcome == 'tagged':
            if tag == ctx.author.mention:
                await ctx.send('You lost against... yourself?')
            else:
                await ctx.send(tag + ' won!')
                await ctx.send(ctx.author.mention + ' lost!')
        if outcome == 'tagger':
            if tag == ctx.author.mention:
                await ctx.send('You won! But also lost...?')
            else:
                await ctx.send(ctx.author.mention + ' won!')
                await ctx.send(tag + ' lost!')
        if outcome == 'no one':
            if tag == ctx.author.mention:
                await ctx.send('Both ' + ctx.author.mention + ' and ' + tag + ' lost!')

@bot.command()
async def assi(ctx):
    '''
    for lil gay boy arassii
    '''
    await ctx.send('<@162966505430974464>')
    await ctx.send('<@162966505430974464>')
    await ctx.send('<@162966505430974464>')

#wrong bot
@bot.command()
async def fish(ctx):
    '''
    use t!fish next time
    '''
    await ctx.send('Wrong bot, kiddo')            

# invite link
@bot.command()
async def invite(ctx):
    '''
    Get the invite link for this bot
    '''
    await ctx.send(INVITE)



### debug commands ###

# # debug command to print all message args
# @bot.command()
# async def getargs(ctx, tag):
#     '''
#     debug command, go away
#     '''
#     await ctx.send('`' + tag + '`')

# # debug command for emotes
# @bot.command()
# async def testemote(ctx, tag):
#     '''
#     debug command, go away
#     '''
#     await ctx.send('<a:Nig:557976066828926986>')



### legacy help commands ###

# # embed with all the commands available
# if cmd == 'commands':
#     commands = {}
#     commands['.rape'] = "Non consensual sex with your preferred person/object (no judgin')"
#     commands['.molest'] = 'Same as .rape, but different reply'
#     commands['.touch'] = 'Same as .rape, but different reply'
#     commands['.fill'] = ';))'
#     commands['.succ'] = 'Give someone of your choosing dat good succ'
#     commands['.banana'] = 'If you really need potassium'
#     commands['.gangrape'] = 'When one is not enough'
#     commands['.ricardo'] = 'Posts a random ricardo gif'
#     commands['.ricardobear'] = 'Posts the mighty ricardo bear'
#     commands['.bitchslap'] = 'Exactly what it sounds like'
#     commands['.fuckoff'] = 'Just fuck off mate'
#     commands['.pro'] = 'Professionals have standards'
#     commands['.reee'] = 'Autistic screeching of the highest quality'
#     commands['.challenge'] = 'Challenge another user'
#     commands['.invite'] = 'Get the invite link'
#     commands['.help'] = "It's this command you dummy"
#     commands['.newcommands'] = 'See if any new commands have been added'

#     msg = discord.Embed(title = 'Vegas Bot commands:', description = '', color = 0x0000ff)
#     for command, descr in commands.items():
#         msg.add_field(name = command, value = descr, inline = False)
#     await ctx.send(embed = msg)

# # embed with the latest commands added
# if cmd == 'newcommands':
#     commands = {}
#     commands['.pro'] = 'Standards mate'
#     commands['.reee'] = 'reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
#     msg = discord.Embed(title = 'New commands:', description = '', color = 0x0000ff)
#     for command, descr in commands.items():
#         msg.add_field(name = command, value = descr, inline = False)
#     await ctx.send(embed = msg)

@bot.event
async def on_ready():
    game = discord.Game("dm for feedback")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("Logged in as " + bot.user.name)
    print("Current servers:")
    for server in bot.guilds:
        print(server.name)

bot.run(TOKEN)