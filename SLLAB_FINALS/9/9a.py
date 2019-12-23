class Student():
	"""docstring for Student"""
	def __init__(self):
		self.name=""
		self.age=""
		self.marks=[]

	def display(self):
		print("Name:",self.name)
		print("Age",self.age)
		print("Marks",self.marks)

	def accept(self):
		self.name=input("Enter name:")
		self.age=int(input("Enter age:"))
		for i in range(3):
			self.marks.append(int(input("Enter marks in subject")))


stud1obj=Student()
stud2obj=Student()

stud1obj.accept()
stud1obj.display()

stud2obj.accept()
stud2obj.display()


		