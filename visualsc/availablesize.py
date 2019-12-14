color = ('BLUE', 'WHITE')
whitec = ('L','S')
bluec = ('M', 'L')

order = input( 'color please :\n ').upper()
size = input('size please (L,M.S)\n').upper()

if order in color :
    print(color)

    if size in whitec or bluec :
        print('yes')
        if order == 'WHITE' :
            if size in whitec :
                print ('order is ok')
                
            else:
                print ('we have not this size')
      
        elif order == 'BLUE' :
            if size in bluec :
                print ('order is ok')
                
            else:
                print ('we have not this size')

            
    else: 
        print('we do not have this size')

else:
    print('only blue and white color available') 
