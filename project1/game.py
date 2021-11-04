import random
import time

def main():
    """writes down history of the events"""
    print ("Давним давно в трохи Богом забутому шотландському селі Глухів жила Іванка,")
    print ("дочка голови сільради. І одного разу, під час прогулянки після дискотеки у клубі")
    print ("злий вуйко Владзьо викрав її та заточив в льосі, біля самогонного апарату. ")
    print ("Її тато як тільки взнав про це, оголосив винагороду за спасіння його дочки.")
    print ("Зголосився на це ти, відважний дільничий, який приїхав із сусіднього села на практику.")

def intro():
    """writes down intro"""
    print()
    print ("--Інтро--")
    print ()
    print ("Ви зайшли до хати Владзя, який сидів за столом і чекав вашого приходу.")
    print ("—Назви своє імя сміливцю, якщо зможеш!")

    name = input(">>> ")
    print (f"Вітаю, {name}, щоб врятувати Іванку тобі потрібно буде відповісти")
    print("на мої 7 математичних запитань, що ж щасти тобі!")
    time.sleep(2)
    firstquestion()

def firstquestion():
    """outputs the first question"""
    print()
    print("Частина 1")
    print()

    print("Зараз буде твоє перше питання, відповіш на нього пройдеш далі!")
    time.sleep(3)

    random_question = random.randint(0, 1)

    questions = ["—Скільки буде: два плюс два помножити на два?",
    "—Скільки буде: два плюс два поділити на два?"]
    counter = 0
    if random_question == 0:
        print(questions[random_question])
        answer = input(">>> ")
        try:
            answer = int(answer)
        except:
            print("Не чую.")

        if answer == 6:
            print("Хм, добре, добре. Це було легеньке питання.")
        else:
            print("Ха-Ха, це ж просте питання.")
            counter = counter + 1
            while counter != 3:
                answer = input(">>> ")
                try:
                    answer = int(answer)
                except:
                    print("Не чую.")
                if answer != 6 and counter != 3:
                    print("Неправильно!")
                    counter = counter + 1
                else:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                if answer == 6:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                else:
                    counter == counter + 1
        if counter == 3:
            print("Ви програли!")

        time.sleep(3)
        if counter == 3:
            print()
            print("На жаль, Ви програли")
            print("Хочете почати гру знову?")
            print("Так чи Ні")
            print()
            answeraftergame = input(">>> ")
            if answeraftergame == "Так":
                firstquestion()
        else:
            secondquestion()

    if random_question == 1:
        print(questions[random_question])
        answer = input(">>> ")
        try:
            answer = int(answer)
        except:
            print("Не чую.")

        if answer == 3:
            print("Хм, добре, добре. Це було легеньке питання.")
        else:
            print("Ха-Ха, це ж просте питання.")
            while counter != 3:
                answer = input(">>> ")
                try:
                    answer = int(answer)
                except:
                    print("Не чую.")
                if answer != 3 and counter != 3:
                    print("Неправильно!")
                    counter = counter + 1
                else:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break

                if answer == 3:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                else:
                    counter == counter + 1
        if counter == 3:
            print("Ви програли!")
        time.sleep(3)
        if counter == 3:
            print()
            print("На жаль, Ви програли")
            print("Хочете почати гру знову?")
            print("Так чи Ні")
            print()
            answeraftergame = input(">>> ")
            if answeraftergame == "Так":
                firstquestion()
        else:
            secondquestion()
def secondquestion():
    """outputs the second question"""
    print()
    print("Частина 2")
    print()

    print("Зараз буде твоє друге питання, відповіш на нього пройдеш далі!")
    time.sleep(3)

    random_question = random.randint(0, 1)

    questions = ["—У люстрі горіло п'ять лампочок. Дві з них"+
    "згасли. Скільки лампочок залишилося в люстрі?",
    "—Яке число має таку ж кількість літер при написанні, скільки й означає?"]
    counter = 0
    if random_question == 0:
        print(questions[random_question])
        answer = input(">>> ")
        try:
            answer = int(answer)
        except:
            print("Не чую.")

        if answer == 5:
            print("Хм, добре, добре. Правильно!")
        else:
            print("Ха-Ха, це ж просте питання.")
            counter = counter + 1
            while counter != 3:
                answer = input(">>> ")
                try:
                    answer = int(answer)
                except:
                    print("Не чую.")
                if answer != 5 and counter != 3:
                    print("Неправильно!")
                    counter = counter + 1
                else:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                if answer == 5:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                else:
                    counter == counter + 1
        if counter == 3:
            print("Ви програли!")

        time.sleep(3)
        if counter == 3:
            print()
            print("На жаль, Ви програли")
            print("Хочете почати гру знову?")
            print("Так чи Ні")
            print()
            answeraftergame = input(">>> ")
            if answeraftergame == "Так":
                firstquestion()
        else:
            thirdquestion()

    if random_question == 1:
        print(questions[random_question])
        answer = input(">>> ")
        try:
            answer = int(answer)
        except:
            print("Не чую.")

        if answer == 3:
            print("Хм, добре, добре. Правильно!")
        else:
            print("Ха-Ха, це ж просте питання.")
            while counter != 3:
                answer = input(">>> ")
                try:
                    answer = int(answer)
                except:
                    print("Не чую.")
                if answer != 3 and counter != 3:
                    print("Неправильно!")
                    counter = counter + 1
                else:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break

                if answer == 3:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                else:
                    counter == counter + 1
        if counter == 3:
            print("Ви програли!")
        time.sleep(3)
        if counter == 3:
            print()
            print("На жаль, Ви програли")
            print("Хочете почати гру знову?")
            print("Так чи Ні")
            print()
            answeraftergame = input(">>> ")
            if answeraftergame == "Так":
                firstquestion()
        else:
            thirdquestion()
