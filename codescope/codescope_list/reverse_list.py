l=[]
k=[]

a=int(input("Enter the number of integers: "))
for x in range(0,a,1):
    b=int(input("Enter the value: "))
    l.append(b)

for x in range(a-1,-1,-1):
    k.append(l[x])

print(l,"\n")
print(k)

print(l=k)