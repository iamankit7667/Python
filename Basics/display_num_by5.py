a=[1,5,10,23,34,30,20,55,66]
l=len(a)
b=[]
x=0
for x in range(0,l):
    if a[x]%5==0:
        print(a[x])
        b.append(a[x])

print(b)
