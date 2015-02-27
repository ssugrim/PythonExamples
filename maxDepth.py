#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def maxDepth(self,node):
        if node == None:
            return 0
        return self.dfs(node)
    def dfs(self,node):
        left = 0
        right = 0
        if node.left != None:
            left = self.maxDepth(node.left)
        if node.right != None:
            right = self.maxDepth(node.right)
        return max([left,right]) + 1


x = Solution()
#root = TreeNode(5)
#root.left = TreeNode(4)
#root.right = TreeNode(8)
#root.left.left = TreeNode(11)
#root.right.left = TreeNode(13)
#root.right.right = TreeNode(4)
#root.left.left.left = TreeNode(7)
#root.left.left.left.right = TreeNode(7)
#root.left.left.left.right.right = TreeNode(7)
#root.left.left.left.right.right.right = TreeNode(7)
#root.left.left.right = TreeNode(2)
#root.right.right.right = TreeNode(1)
#
#print x.minDepth(root)
#
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print x.maxDepth(root)
