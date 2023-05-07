a=int(input("Enter a number :"))
x=a
b=0

while(x>=2):
    if(a%x==0):
        b=x-1
        while(b>1):
            if(x%b!=0):
                print(x," is a prime factor ")
            b=b-1
    x=x-1
                