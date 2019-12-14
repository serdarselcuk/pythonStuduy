ask = input ('guess the bird : ')
if ask == "falkon" :
    print('how do you know')
else:
    ask = input ('guess the bird (second chance): ')
    if ask == "falkon" :
        print('how do you know')
    else:
        ask = input ('guess the bird (third chance): ')
        if ask == "falkon" :
            print('how do you know')
        else:
            print('you could not win! ')
