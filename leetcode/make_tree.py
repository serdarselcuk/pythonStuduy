#%%
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "<%d>" % self.val 


def array2tree(arr):

    if not arr:
        return None

    root = TreeNode(arr[0])

    p = cur_len = 1
    left = []
    right = []
 
    while p < len(arr):

        left += arr[p:p+cur_len]
        right += arr[p+cur_len:p+2*cur_len]

        p += 2 * cur_len
        cur_len *= 2 

    root.left = array2tree(left)
    root.right = array2tree(right)

    return root

null = None