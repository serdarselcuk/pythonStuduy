x=2
y=input('insert : ')
while True:
    if  y == 'done' :
        exit
    elif x < y :
        x = x+1
    else :
        x = x-1
       
    print ('value', x)