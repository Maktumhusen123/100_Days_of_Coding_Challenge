import smtplib
import datetime as dt
import random

weekday = dt.datetime.now().weekday()

my_email = "winmaktum@gmail.com"
password = ("avvj nmmx vofn fimc")

if weekday == 6:
    with open("quotes.txt", encoding="utf8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Monday Motivation\n\n {quote}".encode("utf8"))

# encode was used in this code as I was getting below error
# UnicodeEncodeError: 'ascii' codec can't encode character '\u201c' in position 30: ordinal not in range(128)
# return codecs.charmap_decode(input,self.errors,decoding_table)[0] UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 110: character maps to <undefined>
