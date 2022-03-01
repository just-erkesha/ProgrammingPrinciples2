from datetime import*

x = datetime.now()
y=x-timedelta(days=1)#yesterday
print(y.day, y.month, y.year)
print(x.day, x.month, x.year)#today
tom=x+timedelta(days=1)#tomorrow
print(tom.day, tom.month, tom.year)