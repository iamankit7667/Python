t=(5,7,9)
l=list(t)
n=len(l)
s=-1

for z in range(n):
    s=s+1
    print("\n\n")
    for i in range(n):
        for x in range(n,i,-1):
           print(" ",end=" ")
        for y in range(2*i+1):
           print(l[s],end=" ")

        print("\n")