class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    def rotOne(self,nums):
        tmp = nums[-1]
        for i in reversed(range(len(nums))):
            nums[i] = nums[i-1]
        nums[0] = tmp
        return nums
    def rotate(self, nums, k):
        for i in range(k):
            self.rotOne(nums)
        return nums

x = Solution()
print x.rotate([1,2,3,4,5,6,7],3)
print x.rotate([1,2],1)