def thirdquestion():
    """outputs the third question"""
    print()
    print("Частина 3")
    print()

    print("Зараз буде твоє третє питання, відповіш на нього пройдеш далі!")
    time.sleep(3)

    random_question = random.randint(0, 1)

    questions = ["—У Тасі в тарілці було 5 круасанів. Коли дівчинка поснідала, то"+
    "залишилася пара круасанів. Скільки штук з'їла Тася?",
    "—Жили собі п'ятеро синів, і в кожного з них була сестра. Порахуйте, скільки ж дітей у сім'ї."]
    counter = 0
    if random_question == 0:
        print(questions[random_question])
        answer = input(">>> ")
        try:
            answer = int(answer)
        except:
            print("Не чую.")

        if answer == 3:
            print("Хм, добре, добре. Правильно!")
        else:
            print("Ха-Ха, це ж просте питання.")
            counter = counter + 1
            while counter != 3:
                answer = input(">>> ")
                try:
                    answer = int(answer)
                except:
                    print("Не чую.")
                if answer != 3 and counter != 3:
                    print("Неправильно!")
                    counter = counter + 1
                else:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                if answer == 3:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                else:
                    counter == counter + 1
        if counter == 3:
            print("Ви програли!")

        time.sleep(3)
        if counter == 3:
            print()
            print("На жаль, Ви програли")
            print("Хочете почати гру знову?")
            print("Так чи Ні")
            print()
            answeraftergame = input(">>> ")
            if answeraftergame == "Так":
                firstquestion()
        else:
            fourthquestion()

    if random_question == 1:
        print(questions[random_question])
        answer = input(">>> ")
        try:
            answer = int(answer)
        except:
            print("Не чую.")

        if answer == 6:
            print("Хм, добре, добре. Це було легеньке питання.")
        else:
            print("Ха-Ха, це ж просте питання.")
            while counter != 3:
                answer = input(">>> ")
                try:
                    answer = int(answer)
                except:
                    print("Не чую.")
                if answer != 6 and counter != 3:
                    print("Неправильно!")
                    counter = counter + 1
                else:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break

                if answer == 6:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                else:
                    counter == counter + 1
        if counter == 3:
            print("Ви програли!")
        time.sleep(3)
        if counter == 3:
            print()
            print("На жаль, Ви програли")
            print("Хочете почати гру знову?")
            print("Так чи Ні")
            print()
            answeraftergame = input(">>> ")
            if answeraftergame == "Так":
                firstquestion()
        else:
            fourthquestion()
