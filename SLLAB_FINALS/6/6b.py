class Reverser:
	vowels=['a','e','i','o','u']
	sentence=""
	reverse=""

	def __init__(self, s):
		self.sentence=s
		self.reverse=" ".join(reversed(self.sentence.split()))

	def getRev(self):
		return self.reverse

	def vowelCount(self):
		return sum(s in self.vowels for s in self.sentence.lower())


items=[]
sl=[]
for i in range(3):
	s=input("Enter the sentence/phrase:")
	revobj=Reverser(s)
	items.append(revobj)
	print(revobj.getRev())


for i in sorted(items,key=lambda i:i.vowelCount(),reverse=True):
	print(i.getRev()," VowelCount:",i.vowelCount())
