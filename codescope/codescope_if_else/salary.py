a=int(input("Enter your years of service :"))
b=int(input("Enter your salary :"))

bonus=1

if(a>5):
    bonus=b*0.05
    print("Your bonus is :", int(bonus))
else:
    print("Your won't get bonus")