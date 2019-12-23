class Rectangle:

	def __init__(self,a,b):
		self.len=a
		self.breadth=b

	def area(self):
		return self.len*self.breadth

recobj=Rectangle(10,4)
print("Area:",recobj.area())
