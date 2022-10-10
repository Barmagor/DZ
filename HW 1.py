print ("Введите номер дня недели")
x = int(input())
if x>7:
    print ("Такого дня нет!")
elif x>0 and x<=5:
    print ("Будний")
elif x>5 and x<8:
    print ("Выходной")