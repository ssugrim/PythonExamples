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
    def fib(self,n):
        print n
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1)+self.fib(n-2)

x = Solution()
print "sol %s" % (x.fib(5))
