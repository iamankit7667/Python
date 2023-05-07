a = [1,2,3,4,5]
b = [a[len(a)-1]]+a[:len(a)-1]
print(a)
a = b
print(a)