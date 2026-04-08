rows = (int(input("please enter the total number of rows :")))
print("mirrored right triangled star pattern")
for i in range(1, rows + 1):
    for j in range(1 , rows + 1):
        if j <= rows - i:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()