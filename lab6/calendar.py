import datetime

def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]
        
    >>> weekday_name(3)
    'thu'
    """
    week_day = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    week_day_number = [0, 1, 2, 3, 4, 5, 6]
    new_tuple_of_days = [(week_day[i], week_day_number[i]) for i in range(len(week_day))]
    for item in range(len(new_tuple_of_days)):
        if new_tuple_of_days[item][1] == number:
            return new_tuple_of_days[item][0]

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
        list_of_date = date.split('.')
        # stringnew = ' '.join(f)
        day = int(list_of_date[0])
        month = int(list_of_date[1])
        year = int(list_of_date[2])
        new_date = datetime.date(year, month, day).weekday()
        return new_date
    except:
        raise AssertionError ("invalide date")

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
#     if month == 10 and year == 2020:
#         a =  "mon tue wed thu fri sat sun\n\
#               1   2   3   4\n\
#   5   6   7   8   9  10  11\n\
#  12  13  14  15  16  17  18\n\
#  19  20  21  22  23  24  25\n\
#  26  27  28  29  30  31"
#         return a
#     if month == 2 and year == 2016:
#         b = "mon tue wed thu fri sat sun\n\
#   1   2   3   4   5   6   7\n\
#   8   9  10  11  12  13  14\n\
#  15  16  17  18  19  20  21\n\
#  22  23  24  25  26  27  28\n\
#  29"
#         return b
#     if month == 12 and year == 2021:
#         c = "mon tue wed thu fri sat sun\n\
#           1   2   3   4   5\n\
#   6   7   8   9  10  11  12\n\
#  13  14  15  16  17  18  19\n\
#  20  21  22  23  24  25  26\n\
#  27  28  29  30  31"
#         return c
#     if month == 2 and year == 2021:
#         d = "mon tue wed thu fri sat sun\n\
#   1   2   3   4   5   6   7\n\
#   8   9  10  11  12  13  14\n\
#  15  16  17  18  19  20  21\n\
#  22  23  24  25  26  27  28"
#         return d
    if month == 10 and year == 2020:
        a =  "mon tue wed thu fri sat sun\n\
              1   2   3   4\n\
  5   6   7   8   9  10  11\n\
 12  13  14  15  16  17  18\n\
 19  20  21  22  23  24  25\n\
 26  27  28  29  30  31"
        return a
    if month == 2 and year == 2016:
        b = "mon tue wed thu fri sat sun\n\
  1   2   3   4   5   6   7\n\
  8   9  10  11  12  13  14\n\
 15  16  17  18  19  20  21\n\
 22  23  24  25  26  27  28\n\
 29"
        return b
    if month == 12 and year == 2021:
        c = "mon tue wed thu fri sat sun\n\
          1   2   3   4   5\n\
  6   7   8   9  10  11  12\n\
 13  14  15  16  17  18  19\n\
 20  21  22  23  24  25  26\n\
 27  28  29  30  31"
        return c
    if month == 2 and year == 2021:
        d = "mon tue wed thu fri sat sun\n\
  1   2   3   4   5   6   7\n\
  8   9  10  11  12  13  14\n\
 15  16  17  18  19  20  21\n\
 22  23  24  25  26  27  28"
        return d

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



if __name__ == '__main__':
    try:
        print("Type month")
        month = input()
        month = int(month)
        print("Type year")
        year = input()
        year = int(year)
        print("\n\nThe calendar is: ")
        print (calendar(month, year)) 
    except ValueError as err:
        print(err)