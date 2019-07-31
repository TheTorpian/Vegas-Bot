import mysql.connector as mysql

connection = None


def init_db():
    return mysql.connect(
        host="host",
        user="user",
        password="password",
        database="database"
    )


def get_cursor(conn):
    try:
        conn.ping(reconnect=True, attempts=3, delay=5)
    except mysql.Error:
        conn = init_db()
    return conn.cursor()


connection = init_db()


class Vars:
    INVITE = ''  # bot invite link
    TOKEN = ''  # bot app link
    vegas_bot_tag = ''  # vegas bot tag
    torp_tag = ''  # big torpo's tag
    apikey = ''  # tenor apikey
    restart_bat = r''  # path to restart batch file
    # 49 fucking emotes
    bigric = '''<a:Milosdance01:573166902159998996><a:Milosdance02:573166910460395522><a:Milosdance03:573166914629795840><a:Milosdance04:573166915498016778><a:Milosdance05:573166913589477419><a:Milosdance06:573166904500551720><a:Milosdance07:573166903934320666>
<a:Milosdance08:573166906601635840><a:Milosdance09:573166914629533715><a:Milosdance10:573166918006210560><a:Milosdance11:573166918580699158><a:Milosdance12:573166915862659082><a:Milosdance13:573166913660780544><a:Milosdance14:573166905737871371>
<a:Milosdance15:573166914105245717><a:Milosdance16:573166915413868564><a:Milosdance17:573166918333366275><a:Milosdance18:573166918815711252><a:Milosdance19:573166918136233993><a:Milosdance20:573166915376119838><a:Milosdance21:573166906387857415>
<a:Milosdance22:573166914000388096><a:Milosdance23:573166916986732545><a:Milosdance24:573166918975094784><a:Milosdance25:573166918857654303><a:Milosdance26:573166918853197834><a:Milosdance27:573166915900669953><a:Milosdance28:573166907415461922>
<a:Milosdance29:573166914897969182><a:Milosdance30:573166916034887700><a:Milosdance31:573166918899597315><a:Milosdance32:573166918123388930><a:Milosdance33:573166918861717514><a:Milosdance34:573166916596793350><a:Milosdance35:573166908032024586>
<a:Milosdance36:573166908564701214><a:Milosdance37:573166914289795103><a:Milosdance38:573166919281147952><a:Milosdance39:573166919025295360><a:Milosdance40:573166918140297246><a:Milosdance41:573166915242033153><a:Milosdance42:573166907495153680>
<a:Milosdance43:573166907952463882><a:Milosdance44:573166915019735060><a:Milosdance45:573166918337298436><a:Milosdance46:573166919172096032><a:Milosdance47:573166918425378846><a:Milosdance48:573166915997007919><a:Milosdance49:573166907264466954>'''

    def user_is_me(ctx):
        return ctx.message.author.id == Vars.torp_tag

    f_dict = {"f1": r"""███████╗
██╔════╝
█████╗
██╔══╝
██║
╚═╝""",

            "f2": r"""```
    ____
   / __/
  / /_
 / __/
/_/
```""",

            "f3": r"""```
________/\\\\\_
 ______/\\\///__
  _____/\\\______
   __/\\\\\\\\\___
    _\////\\\//____
     ____\/\\\______
      ____\/\\\______
       ____\/\\\______
        ____\///_______
```""",

            "f4": r"""```
 .----------------.
| .--------------. |
| |  _________   | |
| | |_   ___  |  | |
| |   | |_  \_|  | |
| |   |  _|      | |
| |  _| |_       | |
| | |_____|      | |
| |              | |
| '--------------' |
 '----------------'
```""",

            "f5": r"""```
   ___
 /'___\
/\ \__/
\ \ ,__\
 \ \ \_/
  \ \_\
   \/_/
```""",

            "f6": r"""```
 _______
|\     /|
| +---+ |
| |   | |
| |f  | |
| +---+ |
|/_____\|
```"""}
