print ("Укажите координаты точки по осям х и у")
x = int(input())
y = int(input())
if x==0:
    print ("Точка на оси у")
elif y==0:
    print ("Точка на оси x")
elif x>0 and y>0:
    print ("Точка в первой четверти")
elif x<0 and y>0:
    print ("Точка во второй четверти")
elif x<0 and y<0:
    print ("Точка в третьей четверти")
elif x>0 and y<0:
    print ("Точка в четвёртой четверти")