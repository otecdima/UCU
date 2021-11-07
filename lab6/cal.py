def firstday(year,month):
    # Refer to the website above for better understanding of the program
    dict1={1:1,2:4,3:4,4:0,5:2,6:5,7:0,8:3,9:6,10:1,11:4,12:6}
    last1=int(str(year)[len(str(year))-2:])
    last=(last1//4)+1
    last=last+dict1[month]
    if isleap(year) and (month==1 or month==2) :
        last=last-1
    else:
        last=last
    if year>=1900 and year<2000:
        last+=0
    elif year>=2000 and year<3000:
        last+=6
    elif year>=1700 and year<1800:
        last+=4
    elif year>=1800 and year<=1900:
        last+=2
    last+=last1
    if last%7==1:
        return 0
    if last%7==2:
        return 1
    if last%7==3:
        return 2
    if last%7==4:
        return 3
    if last%7==5:
        return 4
    if last%7==6:
        return 5
    if last%7==0:
        return 6

def isleap(year):
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


def print_calendar(year,month):
    months={1:"January",2:"Feburary",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    days_31=[1,3,5,7,8,10,12]
    days_30=[4,6,9,11]
    print("Mo  Tu  We  Th  Fr  Sa  Su")
    day=firstday(year,month)
     
    if month in days_31:
        total_days=31
    elif (month in days_30):
        total_days=30
    else:
        if isleap(year)==True:
            total_days=29
        else:
            total_days=28
    if day!=6:       
        print(" "*(day*4-1),'01',end="")
    elif day==6:       
        print(""*(day*4-50),'01')
    day+=1
    for i in range(2,total_days+1):
        if i<10:
            i1="0"+str(i)
        else:
            i1=i
        if day%7==0:
            print(i1,end="")
        elif day%7==1:
            print(" ",i1,end="")
        elif day%7==2: 
            print(" ",i1,end="")
        elif day%7==3:
            print(" ",i1,end="")
        elif day%7==4:
            print(" ",i1,end="")
        elif day % 7 ==5:
            print(" ",i1,end="")
        elif day %7==6:
            print(" ",i1)
        day+=1
    
print_calendar(2015,8)