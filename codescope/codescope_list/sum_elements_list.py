l=[]

a=int(input("Enter the number of integers: "))
for x in range(0,a,1):
    b=int(input("Enter the value: "))
    l.append(b)

sum=0
for x in range(a):
    sum=sum+l[x]

print(sum)