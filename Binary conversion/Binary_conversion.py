n = int(input("Enter the number"))
result = " "
while n > 0:
    result = str(n & 1) + result
    n>>=1
print(result)