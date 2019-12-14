J = "AsDf"
setj = set(J)
S = "VDASsfsassdfsvos"
sets = set(S)

def jewels():
    n_jew = 0
    for i in S:
        if i in setj:
            n_jew += 1
    return n_jew

print(jewels())