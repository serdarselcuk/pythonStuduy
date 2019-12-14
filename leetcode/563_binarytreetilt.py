from make_tree import *

giris = [1, 2]

root = array2tree(giris)


def findTilt(root: TreeNode) -> int:
    def difer(root):
        if root is None:
            return 0
        return abs(root.left.val - root.right.val)

    return difer(root) + difer(root.right) + difer(root.left)


print(findTilt(root))

