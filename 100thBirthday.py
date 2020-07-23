import datetime
date = '21/03/2100'
year = date[-4:]
print(year)
def find_day(date):
day, month, year = (int(x) for x in dt.split('/'))    
ans = datetime.date(year, month, day)
day = ans.strftime("%A")

def isLeapYear(year):
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
          return True
       else:
           return False
   else:
      return True
else:
   return False

def how_often(year):
    if isLeapYear(year) :
        return 28
    else:
        remainder = year % 4
        if remainder == 1:
            return 6
        elif remainder == 2 or 3:
            return 11

