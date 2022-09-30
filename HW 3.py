print ("Укажите координаты точки по осям х и у")
x = int(input())
y = int(input())
if x==0:
    print ("Точка на оси у")
if y==0:
    print ("Точка на оси x")
if x>0 and y>0:
    print ("Точка в первой четверти")
if x<0 and y>0:
    print ("Точка во второй четверти")
if x<0 and y<0:
    print ("Точка в третьей четверти")
if x>0 and y<0:
    print ("Точка в четвёртой четверти")