class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
	lead = 0
	maj = num[0]
	for i in num:
		if i == maj:
			lead += 1
		else:
			lead -= 1
			if lead == 0:
				maj = i
				lead = 1
	return maj
x = Solution()
print x.majorityElement([1,2,3,1,1,4])
