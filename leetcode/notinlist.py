l = [1, 2, 5, 45, 3, 2, 2, 4]
l2 = [12, 3, 4, 6, 7, 2]


def merge_list(l, l2):
    set_l = set(l)
    set_l2 = set(l2)
    change = [Set for Set in [set_l, set_l2]]
    list1 = []
    list2 = []
    for lists in change:
        for char in lists:
            if lists == set_l:
                if char not in l2:
                    list1.append(char)
            if lists == set_l2:
                if char not in l:
                    list2.append(char)
    return list1, list2


print(merge_list(l, l2))

