#This program requires the use of while loop, if, elif, else, if, else (nested), casting of type, between strings and numbers. The program should only use code syntax 
# covered in modules 1 - 4. The program must result in print output using the numeric input, similar to that shown in the samples displaying "Items" and "Total".
thelist=[]
ask = input('raport type A/T: ').upper()
while True: 
    if ask =='A' or 'T' :
        break
    else:
        ask = input('raport type A/T: ').upper()

def add_report(ask):
    if ask=='A' :
        x=len(thelist)
        a=0
        print('items','\n')
        for i in range (x):
            print(thelist[a])
            a=a+1
        print('TOTAL','\n',sum(thelist))
    if ask=='T':
        print ('TOTAL','\n',sum(thelist))

while True:
    word=input('enter an integer or Q : ').upper()
    if word.isalpha():
        if word.startswith('Q'):
            add_report(ask)
           
        else:
            print('invalid')
        
    elif word.isdigit():
        num=int(word)
        thelist.append(num)
        
    else:
        print('invalid')
