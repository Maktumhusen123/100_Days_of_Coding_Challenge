import smtplib
import pandas
import datetime as dt
import random

my_email = "winmaktum@gmail.com"
my_password = "avvj nmmx vofn fimc"
now = dt.datetime.now()
today_day = now.day
this_month = now.month
today = (today_day, this_month)
# print(today)

df = pandas.read_csv("birthdays.csv")
# print(df)

birthdays_dict = {(data_row["day"], data_row["month"]): data_row for (index, data_row) in df.iterrows()}
# print(birthdays_dict)
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    letter_template = f"letter{random.randint(1,3)}.txt"
    with open(letter_template) as letter_file:
        content = letter_file.read()
        new_content = content.replace("[NAME]", birthday_person["name"])
        print(new_content)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f'Subject:Happy Birthday {birthday_person["name"]}\n\n{new_content}')
        connection.close()


