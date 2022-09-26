# Program 6:

n = int(input("Enter a number : "))

flag = True
for a in range(2,n):
    if n%a == 0:
        flag = False
        break
if flag:
    print("{} is prime number.".format(n))
else:
    print("{} is not prime number.".format(n))
