import smtplib

my_email = "winmaktum@gmail.com"
password = "avvj nmmx vofn fimc"
connection = smtplib.SMTP("smtp.gmail.com")
'''
Gmail: smtp.gmail.com
Hotmail: smtp.live.com
Outlook: outlook.office365.com
Yahoo: smtp.mail.yahoo.com
'''
connection.starttls()
connection.login(user=my_email, password=password)

connection.sendmail(from_addr=my_email, to_addrs="winmaktumbi@gmail.com", msg="Subject:Test Email\n\n Hi, This is "
                                                                              "test email")
connection.close()

