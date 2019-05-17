import random
import discord
import db_queries
from collections import OrderedDict
from discord.ext import commands
from tokenfile import Vars


BOT_PREFIX = ('.', '$')  # not useless anymore
INVITE = 'https://discordapp.com/api/oauth2/authorize?client_id=542697185339375616&permissions=67619904&scope=bot'  # bot invite link
TOKEN = Vars.TOKEN  # bot app token
vegas_bot_tag = Vars.vegas_bot_tag  # vegas bot's discord tag
torp_tag = Vars.torp_tag  # big torpo's discord tag
bigric = Vars.bigric  # 49 fucking emotes

bot = commands.Bot(command_prefix=BOT_PREFIX)
bot.remove_command("help")  # removes default help command


@bot.command()  # rapes the tagged user or whatever gets typed
async def rape(ctx, *args):
    mode = db_queries.check_mode(sv=ctx.guild.id)[0][0]   # returns dict of tuples, use double index to get actual values
    if mode == 'sfw':
        await ctx.send("You're not supposed to use this command.")
    else:
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
        if args[0] == ctx.author.mention or args[0] == 'myself':
            await ctx.send(random.choice(possible_responses_self))
        # Vegas Bot rape
        elif args[0] == vegas_bot_tag:
            await ctx.send("You can't rape the Vegas Bot.")
        # all other rapes
        else:
            msg = ctx.author.mention + random.choice(possible_responses)
            for arg in args:
                msg += '{0} '.format(arg)
            await ctx.send(msg)


@bot.command()  # rape command clone
async def molest(ctx, *args):
    mode = db_queries.check_mode(sv=ctx.guild.id)[0][0]   # returns dict of tuples, use double index to get actual values
    if mode == 'sfw':
        await ctx.send("You're not supposed to use this command.")
    else:
        # tag self
        if args[0] == ctx.author.mention or args[0] == 'myself':
            await ctx.send('{0} tried to molest themselves.'.format(ctx.author.mention))
        # tag vegas bot
        elif args[0] == vegas_bot_tag:
            await ctx.send('You cannot molest the Vegas Bot.')
        else:
            msg = '{0} molested '.format(ctx.author.mention)
            for arg in args:
                msg += '{0} '.format(arg)
            await ctx.send(msg)


@bot.command()  # rape command clone
async def touch(ctx, *args):
    # tag self
    if args[0] == ctx.author.mention or args[0] == 'myself':
        await ctx.send('{0} touched themselves reaaaaaal good.'.format(ctx.author.mention))
    # tag vegas bot
    elif args[0] == vegas_bot_tag:
        if ctx.author.mention == torp_tag:  # torp tag
            await ctx.send('mmm yes daddy')
        else:  # non-torp tags
            await ctx.send('Only Torp can touch the Vegas Bot.')
    else:
        msg = '{0} touched '.format(ctx.author.mention)
        for arg in args:
            msg += '{0} '.format(arg)
        await ctx.send(msg)


@bot.command()  # rape command clone
async def fill(ctx, *args):
    # tag self
    if args[0] == ctx.author.mention or args[0] == 'myself':
        await ctx.send('{0} filled... themselves up?'.format(ctx.author.mention))
    # tag vegas bot
    elif args[0] == vegas_bot_tag:
        await ctx.send('You cannot fill the Vegas Bot.')
    else:
        msg = '{0} filled '.format(ctx.author.mention)
        for arg in args:
            msg += '{0} '.format(arg)
        msg += ' all the way up ;))'
        await ctx.send(msg)


@bot.command()  # rape command clone
async def succ(ctx, *args):
    # tag self
    if args[0] == ctx.author.mention or args[0] == 'myself':
        await ctx.send('{0} got their own succ'.format(ctx.author.mention))
    # tag vegas bot
    elif args[0] == vegas_bot_tag:
        await ctx.send('The Vegas Bot gave you the succ.')
    else:
        msg = '{0} gave '.format(ctx.author.mention)
        for arg in args:
            msg += '{0} '.format(arg)
        msg += ' dat good succ'
        await ctx.send(msg)


@bot.command()  # banan
async def banana(ctx):
    await ctx.send(':banana: <:medaddy:564806501215240192>')


@bot.command()  # rape for 2 tags
async def gangrape(ctx, *args):
    mode = db_queries.check_mode(sv=ctx.guild.id)[0][0]   # returns dict of tuples, use double index to get actual values
    if mode == 'sfw':
        await ctx.send("You're not supposed to use this command.")
    else:
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
        msg = ctx.author.mention + random.choice(possible_responses) + args[0]
        for arg in args[1:]:
            if arg == ' ':  # removes blank spaces
                break
            else:
                msg += ' and {0}'.format(arg)
        await ctx.send(msg)


