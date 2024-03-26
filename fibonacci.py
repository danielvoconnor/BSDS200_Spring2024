n = 5
a = 1
b = 1
print(a)
print(b)
for i in range(1, n-1):
    x = a + b
    print(x)
    a = b
    b = x
