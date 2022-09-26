# Program 16.4:

n = int(input("Enter a number : "))
number = 1
for i in range(0, n):
    for j in range(0, i + 1):
        print(number, end=' ')
        number += 1
    print(" ")