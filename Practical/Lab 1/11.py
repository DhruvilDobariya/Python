# Program 11:

n = int(input("Enter number : "))
temp = n
rev = 0

while(n>0):
    dig = n%10
    rev = rev*10+dig
    n = n//10
if(temp == rev):
    print("{} is a palindrome number.".format(temp))
else:
    print("{} is not a palindrome number.".format(temp))