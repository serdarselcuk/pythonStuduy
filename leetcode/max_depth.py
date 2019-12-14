from make_tree import *

giris = [3,9,20,null,null,15,7]

root = array2tree( giris )

def maxDepth(root):

    if root is None:
        return 0
        
    return max(maxDepth(root.left),
               maxDepth(root.right))+1

