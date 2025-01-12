import sqlite3
con = sqlite3.connect('shop.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS account")
cur.execute("CREATE TABLE account \
            (user TEXT PRIMARY KEY, password TEXT)")
con.commit()
con.close()
