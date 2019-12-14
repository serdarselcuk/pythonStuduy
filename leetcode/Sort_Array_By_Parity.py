A = [0,2]


# a pointer to the beginning
left = 0
# a pointer to the end
right = len(A) - 1

while left < right:

    # if left pointer is even, do nothing move right
    while A[left] % 2 == 0:
        if left < len(A)-1:
            left += 1
        else:
            break
    # if right pointer is odd, do nothing move left
    while A[right] % 2 == 1:
        if right != 0:
            right -= 1
        else:
            break
    # if right and left switched places, than we looked
    # at every element; so break out of the loop!
    if left >= right:
        break
    
    # otherwise right is pointing at an even
    # left is pointing at an odd number; swap!
    A[left], A[right] = A[right], A[left]
print(A)


