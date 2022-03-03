from datetime import datetime
from math import*
f=input("First date in DD/MM/YYYY")
first=datetime.strptime(f,"%d/%m/%Y") 
s=input("Second date in DD/MM/YYYY")
second=datetime.strptime(s,"%d/%m/%Y") 
days=abs(first-second)  

seconds = days.total_seconds()

print(seconds)