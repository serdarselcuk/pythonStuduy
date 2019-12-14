S = "DDIDIDDIDIID"
#create the list of numbers that we can use
B=[]

for i in range(S.count('')):

    B.append(i)
#first the firs number of B must be decided to not go under the zero when we are decrising the numbers
start = B.pop(B[S.count('D')])
B[1:(B.pop(B[S.count('D')]))+1] = B[0:(B.pop(B[S.count('D')]))]
B[0] = start

for position, command in enumerate (S):

    

#while iterating the orders of S can create 2 pointers for indexing the numbers for both biggers and the smallers in B
    
    pointer = position+1
    pointer_2 = -1
#we need to control the pointer if its to big before it goes while loop
    if  pointer == len(S)-1 :
                break
#the pointer that choses the number in B list acording to comands of list S. 

    if command == 'D' :
        
#to decide decreasing according to the command. ''' not to decrease or increase too much, pointer needs to look for the next commands.'''

        while command == S[pointer]:

# again as an secure step we must stop the pointer at the and of the S index in the while loop
            if  pointer == len(S)-1 :
                break
            pointer += 1
            
        B[position+1],B[pointer] = B[pointer],B[position+1]

    elif command == 'I' :
        
        while command == S[pointer]: 

            if  pointer == len(S)-1 :
                break
#pointer following for the command and pointer_2 is for the item that we will take 
            pointer += 1
            pointer_2-=1
            
        B[position+1],B[pointer_2] = B[pointer_2],B[position+1]
    



print(B)
