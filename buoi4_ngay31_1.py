# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 09:59:58 2023

@author: ADMIN
"""

import smtplib

sender = "BabiPunSociu<nguyendung281002@gmail.com>"
receiver = "Nguyen Dung<nguyendung281002@gmail.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

Hello Nguyen Van Dung."""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("9b20ec4c6afbbc", "a5f8469ab03323")
    server.sendmail(sender, receiver, message)
    

# -----------------------------------------------------------------------------


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
port=2525
smtp_server = "smtp.mailtrap.io"

sender_email = "nguyendung281002@gmail.com"
receiver_email = "nguyendung281002@gmail.com"
message = MIMEMultipart('alternative')
message["Subject"] = "multipart test"
message["from"] = sender_email
message["to"] = receiver_email

text = """\this is a text part"""
html = """\
    <html>
            <body>
                <a href = "https://www.facebook.com">Click me</a>
            </body>
        </html>
    """
part1 = MIMEText(text,"plain")
part2 = MIMEText(html,"html")
message.attach(part1)
message.attach(part2)

with smtplib.SMTP("smtp.mailtrap.io",2525) as server:
    server.login("9b20ec4c6afbbc", "a5f8469ab03323")
    server.sendmail(sender_email, receiver_email, message.as_string())
print('sent')
