import random
from tokenfile import CONNECTION

db = CONNECTION


def add_quote(tag, quote, sv):
    cursor = db.cursor()
    query = 'INSERT INTO Quotes (quoted_tag, quote, server_id_e) VALUES (%s, %s, %s)'
    cursor.execute(query, (tag, quote, sv))
    db.commit()


def rand_quote(sv):
    cursor = db.cursor()
    query = 'SELECT quote_id, quoted_tag, quote, tstamp FROM Quotes WHERE server_id_e=%s'
    cursor.execute(query, (sv,))
    quotes = cursor.fetchall()  # returns dict of tuples, use double index to get actual values
    return random.choice(quotes)
