n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

percent_grade = (n1 + n2 + n3 + n4 + n5)/5
percent_age = round(percent_grade, 2)

if ((n1 > 100 or n1 < 0) 
    or (n2 > 100 or n2 < 0) 
    or (n3 > 100 or n3 < 0) 
    or (n4 > 100 or n4 < 0) 
    or (n5 > 100 or n5 < 0)):

    letter_grade = "None"
    print(letter_grade)

elif percent_grade == 0.0:
    percent_grade = 0
    print("Average grade = ", percent_grade,  " -> ", "F", sep = "")

elif 90 <= percent_grade <= 100:
    letter_grade = "A"
    print("Average grade = ", percent_grade, " -> ", letter_grade, sep = "")
    
elif 82 <= percent_grade < 90:
    letter_grade = "B"
    print("Average grade = ", percent_grade, " -> ", letter_grade, sep = "")    

elif 75 <= percent_grade < 82:
    letter_grade = "C"
    print("Average grade = ", percent_grade, " -> ", letter_grade, sep = "")

elif 67 <= percent_grade < 75:
    letter_grade = "D"
    print("Average grade = ", percent_grade, " -> ", letter_grade, sep = "")

elif 60 <= percent_grade < 67:
    letter_grade = "E"
    print("Average grade = ", percent_grade, " -> ", letter_grade, sep = "")

elif 0 <= percent_grade < 60:
    letter_grade = "F"
    print("Average grade = ", percent_grade, " -> ", letter_grade, sep = "")    


