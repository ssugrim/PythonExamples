class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        digits = []
        for c in s:
            digits.append(ord(c.upper()) - 64)
            sum = 0
        for i,v in enumerate(digits):
            sum += 26 ** (len(digits) - i -1 ) * v
        return sum

x = Solution()
print x.titleToNumber('A')
print x.titleToNumber('B')
print x.titleToNumber('C')
print x.titleToNumber('AB')
