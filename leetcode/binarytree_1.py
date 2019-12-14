t1 = [1,3,2,5]
t2 = [2,1,3,null,4,null,7]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
		if t1 and t2:
			root = TreeNode(t1.val+t2.val)
			root.left = self.mergeTrees(t1.left,t2.left)
			root.right = self.mergeTrees(t1.right,t2.right)

		else:
			return t1 or t2
		return root