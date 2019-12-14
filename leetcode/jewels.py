#soru : 771 (55 ms)
J = "aAsSF"
S = "AASFSGCDFLYTBLVDASsfsassdfsvosmtkhbd"

def Jevel():
    x = 0
    y = x
    for i in J:
        x = S.count(i)
        y = x + y
    return(y)
print(Jevel())