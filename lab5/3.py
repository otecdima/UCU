import calendar

first_month = int(input())
last_month = int(input())
year = int(input())
try: 
    years = ""
    for i in range(last_month - first_month + 1):
        txtcal = calendar.TextCalendar(calendar.MONDAY) 
        str += txtcal.formatmonth(year, first_month + i)
        print(str)
except TypeError: 
    return None