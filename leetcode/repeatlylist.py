ss = [1,2,3,3]
num=[]
def finid():
    for i in ss:
        
        if i in num:

            if ss.count(i) == len(ss)/2:
                return(i)

            else:
                continue
        else:
            num.append(i)
        
            continue

print(finid( ))
