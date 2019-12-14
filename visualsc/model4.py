#This program requires the use of while loop to get non-empty input, if, else, if, else (nested), .isdigit() check for integer only input, .isalpha() check for alphabetic only input. The program should only use code syntax covered in modules 1 - 4. The program must result in printed message analysis of the input.

def str_analysis():


    while True:
        word=input( 'enter word or integer : ')
        if word == '':
            word=input( 'enter word or integer : ')
        elif word.isalpha():
            print(word, ' is all alphabetical characters! ')
            break
        elif word.isdigit():
            number= int(word)

            if number > 99:
                print(number, "is a prety big number ")
                break
            else:
                print(number, "is a smaller number than expected")
            break
        else:
            print( word, 'is neither all alpha nor all digit')
            break



str_analysis()