S = "(()())(())"


def parenthesis(S):

    cur_level = 0
    kume = []
    for char in S:

        if cur_level > (char == ")"):
            # char ")", cur_level > 1
            #      "(". cur_level > 0
            kume.append(char)

        cur_level += -1 + 2 * (char == "(")

    return "".join(kume)


print(parenthesis(S))
