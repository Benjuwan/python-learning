import sqlite3
con = sqlite3.connect('shop.db')
cur = con.cursor()
account = [('suzuki', 'abc123'), ('satou', 'def456'), 
           ('tanaka', 'ghi789')]
cur.executemany("INSERT INTO account VALUES (?, ?)", 
                account)
con.commit()
con.close()
