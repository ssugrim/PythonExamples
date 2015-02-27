class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) < 2:
            return 0
        runSum = 0
        maxBack = max(A)
        if maxBack == 1:
            return A.count(1) - 1
        while A:
            if len(A) == 2:
                runSum +=1
                break
            if len(A) == 1:
                break
            curJump = self.findTailMax(A,maxBack)
            runSum += 1
            curJumpInd = len(A)  - A[::-1].index(curJump)
            if curJumpInd == len(A):
                curJumpInd -= 1
            A = A[:curJumpInd]
        return runSum
    def findTailMax(self,A,maxBack):
        if A[0] >= len(A):
            return A[0]
        TailMax = A[-2]        
        for i,v in enumerate(reversed(A)):
            if i <= v:  
                TailMax = v
            if i == maxBack:
                break
        return TailMax

x = Solution()
print "Answer %s" % x.jump([2,3,1,1,4])
print "Answer %s" % x.jump([0])
print "Answer %s" % x.jump([2,3,1,1,4,2,3,1,1,4])
print "Answer %s" % x.jump([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
print "Answer %s" % x.jump([1,2,3])
print "Answer %s" % x.jump([3,2,1])
print "Answer %s" % x.jump([3,2,1])
print "Answer %s" % x.jump([2,0,2,0,1])
