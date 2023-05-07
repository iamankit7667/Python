a=int(input("Enter a number: "))
x=2
b=2

while(x>1):
    if(a%x==0 and x!=a):
        print(x)
        b=x

        while(b>0):
            if(x%b==0 and b<x):
                print("Not a prime factor")
                
            if(b==x):
                print(x," is a prime factor")
            b=b+1

    x=x+1
