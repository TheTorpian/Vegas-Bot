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
});
client.on('message', function (user, userID, channelID, message, evt) {
    // Our bot needs to know if it will execute a command
    // It will listen for messages that will start with prefix
    if (message.substring(0, 1) == prefix) {
        var args = message.substring(1).split(' ');
        var cmd = args[0];
       
        //args = args.splice(1);
        switch(cmd) {
            // .ping
            case 'ping':
                client.sendMessage({
                    to: channelID,
                    message: 'Pong!'
                });
            break;

            // .rape
            case 'rape':
                var rapee = args[1];
                //if args[1] is a user tag
                if (rapee.substring(0, 2) == '<@'){
                    client.sendMessage({
                        to: channelID,
                        message: rapee + ', ' + '<@' + userID + '>' + ' raped you!'
                    });
                }
                //if tag is vegas bot (doesn't work)
                else if (rapee == '<@542697185339375616>' || rapee == '@Vegas'){
                    client.sendMessage({
                        to: channelID,
                        message: 'You cannot rape the Vegas Bot.'
                    });
                }
                //not a user tag
                else {
                    client.sendMessage({
                        to: channelID,
                        message: 'Invalid user.'
                    });
                }
            break;
        }
    }
});