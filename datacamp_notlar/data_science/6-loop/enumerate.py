# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         

# Build a for loop from scratch
for x,y in enumerate(house):
    print('the '+ house[x][0],'is',house[x][1], y )