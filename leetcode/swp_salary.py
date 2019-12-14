salary = {"headers":{"salary":["id","name","sex","salary"]},"rows":{"salary":[[1,"A","m",2500],[2,"B","f",1500],[3,"C","m",5500],[4,"D","f",500]]}}
print(salary.keys())

headers = salary['headers']
rows = salary['rows']
print(headers)

rows_s = rows['salary']
print(rows_s[0:1])
print(rows_s[1:2])
print(rows_s[2:3])
print(rows_s[3:])
rows_s_1 = rows_s[0:1]
print(type(rows_s_1))
print (rows_s_1[0][2])