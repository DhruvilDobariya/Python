# Program 12:

n = int(input("Enter a number : "))

ans = 0
for i in range(1, n+1):
    ans += (i*i)

print("Sum of square of first {} natural number is = {}".format(n,ans))