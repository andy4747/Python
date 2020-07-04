string='abcd'
itr=iter(string)
print(itr)
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())

class Reverse:
	"""Iterator for looping over a squence backwards"""
	def __init__(self,data):
		self.data=data
		self.index=len(data)

	def __iter__(self):
		return self

	def __next__(self):
		if self.index==0:
			raise StopIteration
		self.index-=1
		return self.data[self.index]

r1=Reverse("spam")
for i in r1:
	print(i)


class TenNumbers:
	def __init__(self):
		self.num=1

	def __iter__(self):
		return self

	def __next__(self):
		if self.num>10:
			raise StopIteration
		val=self.num
		self.num+=1
		return val

v=TenNumbers()
for i in v:
	print(i)


class EvenIndex:
	def __init__(self,data):
		self.data=data
		self.index=0

	def __iter__(self):
		return self

	def __next__(self):
		if self.index>=len(self.data):
			raise StopIteration
		result=self.data[self.index]
		self.index+=2
		return result

value=EvenIndex([0,10,20,30,40,50,60,70,80,90])

for i in value:
	print(i)
