l=[]

a=int(input("Enter the number of integers: "))
for x in range(0,a,1):
    b=int(input("Enter the value: "))
    l.append(b)

small=l[0]
large=l[0]

for x in range (a):
    if(small>l[x]):
        temp=l[x]
        l[x]=small
        small=temp

for x in range (a):
    if(large<l[x]):
        temp=l[x]
        l[x]=large
        large=temp

print("Largest element is: ",large)
print("Smallest element is: ",small)