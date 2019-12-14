
x=7
y=3
def modul(m,x):
        num = []
        while x > 0:
                a = 0
                while m**(a+1) <= x:
                        a +=1
                num.append(a)
                x = x-m**a
        return num   
A = (modul(2,x))
B = (modul(2,y))
C = set(A + B)
return (2*len(C)-(len(A)+len(B)))



