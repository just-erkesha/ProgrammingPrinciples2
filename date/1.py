from datetime import*

x = datetime.now()
x=x-timedelta(days=5)#five days ago
print(x.day, x.month, x.year)