grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

maxi_horiz = []
maxi_vert = grid[0][:]
for i in range (len(grid)):
    
    maxi_horiz.append(max(grid[i]))
    if i > 0 :
        for turn, num in enumerate(grid[i]):

            if num > maxi_vert[turn]:
                maxi_vert[turn] = num
            else :
                continue 
summ = 0
for i in range (len(grid)):
    for turn, num in enumerate(grid[i]):
        summ += (min(maxi_horiz[i], maxi_vert[turn])-num)
print(maxi_horiz , maxi_vert, summ)
