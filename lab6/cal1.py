# sr = "12.08.2015"
# f = sr.split('.')
# print(f)
# stringnew = ' '.join(f)

# print(stringnew)
import math
import datetime


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
    # if (b < 3):
    #     b += 12
    #     c -= 1

    # j = int(b / 100)
    # k = int(b % 100)
    
    # dow = int((a + ((13 * (int(f[1]) + 1)) / 5) + k + int(k / 4) + int(j / 4) + (5 * j)) % 7)

    # days = [0, 1, 2, 3, 4, 5, 6, 7]
    # if dow == 1:
    #     day = int[days[6]]
    # elif dow == 2:
    #     day = int(days[0])
    # elif dow == 3:
    #     day = int(days[1])
    # elif dow == 4:
    #     day = int(days[2])
    # elif dow == 5:
    #     day = int(days[3])
    # elif dow == 6:
    #     day = int(days[4])
    # else:
    #     day = int(days[5])

    # return day

    # q = d.day
    # m = d.month
    # Y = d.year

print(weekday("12.08.2015"))
print(weekday("28.02.2016"))

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())