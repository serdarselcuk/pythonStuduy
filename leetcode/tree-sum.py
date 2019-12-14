# Given an array nums of n integers, are there elements a, b, c in 
# nums such that a + b + c = 0? Find all unique triplets in the 
# array which gives the sum of zero.

#Note:
#The solution set must not contain duplicate triplets.

#Example:

#   Given array nums = [-1, 0, 1, 2, -1, -4],

#   A solution set is:
#   [[-1, 0, 1],[-1, -1, 2]]

nums = [-1, 0, 1, 2, -1, -4]

import numpy as np
def treesum():
    answer = []
    nums_ar = np.array(nums)
    nums_dict = {}
    a = 0
    for i in nums :
        a = a+1
        nums_dict[a]=i
        for j in nums :
            if i == j :
                pass
            elif (i + j )* -1 in nums_dict:
                answer.append([i, j, 0-i-j])
            else :
                continue

treesum()
print (answer)
