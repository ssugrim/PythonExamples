f#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        global curMin
        curMin = 100000
        if root == None:
            return 0
        self.dfs(root,0)
        return curMin
    def dfs(self,node,curDep):
        global curMin
        curDep += 1
        if curDep > curMin:
            return 
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

