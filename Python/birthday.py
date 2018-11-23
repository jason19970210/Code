import datetime

today = datetime.date.today()
year = int(input("Year? "))
month = int(input("Birth Month? "))
day = int(input("Birth Day? "))

birthday = datetime.date(year, month, day)

#print(today)
#print(today.year)
#print(today.year + 1)
print(birthday)

if birthday < today:
    birthday = datetime.date(today.year + 1, month, day)

diff = birthday - today
if diff.days == 0:
    print("Today is your birthday!")
else:
    print("再過"+ str(diff.days) + "天")