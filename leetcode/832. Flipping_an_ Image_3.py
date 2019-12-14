def flipinvert(A):

    for cell in A:

        left = 0
        right = len(cell) - 1

        while right > left:
            # dunku gibi sol-sag yer degisiyorum, degisirken xor uyguluyorum
            cell[left], cell[right] = cell[right] ^ 1, cell[left] ^ 1
            left += 1
            right -= 1

        # eger tek sayida eleman varsa, ortadakini yer degismek diye bir sey
        # yok, ama xor uygulanacak
        if left == right:
            cell[left] ^= 1

    return A
print(flipinvert())