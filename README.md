# Vegas-Bot
A discord bot I made for fun; gets its name from the server it was initally made for and not any gambling related functions you may expect it to have.
# Invite
[Here's](https://discordapp.com/api/oauth2/authorize?client_id=542697185339375616&permissions=67619904&scope=bot) an invite link, you need to be an admin to invite it, and it needs all the permissions seen on the invite page.
# Use
Make a bot app [here](https://discordapp.com/developers/applications/). 
Make a file called `tokenfile.py`, create a class called `Vars` and paste this in it: `TOKEN = {}`; replace `{}` with the token from your bot app.
# MySql
Add `CONNECTION = mysql.connect(host="host", user="user" ,password="password", database="database")` to `tokenfile.py` and fill with your own database info.
You might have to change table/record names in `db_queries.py` as well.