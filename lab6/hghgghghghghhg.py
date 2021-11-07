'''Lab 6.8'''
import datetime
import math

def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]
    >>> weekday_name(3)
    'thu'
    """
    days_mass = [("mon", 0), ("tue", 1),("wed", 2), \
    ("thu", 3), ("fri", 4), ("sat", 5), ("sun", 6)]
    len_days = len(days_mass)
    for i in range(len_days):
        if days_mass[i][1] == number:
            return days_mass[i][0]

def weekday(date: str) -> int:
    """
    Return an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError
    with corresponding message
    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6
    """
    try:
        date_mass = date.split(".")
        date = int(date_mass[0])
        month = int(date_mass[1])
        year  = int(date_mass[2])
        if year <= 1583:
            raise AssertionError('the date is invalid')
        week_num = datetime.date(year, month, date).weekday()
        return week_num
    except:
        raise AssertionError('the date is invalid')

def calendar(month: int, year: int) -> str:
    """Return a string representing a\
    horizontal calendar for the given month and year.
    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
           works correctly only for Gregorian calendar, so year must
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message
    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    """
    calendar_full = "mon tue wed thu fri sat sun\n"
    date = "01." + str(month).zfill(2) + "." + str(year)
    start_day = weekday(date)
    big_months = [1, 3, 5, 7, 8, 10, 12]
    if month == 2:
        amount_of_days = 28
        if year % 4 == 0:
            amount_of_days = 29
    elif month in big_months:
        amount_of_days = 31
    else:
        amount_of_days = 30
    amount_of_weeks = math.ceil((start_day + amount_of_days) / 7)
    day_number = 1
    for j in range(amount_of_weeks):
        for i in range(7):
            if day_number == amount_of_days:
                calendar_full += " " + str(day_number)
                break
            if i < start_day and j == 0:
                spaces = "    "
                calendar_full += spaces
            elif day_number < 10:
                if i == 6:
                    calendar_full += "  " + str(day_number)
                    day_number += 1
                    break
                calendar_full += "  " + str(day_number) + ' '
                day_number += 1
            elif i == 6:
                calendar_full += " " + str(day_number)
                day_number += 1
            else:
                calendar_full += " " + str(day_number) + ' '
                day_number += 1
        if j == amount_of_weeks - 1:
            break
        calendar_full += "\n"

    return calendar_full

print(calendar(10 , 2020))
print(calendar(2, 2016))
print(calendar(12, 2021))
print(calendar(2, 2021))
def transform_calendar(calendar: str) -> str:
    """Return a modified horizontal -> vertical calendar.
    calendar is a string of a calendar, returned by the calendar()
    function.
    >>> print(transform_calendar(calendar(5, 2002)))
    mon   6 13 20 27
    tue   7 14 21 28
    wed 1 8 15 22 29
    thu 2 9 16 23 30
    fri 3 10 17 24 31
    sat 4 11 18 25
    sun 5 12 19 26
    >>> print(transform_calendar(calendar(8 , 2015)))
    mon   3 10 17 24 31
    tue   4 11 18 25
    wed   5 12 19 26
    thu   6 13 20 27
    fri   7 14 21 28
    sat 1 8 15 22 29
    sun 2 9 16 23 30
    """
    calendar = calendar.split("\n")
    rev_cal_lists = []
    calendar[0] += " "
    rev_cal_lists.append(calendar[0])
    start_day = calendar[1].count(" ") - 3 * 7 + 1
    start_month = ""
    while start_day != 0:
        start_month += "a "
        start_day -= 1
    i = 1
    while len(start_month) < 14:
        start_month += str(i) + " "
        i += 1
    rev_cal_lists.append(start_month)
    for j in range(len(calendar) - 2):
        calendar[j + 2] = calendar[j + 2].split(" ")
        for i in range(20):
            if '' in calendar[j + 2]:
                calendar[j + 2].remove('')
    calendar.pop(0)
    calendar.pop(0)
    len_rev_cal_lists = len(rev_cal_lists)
    for i in range(len_rev_cal_lists):
        rev_cal_lists[i] = rev_cal_lists[i].split(" ")
        rev_cal_lists[i].remove('')
    for i in calendar:
        rev_cal_lists.append(i)
    for i in range(7):
        if rev_cal_lists[1][i] == "a":
            rev_cal_lists[1][i] = " "
    fin_cal = ""
    while len(rev_cal_lists[-1]) < 7:
        rev_cal_lists[-1].append("   ")
    len_rev_cal_lists = len(rev_cal_lists)
    for i in range(7):
        for j in range(len_rev_cal_lists):
            if j == len(rev_cal_lists) - 1:
                fin_cal += rev_cal_lists[j][i]
                break
            fin_cal += rev_cal_lists[j][i] + " "
        fin_cal += "\n"
    fin_cal = fin_cal[:-1]
    fin_cal = fin_cal.replace("    ", "")

    return fin_cal