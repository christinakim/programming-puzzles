"""
stats object 
insert median
mean
O(1) memory 
int between 0/1000
"""

class stats(object):
	def __int__(self):
		self.count = 0
		self.sum = 0
		self.dict = {}

	def insert(self, n):
		self.sum = self.sum + n
		self.count = self.count + 1
		if n in self.dict:
			self.dict[n] = self.dict.get(n)+1
		else:
			self.dict[n] = 1

	def mean():
		return float(self.sum/self.count)

	def median(self):
		median_index = self.count
		for i in range(1000):
			if self.dict[i]