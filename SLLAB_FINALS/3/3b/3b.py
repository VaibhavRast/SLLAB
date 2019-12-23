import sys
import os
from functools import reduce

if(len(sys.argv)!=2):
    print("Invalid format")
    sys.exit()

if(not(os.path.exists(sys.argv[1]))):
    print("File not found")
    sys.exit()

if(sys.argv[1].split('.')[-1]!='txt'):
    print("Invalid file format")
    sys.exit()

dict={}
wordLi=[]

file=open(sys.argv[1],"r")

for line in file:
    for word in line.split():
        dict[word]=dict.get(word,0)+1;

print(dict)

sl=[]
sl=sorted(dict.items(),key= lambda x:x[1],reverse=True)
print(sl[:10])


for i,j in sl[:10]:
    wordLi.append(len(i))

print(wordLi)

sum=reduce(lambda x,y: x+y,wordLi)
print("Avg Length:",sum/len(wordLi))

print([x*x for x in wordLi if x%2!=0])