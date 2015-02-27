#Definition for a  binary tree node
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p == None and q != None:
            return False
        if p != None and q == None:
            return False
        return self.bfs(p,q)
    def bfs(self,node1,node2):
        que1 = deque()
        que2 = deque()
        que1.append(node1)
        que2.append(node2)
        while que1 or que2:
            print "que1 %s" % (map(lambda node: node.val, que1))
            print "que2 %s" % (map(lambda node: node.val, que2))
            cur1 = que1.popleft()
            cur2 = que2.popleft()

            if cur1.val != cur2.val:
                return False
            if cur1.left == None and cur2.left != None:
                return False
            if cur2.left == None and cur1.left != None:
                return False
            if cur1.right == None and cur2.right != None:
                return False
            if cur2.right == None and cur1.right != None:
                return False
            if cur1.left != None and cur2.left != None and cur1.right != None and cur2.right != None:
                if cur1.left.val != cur1.left.val:
                    return False
                if cur1.right.val != cur1.right.val:
                    return False

            if cur1.left != None:
                que1.append(cur1.left)
            if cur1.right != None:
                que1.append(cur1.right)
            if cur2.left != None:
                que2.append(cur2.left)
            if cur2.right != None:
                que2.append(cur2.right)
        return True

x = Solution()

root = TreeNode(10)
root.left = TreeNode(5)
#root.right = TreeNode(15)
#root.left.left = TreeNode(4)
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
#root = TreeNode(1)
#root.left = TreeNode(2)
#root.right = TreeNode(3)
#root.left.left = TreeNode(4)
#root.left.right = TreeNode(5)
#root.left.left.left = TreeNode(8)

root1 = TreeNode(10)
root1.right = TreeNode(5)
#root1.right = TreeNode(3)
#root1.left.right = TreeNode(15)
#root1.left.right = TreeNode(5)
#root1.right.left = TreeNode(6)
#root1.right.right = TreeNode(7)
#root1.left.left.left = TreeNode(8)
##root1.left.right.left = TreeNode(10)
#root1.right.left.right = TreeNode(12)
#root1.right.right.right = TreeNode(14)
#root1.left.left.left.left = TreeNode(15)
#root1.right.left.right.left = TreeNode(19)
print TreeNode(1) == TreeNode(1)
print "answer %s" % (x.isSameTree(root,root1))
print "answer %s" % (x.isSameTree(TreeNode(1),TreeNode(0)))

#root = TreeNode(0)
#print "answer %s" % (x.minDepth(root))

