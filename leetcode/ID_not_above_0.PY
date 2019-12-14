A = "DDIDDIIDIIDIDIIDIDDDDDIDIDIDIDIIII"

def st_match(List,num):
    B =[]
    for i in A:
        if i =='D':
            num-=1
        else:
            num+=1
        B.append(num)
    return B    

deficit = min(st_match(A,0))

if deficit <= -1 :
    return(st_match(A,(deficit*(-1))))
else:
    return (st_match(A,0),)