@bot.command()  # random ricardo gif or meme
async def ricardo(ctx):
    possible_ricardos = [
        'https://tenor.com/2Aql.gif',
        'https://tenor.com/4f6F.gif',
        'https://tenor.com/3KGw.gif',
        'https://tenor.com/3WCg.gif',
        'https://tenor.com/3oVt.gif',
        'https://imgur.com/a/pM5R4UM',
        'https://imgur.com/a/3qtdO1e',
        '<a:ricardoBear:564806311791820810>',
        bigric
    ]

    await ctx.send(random.choice(possible_ricardos))


@bot.command()  # ricardo bear
async def ricardobear(ctx):
    await ctx.send('<a:ricardoBear:564806311791820810>')


@bot.command()  # big ricardo
async def bigricardo(ctx):
    await ctx.send(bigric)


@bot.command()  # bitchslaps the tagged user or whatever gets typed
async def bitchslap(ctx, *args):
    # tag self
    if args[0] == ctx.author.mention or args[0] == 'myself':
        await ctx.send('{0} bitchslapped themselves'.format(ctx.author.mention))
    # tag vegas bot
    elif args[0] == vegas_bot_tag:
        await ctx.send('You cannot bitchslap the Vegas Bot.')
    else:
        msg = '{0} bitchslapped '.format(ctx.author.mention)
        for arg in args:
            msg += '{0} '.format(ctx.author.mention)
        await ctx.send(msg)


@bot.command()  # fuck off meme
async def fuckoff(ctx):
    await ctx.send('https://imgur.com/a/RMXA4xP')


@bot.command()  # professional have standards meme
async def pro(ctx):
    await ctx.send('https://imgur.com/a/TE06C5s')


@bot.command()  # reeeeeeee
async def reee(ctx):
    await ctx.send('https://imgur.com/a/0QeJEHa')


@bot.command()  # challenge the tagged user
async def challenge(ctx, tag):
    possible_outcomes = [
        'tagged',
        'tagger',
        'no one'
    ]

    outcome = random.choice(possible_outcomes)

    if tag == vegas_bot_tag:
        await ctx.send("You always lose against Vegas Bot.")
    else:
        if outcome == 'tagged':
            if tag == ctx.author.mention:
                await ctx.send('You lost against... yourself?')
            else:
                await ctx.send('{0} won!'.format(tag))
                await ctx.send('{0} lost!'.format(ctx.author.mention))
        if outcome == 'tagger':
            if tag == ctx.author.mention:
                await ctx.send('You won! But also lost...?')
            else:
                await ctx.send('{0} won!'.format(ctx.author.mention))
                await ctx.send('{0} lost!'.format(tag))
        if outcome == 'no one':
            if tag == ctx.author.mention:
                await ctx.send('Both {0} and {1} lost!'.format(ctx.author.mention, tag))


@bot.command()  # invite link
async def invite(ctx):
    await ctx.send(INVITE)


@bot.command()  # wrong bot
async def fish(ctx):
    await ctx.send('Wrong bot, kiddo')


@bot.command()  # wrong bot again
async def pepo(ctx):
    await ctx.send('Wrong bot, kiddo')


@bot.command()  # wrong bot?
async def dad(ctx):
    await ctx.send("I'm dad")


