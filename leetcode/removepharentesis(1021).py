
S = "(()())(())"

def parenthesis(S):

    cur_level = 0
    kume = []
    for char in S:

        if char == "(":
            if cur_level > 0:
                kume.append("(")
            cur_level += 1                
        else:
            if cur_level > 1:
                kume.append(")")
            cur_level -= 1

    return "".join(kume)

print(parenthesis(S))