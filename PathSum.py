# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution:

    def hasPathSum(self, root, target):

        if root is None:
            return target == 0

        else:
            res = 0
            target -= root.val

            if target == 0 and root.left is None and root.right is None:
                return 1

            if root.left:
                res = res or self.hasPathSum(root.left, target)
            if root.right:
                res = res or self.hasPathSum(root.right, target)

            return res
