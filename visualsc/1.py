maxvalue = -1E6
minvalue = 1E6
while True :
    num = input('enter number :')

    try:
        num = float(num)
    except:
        if num == 'done' :
            break
        else:
            print("Invalid input.")
            continue

    num = int(num)

    if num > maxvalue :
        maxvalue = num
        
    if num < minvalue :
        minvalue = num
        
        
print('Maximum is', maxvalue)
print('Minimum is', minvalue)