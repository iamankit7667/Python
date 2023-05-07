a=int(input("Enter a number: "))
x=2

while(x>1):
    if(a%x==0 and x!=a):
        print(x)
    x=x+1