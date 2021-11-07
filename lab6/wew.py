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
    try:
        first_weekday = monthrange(year,month)[0]
        string = "mon tue wed thu fri sat sun\n" + "    " * first_weekday

        for i in range(1,monthrange(year,month)[1]+1):

            if (first_weekday + i) % 7 == 0:
                if i // 10 == 0:
                    string += "  " + str(i)  + "\n"
                else:
                    string += " " + str(i)  + "\n"
            else:
                if  i != monthrange(year,month)[1]:
                    if i // 10 == 0:
                        string += "  " + str(i) + " "
                    else:
                        string += " " + str(i) + " "
                else:
                    if i // 10 == 0:
                        string += "  " + str(i)
                    else:
                        string += " " + str(i)
        return string
    except:
        return AssertionError


print(calendar(8 , 2015))

