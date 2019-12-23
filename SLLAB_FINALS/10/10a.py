from functools import reduce

li=[1,2,3,4,5,6]
print(li)
newli=[x*3 for x in li]
print(newli)

sum=reduce(lambda x,y:x+y,li)
print("Sum of original list",sum)


sum=reduce(lambda x,y:x+y,newli)
print("Sum of new list",sum)