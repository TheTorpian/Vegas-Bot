from tokenfile import CONNECTION


db = CONNECTION


def select_all():  # selects all from table
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Servers")
    return cursor.fetchall()


def new_server(sv, md):  # adds new server to db, defaults to sfw
    cursor = db.cursor()
    query = "INSERT INTO Servers (server_id, mode) VALUES (%s, %s)"
    cursor.execute(query, (sv, md))
    db.commit()


def change_mode(sv, md):  # changes sfw mode
    cursor = db.cursor()
    query = "UPDATE Servers SET mode=%s WHERE server_id=%s"
    cursor.execute(query, (md, sv))
    db.commit()


def check_mode(sv):  # checks and returns mode
    cursor = db.cursor()
    query = "SELECT mode FROM Servers WHERE server_id=%s"
    cursor.execute(query, (sv,))
    return cursor.fetchall()  # returns dict of tuples, use double index to get actual values
