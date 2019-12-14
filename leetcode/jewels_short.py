
#soru : 771 (55 ms)
J = "AsDf"
S = "VDASsfsassdfsvos"


def jewels():
    return sum(map(J.count, S))


print(jewels())