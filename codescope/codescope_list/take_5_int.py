l=[]

for x in range(0,4,1):
    a=int(input("Enter an integer :"))
    l.append(a)

print("\nNow check if a particular integer is present in the list or not")

b=int(input("\nEnter another integer :"))
count=0

for i in range(0,4,1):
    if(l[i]==b):
        count=count+1

if(count!=0):
    print("\n",b," is present in the list\n")
else:
    print("\n",b," is not present in the list")