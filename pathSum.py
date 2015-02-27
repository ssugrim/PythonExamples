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
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        return self.dfs(root,0,sum)
    def dfs(self,node,runsum, target):
        runsum += node.val
        if runsum == target and node.left == None and node.right == None:
            return True
        if node.left != None:
            if self.dfs(node.left, runsum, target):
                return True
        if node.right != None:
            if self.dfs(node.right, runsum,target):
                return True
        return False


x = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

print x.hasPathSum(root,22)

#root = TreeNode(1)
#root.left = TreeNode(2)
#print x.hasPathSum(root,1)

