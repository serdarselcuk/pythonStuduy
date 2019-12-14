# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
#fh = open(fname)
fh = open ('mbox-short.txt')
summ=0
avar=0
for line in fh:
    
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        
        stre=line.find(' ')
        tre=line[stre:]
        ftr=float(tre)
        summ=ftr+summ
        avar=avar+1

print('avaradge spam confidence :', summ/avar)
