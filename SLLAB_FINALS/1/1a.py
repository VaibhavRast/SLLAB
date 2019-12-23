li=[]

n=int(input("Enter no of elements to be inserted:"))
for i in range(0,n):
	li.append(int(input("Enter:")))

print(li)
print("Max:",max(li)," Min:",min(li))

ele=int(input("Enter element to be inserted:"))
li.append(ele)
print(li)


ele=int(input("Enter element to be deleted:"))
li.remove(ele)
print(li)

ele=int(input("Enter element to be searched:"))

if ele in li:
	print("Found ")
else:
	print("Not Found")

