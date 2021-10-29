from random import *
from keyboard import *
print("Давай сыграем в игру выбери: Камень , ножницы или бумагу.")
print()
suk=0
while suk not in [1,2,3]:
    try:
        suk=int(input("Ты хочешь сыграть с роботом или с другом => ") ) 
    except TypeError:
        print("Можно только 1 и 2!")
bot=0
gamer=0
nic=0
god=0
if suk==1:
    while True:
        print("Ты хочешь продолжить (Нажми backspace) или закочить (Нажми enter)?")
        print()
        try:
             if read_key()=="backspace":
                print()
                print("Продолжаем игру.")
                print()
                pass
        except:
                ValueError
        try:
            if read_key()=="enter":
                print()
                print("Спасибо за игру!")
                print()
                print()
                print(f"Ничьих было {nic} , Побед у игрока {gamer} , Побед у робота было {bot}.")
                break
        except:
                ValueError
        c=0
        while c not in [1,2,3] :
            try:
                c=int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
            except TypeError:
                print("Можно только 1,2,3!")
            print()
            if c == 1:
                print("Вы выбрали камень.")
                print()
            elif c == 2:
                print("Вы выбрали ножницы.")
                print()
            elif c == 3:
                print("Вы выбрали бумагу.")
                print()
            b = randint(1,3)
            print()
            if b == 1:
                print("Компьютер выбрал камень.")
                print()
            elif b == 2:
                print("Компьютер выбрал ножницы.")
                print()
            elif b == 3:
                 print("Компьютер выбрал бумагу.")
                 print()
            if c == 1 and b == 1:
                nic+=1
                win=0
            elif c== 1 and b == 2:
                gamer+=1
                win=1
            elif c== 1 and b == 3:
                bot+=1
                win=2
            elif c== 2 and b == 1:
                bot+=1
                win=2
            elif c== 2 and b == 2:
                nic+=1 
                win=0
            elif c== 2 and b == 3:
                gamer+=1
                win=1
            elif c== 3 and b == 1:
                gamer+=1
                win=1
            elif c== 3 and b == 2:
                bot+=1
                win=2
            elif c== 3 and b == 3:
                win=0
                nic+=1
            print()
            if win == 0:
                print("Ничья, повезёт в след. раз!")
            elif win == 1:
                print("Ты Победил, Лучший!")
            elif win == 2:
                print("Победил компьютер, как жаль!")
if suk==2:
    while True:
        print("Ты хочешь продолжить (Нажми backspace) или закочить (Нажми enter)?")
        print()
        try:
             if read_key()=="backspace":
                print()
                print("Продолжаем игру.")
                print()
                pass
        except:
                ValueError
        try:
            if read_key()=="enter":
                print()
                print("Спасибо за игру!")
                print()
                print(f"Ничьих было {nic} , Побед у первого игрока {gamer} , Побед у второго игрока было {god}.")
                break
        except:
                ValueError
        c=0
        while c not in [1,2,3] :
            try:
                c=int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
            except TypeError:
                print("Можно только 1,2,3!")
            print()
            if c == 1:
                print("Вы выбрали камень.")
                print()
            elif c == 2:
                print("Вы выбрали ножницы.")
                print()
            elif c == 3:
                print("Вы выбрали бумагу.")
                print()
        b=0
        while b not in [1,2,3] :
            try:
                b=int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
            except TypeError:
                print("Можно только 1,2,3!")
            print()
            if b == 1:
                print("Игрок 2 выбрал камень.")
                print()
            elif b == 2:
                print("Игрок 2 выбрал ножницы.")
                print()
            elif b == 3:
                 print("Игрок 2 выбрал бумагу.")
                 print()
            if c == 1 and b == 1:
                nic+=1
                win=0
            elif c== 1 and b == 2:
                gamer+=1
                win=1
            elif c== 1 and b == 3:
                god+=1
                win=2
            elif c== 2 and b == 1:
                god+=1
                win=2
            elif c== 2 and b == 2:
                nic+=1 
                win=0
            elif c== 2 and b == 3:
                gamer+=1
                win=1
            elif c== 3 and b == 1:
                gamer+=1
                win=1
            elif c== 3 and b == 2:
                god+=1
                win=2
            elif c== 3 and b == 3:
                win=0
                nic+=1
            if win == 0:
                print("Ничья, повезёт в след. раз!")
                print()
            elif win == 1:
                print("Победил первый игрок, Лучший!")
                print()
            elif win == 2:
                print("Победил второй игрок, как жаль!")
                print()
if suk==3:
    while True:
        print("Ты хочешь продолжить смотреть за битвой (Нажми backspace) или закочить (Нажми enter)?")
        print()
        try:
             if read_key()=="backspace":
                print()
                print("Продолжаем просмотр.")
                print()
                pass
        except:
                ValueError
        try:
            if read_key()=="enter":
                print()
                print("Спасибо за просмотр!")
                print()
                print()
                print(f"Ничьих было {nic} , Побед у первого робота было {gamer} , Побед у второго робота было {bot}.")
                break
        except:
                ValueError
        b = randint(1,3)
        g = randint(1,3)
        print()
        if b == 1:
            print("Робот 1 выбрал камень.")
            print()
        elif b == 2:
            print("Робот 1 выбрал ножницы.")
            print()
        elif b == 3:
            print("Робот 1 выбрал бумагу.")
            print()
        if g== 1:
            print("Робот 2 выбрал камень.")
            print()
        elif g == 2:
            print("Робот 2 выбрал ножницы.")
            print()
        elif g == 3:
            print("Робот 2 выбрал бумагу.")
            print()
        if b==g:
            print("Ничья")
            nic+=1
        elif b==1 and g==2 or b==2 and g==3 or b==3 and g==1:
            gamer+=1
            print("Выиграл робот 1")
        elif b==1 and g==3 or b==2 and g==1 or b==3 and g==2:
            bot+=1
            print("Выиграл робот 2")
