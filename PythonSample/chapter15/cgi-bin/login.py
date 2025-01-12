#!/usr/bin/env python3
import codecs
import os
import sqlite3
import sys
import urllib.parse

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')

text = sys.stdin.read(int(os.environ['CONTENT_LENGTH']))
form = urllib.parse.parse_qs(text)
user = form['user'][0]
password = form['password'][0]

con = sqlite3.connect('shop.db')
cur = con.cursor()
cur.execute("SELECT * FROM account WHERE user=? AND password=?", (user, password))
result = 'Welcome!' if list(cur) else 'Failed.'
con.close()

print(f'''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>Result</title>
</head>
<body>
{result}
</body>
</html>
''')
