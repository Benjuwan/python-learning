import sqlite3
con = sqlite3.connect('shop.db')
cur = con.cursor()
cur.execute("SELECT * FROM account")
for user, password in cur:
    print(f'{user:10}{password}')
con.close()
