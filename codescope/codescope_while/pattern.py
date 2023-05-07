i=5
j=0
x=0

while(i>0):

    i=i-1
    j=2*i-1
    x=i-1

    while(x<4):
       print(" ",end=" ")
       x=x+1

    while(j>0):
      if(j%2!=0):
         print("1",end=" ")
      else:
         print("0",end=" ")
      j=j-1

    print("\n")
      