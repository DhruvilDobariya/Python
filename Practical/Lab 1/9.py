# Program 9:

n = int(input("Enter a number : "))
a = 0
b = 1
sum = 0
print("Fibonacci series is : ", end = " ")
while(sum <= n):
     print(sum, end = " ")
     a = b
     b = sum
     sum = a + b