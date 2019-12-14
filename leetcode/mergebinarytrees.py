def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
		if t1 and t2:
			root=TreeNode(t1.val+t2.val)
			root.left=self.mergeTrees(t1.left,t2.left)
			root.right=self.mergeTrees(t1.right,t2.right)

		else:
			return t1 or t2
		return root