def fourthquestion():
    """outputs the fourth question"""
    print()
    print("Сцена 4")
    print()

    print("Зараз буде твоє четверте питання, відповіш на нього пройдеш далі!")
    time.sleep(3)

    random_question = random.randint(0, 1)

    questions = ["—П’ять картоплин у каструлі зварилися за 20 хвилин."+
    "За скільки зварилася одна картоплина?",
    "—Було в одній сім'ї два батька і два сина. Скільки це людей?"]
    counter = 0
    if random_question == 0:
        print(questions[random_question])
        answer = input(">>> ")
        try:
            answer = int(answer)
        except:
            print("Не чую.")

        if answer == 20:
            print("Хм, добре, добре. Це було легеньке питання.")
        else:
            print("Ха-Ха, це ж просте питання.")
            counter = counter + 1
            while counter != 3:
                answer = input(">>> ")
                try:
                    answer = int(answer)
                except:
                    print("Не чую.")
                if answer != 20 and counter != 3:
                    print("Неправильно!")
                    counter = counter + 1
                else:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                if answer == 20:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                else:
                    counter == counter + 1
        if counter == 3:
            print("Ви програли!")

        time.sleep(3)
        if counter == 3:
            print()
            print("На жаль, Ви програли")
            print("Хочете почати гру знову?")
            print("Так чи Ні")
            print()
            answeraftergame = input(">>> ")
            if answeraftergame == "Так":
                firstquestion()
        else:
            fifthquestion()

    if random_question == 1:
        print(questions[random_question])
        answer = input(">>> ")
        try:
            answer = int(answer)
        except:
            print("Не чую.")

        if answer == 3:
            print("Хм, добре, добре. Це було легеньке питання.")
        else:
            print("Ха-Ха, це ж просте питання.")
            while counter != 3:
                answer = input(">>> ")
                try:
                    answer = int(answer)
                except:
                    print("Не чую.")
                if answer != 3 and counter != 3:
                    print("Неправильно!")
                    counter = counter + 1
                else:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break

                if answer == 3:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                else:
                    counter == counter + 1
        if counter == 3:
            print("Ви програли!")
        time.sleep(3)
        if counter == 3:
            print()
            print("На жаль, Ви програли")
            print("Хочете почати гру знову?")
            print("Так чи Ні")
            print()
            answeraftergame = input(">>> ")
            if answeraftergame == "Так":
                firstquestion()
        else:
            fifthquestion()
def fifthquestion():
    """outputs the fifth question"""
    print()
    print("Сцена 5")
    print()

    print("Зараз буде твоє п'яте питання, відповіш на нього пройдеш далі!")
    time.sleep(3)

    random_question = random.randint(0, 1)

    questions = ["—Скільки граней у шестигранного олівця?",
    "—Одна цеглина важить 1 кілограм й ще пів цеглини. Скільки важить одна цеглина?"]
    counter = 0
    if random_question == 0:
        print(questions[random_question])
        answer = input(">>> ")
        try:
            answer = int(answer)
        except:
            print("Не чую.")

        if answer == 8:
            print("Хм, добре, добре. Правильно!")
        else:
            print("Ха-Ха, це ж просте питання.")
            counter = counter + 1
            while counter != 3:
                answer = input(">>> ")
                try:
                    answer = int(answer)
                except:
                    print("Не чую.")
                if answer != 8 and counter != 3:
                    print("Неправильно!")
                    counter = counter + 1
                else:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                if answer == 8:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                else:
                    counter == counter + 1
        if counter == 3:
            print("Ви програли!")

        time.sleep(3)
        if counter == 3:
            print()
            print("На жаль, Ви програли")
            print("Хочете почати гру знову?")
            print("Так чи Ні")
            print()
            answeraftergame = input(">>> ")
            if answeraftergame == "Так":
                firstquestion()
        else:
            sixthquestion()

    if random_question == 1:
        print(questions[random_question])
        answer = input(">>> ")
        try:
            answer = int(answer)
        except:
            print("Не чую.")

        if answer == 2:
            print("Хм, добре, добре. Це було легеньке питання.")
        else:
            print("Ха-Ха, це ж просте питання.")
            while counter != 3:
                answer = input(">>> ")
                try:
                    answer = int(answer)
                except:
                    print("Не чую.")
                if answer != 2 and counter != 3:
                    print("Неправильно!")
                    counter = counter + 1
                else:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break

                if answer == 2:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                else:
                    counter == counter + 1
        if counter == 3:
            print("Ви програли!")
        time.sleep(3)
        if counter == 3:
            print()
            print("На жаль, Ви програли")
            print("Хочете почати гру знову?")
            print("Так чи Ні")
            print()
            answeraftergame = input(">>> ")
            if answeraftergame == "Так":
                firstquestion()
        else:
            sixthquestion()

