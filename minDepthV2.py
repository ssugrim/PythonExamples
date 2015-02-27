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
        if root == None:
            return 0
        return self.bfs(root)
    def bfs(self,node):
        que1 = []
        que2 = []
        que1.append(node)
        depth = 0
        flag = True
        while que1 or que2:
            print "que1 %s" % (map(lambda node: node.val, que1))
            print "que2 %s" % (map(lambda node: node.val, que2))
            if flag:
                cur = que1.pop(0)
                print "cur: %s, depth: %s" %(cur.val,depth)
                if cur.left == None and cur.right == None:
                    depth += 1
                    break
                if cur.left != None:
                    que2.append(cur.left)
                if cur.right != None:
                    que2.append(cur.right)
                if len(que1) == 0:
                    flag = False
                    depth += 1
            else:
                cur = que2.pop(0)
                print "cur: %s, depth: %s" %(cur.val,depth)
                if cur.left == None and cur.right == None:
                    depth += 1
                    break
                if cur.left != None:
                    que1.append(cur.left)
                if cur.right != None:
                    que1.append(cur.right)
                if len(que2) == 0:
                    flag = True
                    depth += 1
        return depth

        


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
#root = TreeNode(1)
#root.left = TreeNode(2)
#root.right = TreeNode(3)
#root.left.left = TreeNode(4)
#root.left.right = TreeNode(5)
#root.left.left.left = TreeNode(8)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
#root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
#root.left.right.left = TreeNode(10)
root.right.left.right = TreeNode(12)
root.right.right.right = TreeNode(14)
root.left.left.left.left = TreeNode(15)
root.right.left.right.left = TreeNode(19)

print "answer %s" % (x.minDepth(root))

#root = TreeNode(0)
#print "answer %s" % (x.minDepth(root))