@bot.command()
async def help(ctx, *args):
    commands = OrderedDict()
    commands['rape'] = ["Non consensual sex with your preferred person/object (nsfw only)", '[arg]', 'nsfw']
    commands['molest'] = ['Same as .rape, but different reply (nsfw only)', '[arg]', 'nsfw']
    commands['touch'] = ['Touchy touchy', '[arg]', '']
    commands['fill'] = [';))', '[arg]', '']
    commands['succ'] = ['Give someone of your choosing dat good succ', '[arg]', '']
    commands['banana'] = ['If you really need potassium', '', '']
    commands['gangrape'] = ['When one is not enough (nsfw only)', '[args...]', 'nsfw']
    commands['ricardo'] = ['Posts a random ricardo gif', '', '']
    commands['ricardobear'] = ['Posts the mighty ricardo bear', '', '']
    commands['bitchslap'] = ['Exactly what it sounds like', '', '']
    commands['fuckoff'] = ['Just fuck off mate', '', '']
    commands['pro'] = ['Professionals have standards', '', '']
    commands['reee'] = ['Autistic screeching of the highest quality', '', '']
    commands['challenge'] = ['Challenge another user', '[arg]', '']
    commands['invite'] = ['Get the invite link', '', '']
    commands['nsfw'] = ['Turns nsfw mode on or off (admin only)', "$on/$off", '']
    commands['check_nsfw'] = ['Checks if nsfw is enabled on this server or not', '', '']
    commands['help'] = ["It's this command you dummy", '', '']

    mode = db_queries.check_mode(sv=ctx.guild.id)[0][0]   # returns dict of tuples, use double index to get actual values

    if len(args) == 0:  # get longest command name, to have evenly spaced help message
        max_len = 0
        for cmd in commands:
            if len(cmd) > max_len:
                max_len = len(cmd)

        msg = '```'

        for command, desc in commands.items():  # for every command in the commands dict
            if mode != 'nsfw' and desc[2] == 'nsfw':
                continue
            msg += '.{0} '.format(command)  # command name
            for a in range(len(command), max_len):  # extra spaces
                msg += ' '
            msg += '{0}\n'.format(desc[0])  # add the description

        msg += '\n\nType .help [command] for more info on a command.```'

    elif args[0] in commands:
        msg = '```.{0} {1}\n\n{2}```'.format(args[0], commands[args[0]][1], commands[args[0]][0])  # command name and arguments (if needed)

    else:
        msg = 'No command called "'
        for arg in args:  # add all *args items in a string format
            msg += '{0} '.format(arg)
        msg = msg[:-1]  # remove the last space
        msg += '" found.'
    await ctx.send(msg)


### debug commands ###

@bot.command()  # ping command
async def ping(ctx):
    await ctx.send("pong")


@bot.command()  # say args
async def say(ctx, *args):
    if ctx.author.mention == torp_tag:
        msg = ''
        for x in args:
            msg += ' {0}'.format(x)
        await ctx.send(msg)
    else:
        await ctx.send('You do not have permission to use this command.')


@bot.command()  # sends first word from message
async def getargs(ctx, tag):
    if ctx.author.mention == torp_tag:
        await ctx.send('`{0}`'.format(tag))
    else:
        await ctx.send('You do not have permission to use this command.')


@bot.command()  # get current server id
async def getguild(ctx):
    if ctx.author.mention == torp_tag:
        await ctx.send(ctx.guild.id)
    else:
        await ctx.send('You do not have permission to use this command.')


@bot.command()  # emote testing
async def testemote(ctx, tag):
    if ctx.author.mention == torp_tag:
        await ctx.send('<a:Nig:557976066828926986>')
    else:
        await ctx.send('You do not have permission to use this command.')


@bot.command()  # leaves guild specified and prints in console
async def leave(ctx, arg):
    if ctx.author.mention == torp_tag:
        for server in bot.guilds:
            if str(server.id) == str(arg):
                await server.leave()
                print('Left "{0}": {1}'.format(server.name, server.id))
    else:
        await ctx.send('You do not have permission to use this command.')


### mysql ###

@bot.command()  # changes nsfw on or off
async def nsfw(ctx, arg):
    if ctx.author.mention == torp_tag:
        if arg == 'on':
            db_queries.change_mode(sv=ctx.guild.id, md='nsfw')
            await ctx.send("Gettin' extra naughty now :))")
        elif arg == 'off':
            await ctx.send("Don't tell mommy")
            db_queries.change_mode(sv=ctx.guild.id, md='sfw')
        else:
            await ctx.send("Invalid argument")
    else:
        await ctx.send('You do not have permission to use this command.')


@bot.command()  # manually adds server where command was called
async def add_server_db(ctx):
    db_queries.new_server(sv=ctx.guild.id, md='sfw')


@bot.command()  # checks mode of server where command was called
async def check_nsfw(ctx):
    mode = db_queries.check_mode(sv=ctx.guild.id)[0][0]   # returns dict of tuples, use double index to get actual values
    if mode == 'nsfw':
        await ctx.send("I can be very naughty :))")
    else:
        await ctx.send("I'm innocent, I swear")
    await ctx.send(mode)


### bot stuff ###

@bot.event  # prints message in console with name and id of guild joined
async def on_guild_join(guild):
    print('Joined "{0}": {1}\n'.format(guild.name, guild.id))
    db_queries.new_server(sv=str(guild.id), md='sfw')
    print("Added '{0}' to db\n\n".format(guild.id))


@bot.event
async def on_ready():
    game = discord.Game("with the big boys")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("Logged in as {0}".format(bot.user.name))
    print("Current servers:")
    for server in bot.guilds:
        print('{0}: {1}'.format(server.name, server.id))
    print('\n{0}\n\n'.format(db_queries.db))

bot.run(TOKEN)
