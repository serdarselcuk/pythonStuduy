A = [[1,1,0],[1,0,1],[0,0,0]]
for r, row in enumerate(A):
    row = row[::-1]
    for i in range(len(row)):
        row[i] = 1-row[i]
    A[r] = row
print( A)