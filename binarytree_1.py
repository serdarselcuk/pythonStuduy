#%%
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "<%d>" % self.val 


def tree_from_array(arr):

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

    root.left = tree_from_array(left)
    root.right = tree_from_array(right)

    return root

tree = tree_from_array([0, 1, 2, 3, 4, 5, 6, 7, 8])

#%%

def sumtree(root):
    if root is None:
        return 0

    return root.val + sumtree(root.left) + sumtree(root.right)




#%%
sumtree(tree)