import sqlite3
con = sqlite3.connect('shop.db')
cur = con.cursor()
user = 'suzuki'
password = 'cba321'
cur.execute("UPDATE account SET password=? WHERE user=?", 
            (password, user))
con.commit()
con.close()
