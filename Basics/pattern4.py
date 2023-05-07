a=int(input("Enter the number of rows: "))

for i in range(a):
    for x in range(i+1):
        print(x+1,"  ", end="")
    print("\n")