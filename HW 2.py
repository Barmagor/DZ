for x in range (2):
    for y in range (2):
        for z in range (2):
            print (not (x or y or x)  == (not x and not y and not z)) 
            print (x,y,z)