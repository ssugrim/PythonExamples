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
    def minDepth(self, root):
        global curMin
        if root == None:
            return 0
        curMin = self.maxDep(root)
        self.dfs(root,0)
        return curMin
    def maxDep(self,node):
        left = 0
        right = 0
        if node.left != None:
            left = self.maxDep(node.left)
        if node.right != None:
            right = self.maxDep(node.right)
        return max([left,right]) + 1
    def dfs(self,node,curDep):
        global curMin
        curDep += 1
#        if curDep > curMin:
#           return
        if node.left == None and node.right == None:
            if curDep < curMin:
                curMin = curDep
        if node.left != None:
            self.dfs(node.left, curDep)
        if node.right != None:
            self.dfs(node.right, curDep)


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
print x.maxDep(root)

