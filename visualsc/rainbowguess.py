rainbow = "red orange yellow green blue indigo violet"
while True:
    for i in range(3):
        chance=input()

        if not chance in rainbow:
            print('wrong')
        else:
            break
    break