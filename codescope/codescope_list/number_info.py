l=[]

def pos(x):
    if(x>0):
        print(x," is positive")

def neg(x):
    if(x<0):
        print(x," is negative")

def even(x):
    if(x%2==0):
        print(x," is even")

def odd(x):
    if(x%2!=0):
        print(x," is odd")

def zeros(x):
    a=x
    count=0
    while(x>0):
        if(x%10==0):
            count=count+1
            x=x//10
        else:
            break
    print("The number of zeros in",a,"is",count)

a=int(input("Enter the number of integers: "))
for x in range(0,a,1):
    b=int(input("Enter the value: "))
    l.append(b)

for x in range(0,a,1):
    print("\n")
    pos(l[x])
    neg(l[x])
    even(l[x])
    odd(l[x])
    zeros(l[x])
    print("\n")