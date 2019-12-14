
left = 5
right = 2589
arr = [digit for digit in range (left,right+1)]

def selfdivid(num):
        ten = 1
        num1=num
        while ten > 0:
            ten, one = divmod(num1, 10)
            num1 = ten
            if one == 0 or num % one != 0:           
                return False
        return True

is_dividabl = []
for num in arr :
       if selfdivid(num) is True:
                is_dividabl.append(num)
print (is_dividabl)