atomic={"H":"Hydrogen","He":"Helium","Na":"Sodium"}

#Add existing
sym=input("Enter existing symbol ")
name=input("Enter name ")
atomic[sym]=name
print(atomic)

#add unique
sym=input("Enter symbol ")
name=input("Enter name ")
atomic[sym]=name
print(atomic)

#no of elements
print("Length:",len(atomic))

#search element
sym=input("Enter symbol to be searched ")

if (sym in atomic):
	print("Found",atomic[sym])

else :
	print("Not Found")