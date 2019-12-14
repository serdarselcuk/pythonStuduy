
left = 5
right = 30
arr = [digit for digit in range (left,right+1)]
array = [digit for digit in range (left,right+1)]
for num in arr:
    ten = 1
    num1 = num
    while ten > 0:
        ten, one = divmod(num1, 10)
        num1 = ten
        if one == 0 or num % one != 0:
            array.remove (num)
            break
        
print (array)
