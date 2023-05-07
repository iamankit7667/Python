L=[10,23,1,56,9,12]

for i in range (0,len(L)-1):
    for j in range (0,len(L)-1):
        if (L[j+1]<L[j]):
            temp =L[j+1]
            L[j+1]=L[j]
            L[j]=temp

print("Bubble sort")
print(L)
