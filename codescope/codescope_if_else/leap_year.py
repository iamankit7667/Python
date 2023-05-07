a=int(input("Enter the year :"))

if( a%4==0 and a%100!=0):
    print( a," is a leap year")
elif( a%4==0 and a%100==0 ):
    if(a%400==0):
        print(a," is a leap year")
    else:
        print(a," is not a leap year")
else:
    print(a," is not a leap year")
