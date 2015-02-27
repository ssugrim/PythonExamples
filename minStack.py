class MinStack:
    # @param x, an integer
    # @return an integer
	def __init__(self):
		self.data = []
		self.minimum = []
	def push(self, x):
		if len(self.data) == 0:
			self.data.append(x)
			self.minimum.append(x)
		else:
			self.data.append(x)
			if x <= self.minimum[-1]:
				self.minimum.append(x)
		print self.data
		print self.minimum
	def pop(self):
		popped = self.data.pop()
		if popped == self.minimum[-1]:
			self.minimum.pop()
		print self.data
		print self.minimum
		return popped
	def top(self):
		print self.data
		print self.minimum
		return self.data[-1]
	def getMin(self):
		print self.data
		print self.minimum
		return self.minimum[-1]
x = MinStack()
x.push(3)
x.push(5)
x.push(2)
x.push(8)
x.push(2)
x.push(2)
x.push(9)
print "min"
print x.getMin()
print "top"
print x.top()
print "pop"
print x.pop()
print "min"
print x.getMin()
print "top"
print x.top()
print "pop"
print x.pop()
print "min"
print x.getMin()
print "top"
print x.top()
print "pop"
print x.pop()
print "min"
print x.getMin()
print "top"
print x.top()
print "pop"
print x.pop()
print "min"
print x.getMin()
print "top"
print x.top()
print "pop"
print x.pop()
print "min"
print x.getMin()
print "top"
print x.top()
print "pop"
print x.pop()
