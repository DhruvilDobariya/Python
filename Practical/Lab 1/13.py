# Program 13:

n = int(input("Enter a number : "))

ans = 0
for i in range(1, n+1):
    ans += (i*i*i)

print("Sum of cube of first {} natural number is = {}".format(n,ans))