var Discord = require('discord.io');
var logger = require('winston');
var auth = require('./auth.json');
const prefix = '.';

//idfk what logger is for

// Configure logger settings
// logger.remove(logger.transports.Console);
// logger.add(logger.transports.Console, {
//     colorize: true
// });
//logger.level = 'debug';

// Initialize Discord Bot
var client = new Discord.Client({
   token: auth.token,
   autorun: true
});
client.on('ready', function (evt) {
    logger.info('Connected');
    logger.info('Logged in as: ');
    logger.info(client.username + ' - (' + client.id + ')');
    client.setPresence( {game: {name:"with bitches"}} );
});
client.on('message', function (user, userID, channelID, message, evt) {
    // Our bot needs to know if it will execute a command
    // It will listen for messages that will start with prefix
    if (message.substring(0, 1) == prefix) {
        var args = message.substring(1).split(' ');
        var cmd = args[0];
       
        //args = args.splice(1);
        switch(cmd) {
            // .rape
            case 'rape':
                var rapee = args[1];
                //if args[1] is a user tag
                if (rapee.substring(0, 2) == '<@'){
                    //if tag is vegas bot
                    if (rapee == '<@542697185339375616>'){
                        client.sendMessage({
                            to: channelID,
                            message: 'You cannot rape the Vegas Bot.'
                        });
                    }
                    //if tags are other bots
                    else if (rapee == '<@367835200916291586>' || rapee == '<@389937555853934593>'){
                        client.sendMessage({
                            to: channelID,
                            message: "It's not a good idea to fuck a bot."
                        });
                    }
                    //if tag is a valid user
                    else {
                        client.sendMessage({
                            to: channelID,
                            message: rapee + ', ' + '<@' + userID + '>' + ' raped you!'
                        });
                    }
                }
                //not a user tag
                else {
                    client.sendMessage({
                        to: channelID,
                        message: 'Invalid user.'
                    });
                }
            break;
            //test function to display args
            case 'rapeTest':
                var rapee = args[1];
                if (rapee.substring(0, 2) == '<@'){
                    client.sendMessage({
                        to: channelID,
                        message: 'user tag: `' + rapee + '`, ' + 'sender: `' + userID + '`'
                    });
                }
        }
    }
});