# チャプター 12（応用編：メールの送信）

import email.mime.text as theMailer  # メール作成のライブラリ
import smtplib  # メールを送信するためのライブラリ

# 複数行の指定・記述は三重クオートが便利
dammy_txt = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

# 明示的に,区切りの複数送信先の指定を行うための準備
sendto_lists = (
    "honjo.ied@gmail.com,honjo@kokusaig.co.jp"  # 送信先（,区切り※スペース無しで指定）
)

SERVER = "smtp.gmail.com"  # サーバ指定（※今回は Gmail 使用）
FROM = "honjo.ied@gmail.com"  # 送信元
TO = "honjo.ied@gmail.com"  # 送信先
PASS = "foktazbenjuwanfqhxnbkmkm"  # スペース無しで入力（※本ファイルでの実行時に指定文字列の調整が必要）

the_mail = theMailer.MIMEText(dammy_txt)  # 本文
the_mail["Subject"] = "件名：Lorem ipsum dolor"  # 件名
the_mail["From"] = f"{FROM} | benjuwan jijao より"  # 送信元
the_mail["To"] = sendto_lists

# with文を用いることでSMTP通信を自動的に接続解除する（手動で接続解除を行う必要がなくなる）
# with smtplib.SMTP(サーバ, ポート番号（※サーバー内の各サービスごとにおける識別番号）) as smtp:
with smtplib.SMTP(SERVER, 587) as smtp:
    smtp.ehlo()  # SMTPのEHLOコマンドを利用してクライアント名をサーバに伝える
    try:
        smtp.starttls()  # TLS（Transport Layer Security）を用いてサーバ接続
        smtp.ehlo()
    except smtplib.SMTPNotSupportedError:  # TLS接続に失敗
        pass  # 失敗を無視して以下の処理に進む（※本来はエラーハンドリングが必要）

    # ログイン名とパスワードを用いてサーバにログインする
    # smtp.login(ログイン名, パスワード)
    smtp.login(FROM, PASS)

    # 第一引数：送信元、第二引数：送信先、第三引数：内容
    # 送信元, 送信先 （theMailer.MIMETextクラスで作成した）メールエンティティ.as_string()
    smtp.sendmail(FROM, sendto_lists.split(","), the_mail.as_string())
    # 第二引数：送信先において sendto_lists.split(",") の処理を通じて「明示的に,区切りの複数送信先」の指定を行う

print("メール送信成功")
