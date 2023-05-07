x=int(input("Enter a number: "))
b=2

while(b>1):
    if(x%b==0 and b!=x):
        print("Not a prime number")
        break
    if(b==x):
        print(x," is a prime number")
    b=b+1