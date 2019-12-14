A = [0,0,0,0,0,0,0,0,1,1,1,1]
A.reverse()
Sum = []
for i, x in enumerate(A) :
    if x == 1 :
        Sum.append(2**i)
print(sum(Sum))