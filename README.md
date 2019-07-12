# Vegas-Bot
A discord bot I made for fun; gets its name from the server it was initally made for and not any gambling related functions you may expect it to have.
# Invite
I made this mostly for myself and a few selected servers, if you really want to use this bot I recommend hosting it yourself.
# Use
Make a bot app [here](https://discordapp.com/developers/applications/). 
Make a file called `tokenfile.py`, create a class called `Vars` and paste this in it: `TOKEN = {}`; replace `{}` with the token from your bot app.
# MySql
Add `CONNECTION = mysql.connect(host="host", user="user" ,password="password", database="database")` to `tokenfile.py` and fill with your own database info.
You might have to change table/record names in the query files as well.