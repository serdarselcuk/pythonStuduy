# returns min numbers of numerics that i must to
#  take to the begining of the list
kume = [2, 1, 2, 1, 3, 2, 5, 7, 4, 1, 2, 2, 1]


def sort_heights(kume):
    count = 0
    # min vals of list are not necessary to iterate
    mini_count = kume.count(min(kume))
    for char in range((len(kume)) - mini_count):
        maxi = max(kume)
        # if index of maxi is at the beginning it dont need to change its places
        if kume.index(maxi) != 0:
            kume.remove(maxi)
            count += 1
        else:
            kume.remove(maxi)
    return count


print(sort_heights(kume))
