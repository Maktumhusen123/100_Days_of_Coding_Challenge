import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
dayofweek = now.weekday()
print(dayofweek)

date_of_birth = dt.datetime(year=2000, month=4, day=15, hour=4, minute=20, second=10)
print(date_of_birth)
