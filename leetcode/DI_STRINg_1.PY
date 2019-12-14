S = "DDDDDDDDDDDD"
#create the list of numbers that we can use:B
B=[]

for i in range(len(S)+1):
    B.append(i)
#speare the number and create the lists that will use for I or D commands
com_I = S.count('I')
com_D = S.count('D')

big_grup = B[-com_I-1:-1]
small_grup = B[0:com_D]

print(small_grup,big_grup)
#two pointers for chosing the numbers in two grup of lists
right = -1
left = 0
# create C for the last list
C =[ small_grup[-1]]
for i , com in enumerate(S):
    #two pointers for chosing the numbers in two grup of lists controller will be used for controlling bommans in S
    controller = i
    right = -1
    left = 0
    if i == len(S)-1 :
        C = C + big_grup + small_grup
        

    #making list according to commands
    elif com == 'I':
        #if 'I' command will continue next (controller)in S we must take the small one in big grup
        while S[controller+1]==com:
            right -= 1
            controller +=1

            #if right pointer will goes to much we must stop this
            if controller == len (S)-2:
                break
        C.append(big_grup[right]) 
        big_grup.remove(big_grup[right])
    elif com == 'D' :
        #if 'D' command will continue next (controller)in S we must take the big one in small grup
        while S[controller+1]==com:
            left += 1
            controller += 1
            #if left pointer will goes to much we must stop this
            if controller == len (S)-2:
                break
        
        C.append(small_grup[left])
        small_grup.remove(small_grup[left])

    print(C)

