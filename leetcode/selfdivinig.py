
left = 5
right = 2589
arr = [digit for digit in range (left,right+1)]

def get_digits(num):
        ten = 1
        digits=[]
        while ten > 0:
                ten, one = divmod(num, 10)
                digits.append(one)
                num = ten
        return digits

def is_dividible(num):
        dividers = get_digits(num)
        if 0 in dividers:            
                return False
        divider = (i for i in dividers)
        count = 0
        while (num % ( next(divider)) == 0 ) is True:
                count += 1
                if count == len(dividers):
                        return True

is_dividabl = []
for num in arr :
        if is_dividible(num) is True:
                is_dividabl.append(num)
print (is_dividabl)