nums = [2, 7, 11, 15]
target = 9

for q in nums:
    if target - q in nums:
        print(nums.index(q),nums.index(target-q))
        break
    else:
        continue