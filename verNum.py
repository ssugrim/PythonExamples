class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1arr = map(lambda x: int(x), version1.split("."))
        v2arr = map(lambda x: int(x), version2.split("."))
        while v1arr and v2arr:
           l = v1arr.pop(0)
           r = v2arr.pop(0)
           if l > r:
               return 1
           elif l < r:
               return -1
           else:
               next
        if len(v1arr) == 0:
            if v2arr.count(0) == len(v2arr):
                return 0
            else:
                return -1
        else:
            if v1arr.count(0) == len(v1arr):
                return 0
            else:
                return 1


x = Solution()
print x.compareVersion("1","1.1")
print x.compareVersion("0.1","1.1")
print x.compareVersion("1.1","1.1")
print x.compareVersion("1.0","1")
print x.compareVersion("1.1","1.2")
print x.compareVersion("1.2","13.37")
print x.compareVersion("1.0","1.0.7")
