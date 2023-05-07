a=int(input("Enter a number :"))

print("\nFibonnaci using function\n")
#def fib(a):
    
      
    
#fib(a)

num1=0
num2=1
    
print(num1," ",num2,end=" ")
for x  in range(1,a+1):
      a=num1+num2
      num1=num2
      num2=a
      print(" ",a,end=" ")
   