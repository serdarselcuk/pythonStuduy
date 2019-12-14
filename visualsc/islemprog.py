num = 1,35,23,5,43
x=0
y=1
target=28
for i in num:
    if num[x]+num[y]==target:
        print('ok')
        break
    else:
        for i in num:
            x=x+1
            if num[x] + num[y] == target :
                print(num[x],'+',num[y],'=',target)
            else:
                y=y+1
                continue
        continue