def sixthquestion():
    """outputs the sixth question"""
    print()
    print("Сцена 6")
    print()

    print("Зараз буде твоє шосте питання, відповіш на нього пройдеш далі!")
    time.sleep(3)

    random_question = random.randint(0, 1)
    questions = ["—Сумарний вік членів сім'ї з 4 чоловік дорівнює 68,"+
    "а 4 роки назад дорівнював 53. Скільки років молодшому члену сім'ї?",
    "—Скільки в мене квітів, якщо всі з них окрім двох - троянди, всі окрім двох"+
    "- тюльпани, і всі окрім двох - маргаритки?"]
    counter = 0
    if random_question == 0:
        print(questions[random_question])
        answer = input(">>> ")
        try:
            answer = int(answer)
        except:
            print("Не чую.")

        if answer == 3:
            print("Хм, добре, добре. Це було легеньке питання.")
        else:
            print("Ха-Ха, це ж просте питання.")
            counter = counter + 1
            while counter != 3:
                answer = input(">>> ")
                try:
                    answer = int(answer)
                except:
                    print("Не чую.")
                if answer != 3 and counter != 3:
                    print("Неправильно!")
                    counter = counter + 1
                else:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                if answer == 8:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                else:
                    counter == counter + 1
        if counter == 3:
            print("Ви програли!")

        time.sleep(3)
        if counter == 3:
            print()
            print("На жаль, Ви програли")
            print("Хочете почати гру знову?")
            print("Так чи Ні")
            print()
            answeraftergame = input(">>> ")
            if answeraftergame == "Так":
                firstquestion()
        else:
            seventhquestion()
    if random_question == 1:
        print(questions[random_question])
        answer = input(">>> ")
        try:
            answer = int(answer)
        except:
            print("Не чую.")

        if answer == 3:
            print("Хм, добре, добре. Правильно!")
        else:
            print("Ха-Ха, це ж просте питання.")
            while counter != 3:
                answer = input(">>> ")
                try:
                    answer = int(answer)
                except:
                    print("Не чую.")
                if answer != 3 and counter != 3:
                    print("Неправильно!")
                    counter = counter + 1
                else:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break

                if answer == 3:
                    print("Нарешті, правильно! Ти проходиш далі!")
                    break
                else:
                    counter == counter + 1
        if counter == 3:
            print("Ви програли!")
        time.sleep(3)
        if counter == 3:
            print()
            print("На жаль, Ви програли")
            print("Хочете почати гру знову?")
            print("Так чи Ні")
            print()
            answeraftergame = input(">>> ")
            if answeraftergame == "Так":
                firstquestion()
        else:
            seventhquestion()

def seventhquestion():
    """outputs the seventh question"""
    print()
    print("Сцена 7")
    print()

    print("Зараз буде твоє останнє, сьоме питання, відповіш на нього - врятуєш Іванку!")
    time.sleep(3)

    random_question = random.randint(0, 1)
    questions = ["—На столі лежить 100 аркушів паперу. За кожні 10 секунд можна порахувати "+
    "10 аркушів. Скільки секунд знадобиться, щоб порахувати 80 аркушів?",
    "—Якщо півтори курки несуть півтора яйця за півтора дня, скільки дві курки знесуть за два дні?"]
    counter = 0
    if random_question == 0:
        print(questions[random_question])
        answer = input(">>> ")
        try:
            answer = int(answer)
        except:
            print("Не чую.")

        if answer == 20:
            print("Хм, добре, добре. Правильно!")
        else:
            print("Ха-Ха, це ж просте питання.")
            counter = counter + 1
            while counter != 3:
                answer = input(">>> ")
                try:
                    answer = int(answer)
                except:
                    print("Не чую.")
                if answer != 20 and counter != 3:
                    print("Неправильно!")
                    counter = counter + 1
                else:
                    print("Нарешті, правильно! Ти виграв!!!")
                    break
                if answer == 20:
                    print("Нарешті, правильно! Ти виграв!!!")
                    break
                else:
                    counter == counter + 1
        if counter == 3:
            print("Ви програли!")

        time.sleep(3)
        if counter == 3:
            print()
            print("На жаль, Ви програли")
            print("Хочете почати гру знову?")
            print("Так чи Ні")
            print()
            answeraftergame = input(">>> ")
            if answeraftergame == "Так":
                firstquestion()
        else:
            almostend()
    if random_question == 1:
        print(questions[random_question])
        answer = input(">>> ")
        try:
            answer = int(answer)
        except:
            print("Не чую.")
        if answer == 4:
            print("Ти переміг!!!")
        else:
            print("Ха-Ха, це ж просте питання.")
            while counter != 3:
                answer = input(">>> ")
                try:
                    answer = int(answer)
                except:
                    print("Не чую.")
                if answer != 4 and counter != 3:
                    print("Неправильно!")
                    counter = counter + 1
                else:
                    print("Нарешті, правильно! Ти переміг!!!")
                    break

                if answer == 4:
                    print("Нарешті, правильно! Ти переміг!!!")
                    break
                else:
                    counter == counter + 1
        if counter == 3:
            print("Ви програли!")
        time.sleep(3)
        if counter == 3:
            print()
            print("На жаль, Ви програли")
            print("Хочете почати гру знову?")
            print("Так чи Ні")
            print()
            answeraftergame = input(">>> ")
            if answeraftergame == "Так":
                firstquestion()
        else:
            almostend()

def almostend():
    """outputs the words of enemy"""
    print()
    print("---")
    print("—О ніііііііііі, ти зміг мене перемогти!")
    print("—Ти все-таки достойний дочки голови сільради.")
    print("—Я звільняю тебе, Іванко!")
    print("---")
    time.sleep(2)
    end()

def end():
    """outputs the end of the story"""
    print("Хоробрий дільничий звільнив Іванку, і жили вони довго і щасливо!")
    print("Кінець.")

main()
time.sleep(10)
intro()
