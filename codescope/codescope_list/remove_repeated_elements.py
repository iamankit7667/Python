l=[1,2,3,2,1,3,12,12,32]
k=[]


for i in range(len(l)):
    count=0
    for j in range(len(l)):
        if(i==j):
            continue
        if(l[i]==l[j]):
            count=count+1
    if(count==0):
        k.append(l[i])

print(k)