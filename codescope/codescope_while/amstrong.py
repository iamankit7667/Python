#Write all Armstrong numbers between 100 to 500.
#isnt working


b=0
x=100
rem=0
num=0

print(x)

while(x<=500):
    b=x
    while(x>0):
       rem=x%10
       num=num+rem*rem*rem
       x=x//10

    if(b==num):
       print(b," is an amstrong number")
    else:
       print(b," is not an amstrong number")
    
    x=x+1
