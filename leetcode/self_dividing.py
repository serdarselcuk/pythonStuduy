
left = 5
right = 2589
arr = [digit for digit in range (left,right+1)]

def get_digits(num):
        
        digits=[]
        while num > 0:
                num, rem = divmod(num, 10)
                digits.append(rem)
                
        return digits

def is_divisible(num):

    for digit in get_digits(num):
        if digit == 0 or num % digit > 0:
            return False

    return True

