shirtsize=input('which size?: ')
if shirtsize.isdigit() == False:
    print("Invalid: guess should only use digits")
elif shirtsize=='s':
    print('it costs $3')
elif shirtsize=='l':
    print('it costs $4')
elif shirtsize=='m':
    print('unfortunataly it has finished')
else:
    print('you entered unnown size?')