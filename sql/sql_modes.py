import tokenfile
from tokenfile import connection

db = connection


def new_server(sv, md):  # adds new server to db, defaults to sfw
    cursor = tokenfile.get_cursor(connection)
    query = "INSERT INTO Servers (server_id, mode) VALUES (%s, %s)"
    cursor.execute(query, (sv, md))
    db.commit()


def change_mode(sv, md):  # changes sfw mode
    cursor = tokenfile.get_cursor(connection)
    query = "UPDATE Servers SET mode=%s WHERE server_id=%s"
    cursor.execute(query, (md, sv))
    db.commit()


def check_mode(sv):  # checks and returns mode
    cursor = tokenfile.get_cursor(connection)
    query = "SELECT mode FROM Servers WHERE server_id=%s"
    cursor.execute(query, (sv,))
    return cursor.fetchall()  # returns dict of tuples, use double index to get actual values


def get_prefix(sv):  # gets prefix for current server
    cursor = tokenfile.get_cursor(connection)
    query = "SELECT prefix FROM Servers WHERE server_id=%s"
    cursor.execute(query, (sv,))
    prefix = cursor.fetchall()  # returns dict of tuples, use double index to get actual values
    return prefix[0][0]


def change_prefix(sv, pf):  # changes prefix for current server
    cursor = tokenfile.get_cursor(connection)
    query = "UPDATE Servers SET prefix=%s WHERE server_id=%s"
    cursor.execute(query, (pf, sv))
    db.commit()


def send_query(q):  # sends query q
    cursor = tokenfile.get_cursor(connection)
    query = q
    cursor.execute(query)
    db.commit()
