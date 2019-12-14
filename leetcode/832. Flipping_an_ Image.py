#832. Flipping an Image
A = [[1,1,0],[1,0,1],[0,0,0]]

B = []
for cell in A :
    B.append(list(reversed(cell)))

C = []
   
for cell in B:
    D = []
    for eleman in cell:
#""" 
#"xor" diye bir islem daha var, "exclusive or" demek
#1 ^ 1 = 0
#1 ^ 0 = 1
#0 ^ 1 = 1
#0 ^ 0 = 0
#isleme girenler ayniysa 0, farkliysa 1 veriyor ozetle
#"""
        eleman = eleman ^ 1
        
        D.append(eleman)
        
    C.append(D)
print(C)