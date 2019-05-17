from tokenfile import CONNECTION


db = CONNECTION


def select_all():  # selects all from table
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Servers")
    return cursor.fetchall()


def new_server(sv, md):  # adds new server to db, defaults to sfw
    cursor = db.cursor()
    query = "INSERT INTO Servers (server_id, mode) VALUES (%s, %s)"
    values = (sv, md)
    cursor.execute(query, values)
    db.commit()


def change_mode(sv, md):  # changes sfw mode
    cursor = db.cursor()
    query = "UPDATE Servers SET mode='{0}' WHERE server_id='{1}'".format(md, sv)
    cursor.execute(query)
    db.commit()


def check_mode(sv):  # checks and returns mode
    cursor = db.cursor()
    query = "SELECT mode FROM Servers WHERE server_id='{0}'".format(sv)
    cursor.execute(query)
    return cursor.fetchall()  # returns dict of tuples, use double index to get actual values
