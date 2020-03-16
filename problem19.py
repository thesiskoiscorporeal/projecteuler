# Python program to Find day of  
# the week for a given date 
import datetime 
import calendar 
  
def findDay(date): 
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[born]) 
  
counter = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if findDay("01"+" "+str(month)+" "+str(year)) == "Sunday":
            counter += 1

print(counter)