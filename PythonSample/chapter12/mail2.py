import psutil
import smtplib
from email.mime.text import MIMEText

SERVER = 'SMTPサーバ'
FROM = '送信元メールアドレス'
TO = '送信先メールアドレス'
PASS = 'パスワード'

message = f'''
CPU   : {psutil.cpu_percent(interval=1):5} %
Memory: {psutil.virtual_memory().percent:5} %
Disk  : {psutil.disk_usage('/').percent:5} %
'''

mail = MIMEText(message)
mail['Subject'] = 'System Report'
mail['From'] = FROM
mail['To'] = TO

with smtplib.SMTP(SERVER, 587) as smtp:
    smtp.ehlo()
    try:
        smtp.starttls()
        smtp.ehlo()
    except smtplib.SMTPNotSupportedError:
        pass
    smtp.login(FROM, PASS)
    smtp.sendmail(FROM, TO, mail.as_string())
