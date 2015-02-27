class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        compliments = {}
        ind1 = 0
        ind2 = 0
        for i,x in enumerate(num):
            diff = target - x
            compliments[diff]=i
        print compliments
        for i,x in enumerate(num):
            if target - x == x:
                if num.count(x) < 2:
                    continue
            if x in compliments:
                ind1 = i + 1
                ind2 = compliments[x] + 1
                break
        return[ind1, ind2]

x = Solution()
print [0,4,3,0]
print 0
print x.twoSum([0,4,3,0],0)
print [2,7,11,15]
print 9
print x.twoSum([2,7,11,15],9)
print [3,2,4]
print 6
print x.twoSum([3,2,4],6)
