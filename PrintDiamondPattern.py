# Python Program to print the pattern

#Read input value from user and store in count variable
count = int(input("Enter input value"))
for i in range(0, count):
    for j in range(0, i+1):
         print("* ",end="")
    print()

for i in range(0, count):
    for j in range(count-1, i, -1):
        print("*", end=" ")
    print()
