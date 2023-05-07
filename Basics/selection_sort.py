l=[89,45,3,90,23,54]
a=len(l)

for i in range(0,a):
    for j in range(i+1,a):
        if(l[i]>l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp

print(l)