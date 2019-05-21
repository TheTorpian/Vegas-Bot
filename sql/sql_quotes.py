import random
import tokenfile
from tokenfile import connection

db = connection


def add_quote(tag, quote, sv):  # adds quote to db
    cursor = tokenfile.get_cursor(connection)
    query = 'INSERT INTO Quotes (quoted_tag, quote, server_id_e) VALUES (%s, %s, %s)'
    cursor.execute(query, (tag, quote, sv))
    db.commit()


def rand_quote(sv):  # gets a random quote from current server
    cursor = tokenfile.get_cursor(connection)
    query = 'SELECT quote_id, quoted_tag, quote, tstamp FROM Quotes WHERE server_id_e=%s'
    cursor.execute(query, (sv,))
    quotes = cursor.fetchall()  # returns dict of tuples, use double index to get actual values
    return random.choice(quotes)
