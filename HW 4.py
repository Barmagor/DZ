print ("Укажите номер четверти")
x = int(input())
if x==1:
    print ("x от 0 до плюс бесконечности, у от 0 до плюс бесконечности")
elif x==2:
    print ("x от 0 до минус бесконечности, у от 0 до плюс бесконечности")
elif x==3:
    print ("x от 0 до минус бесконечности, у от 0 до минус бесконечности")
elif x==4:
    print ("x от 0 до плюс бесконечности, у от 0 до минус бесконечности")
elif x<1 or x>4:
    print("Некорректный номер четверти")
