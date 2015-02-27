#Definition for a  binary tree node
from collections import deque

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        que = deque()
        que.append([m,n])
        paths = 0
        while que:
            cp = que.popleft()
            if cp[0] - 1 >= 1:
                que.append([cp[0] - 1,cp[1]])
            if cp[1] - 1 >= 1:
                que.append([cp[0],cp[1] - 1])
            if cp[1] == 1 and cp[0] == 1:
                paths += 1
#            print cp
#            print que
        return paths


x = Solution()
print "sol %s" % (x.uniquePaths(2,3))

#recursive solution
#    def uniquePaths(self, m, n):
#        if m == 1 or n == 1:
#            return 1
#        return self.uniquePaths(m, n -1 ) + self.uniquePaths(m - 1, n)
