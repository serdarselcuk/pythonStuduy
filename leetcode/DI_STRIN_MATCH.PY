S = 'DDDIDIDIDID'
        
left = 0
right = len(S)        
nums = list(range(right + 1))
        
res = []
        
for char in S:
            
    if char == "I":
        res.append(nums[left])
        left += 1
    else:
        res.append(nums[right])
        right -= 1
                
res.append(nums[left]) # left == right, it doesn't matter
                
print( res)