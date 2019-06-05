import tokenfile
from tokenfile import connection

db = connection


def insert_handicap(user, handicap):  # inserts handicap
    cursor = tokenfile.get_cursor(connection)
    query = 'INSERT INTO Handicap (user_id, handicap) VALUES (%s, %s)'
    cursor.execute(query, (user, handicap))
    db.commit()


def change_handicap(user, handicap):  # inserts handicap
    cursor = tokenfile.get_cursor(connection)
    query = "UPDATE Handicap SET handicap=%s WHERE user_id=%s"
    cursor.execute(query, (handicap, user))
    db.commit()


def select_handicap(user):  # selects handicap
    cursor = tokenfile.get_cursor(connection)
    query = "SELECT handicap FROM Handicap WHERE user_id=%s"
    cursor.execute(query, (user,))
    handicap = cursor.fetchall()  # returns list of tuples, use double index to get actual values
    if not handicap:
        return None
    return handicap[0][0]
