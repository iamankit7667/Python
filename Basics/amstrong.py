x=int(input("Enter the number :"))
num=0
rem=0

b=x
while(x>0):
    rem=x%10
    num=num+rem*rem*rem
    x=x//10

if(b==num):
    print(b," is an amstrong number")
else:
    print(b," is not an amstrong number")