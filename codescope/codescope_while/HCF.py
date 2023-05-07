a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))

c=0

if(a>b):
    c=b
else:
    c=a

for x in range(c,1,-1):
    if(a%x==0 and b%x==0):
        if(x!=1):
            print("HCF is :",x)
            break
        else:
            print("The numbers are co-prime")
    
        


