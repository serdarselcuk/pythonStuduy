
from pathlib import Path
book = "romeo.txt"
source = open(Path.cwd()/visualsc/py4e_e_8-1/book)
readsource = source.read()
count = 0
for line in source:
    count = count + 1
    print(line.rstrip( ))
    print(count)