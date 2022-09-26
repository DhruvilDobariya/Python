# Program 14:

bnum = list(input("Enter a binary number : "))
value = 0

for i in range(len(bnum)):
	digit = bnum.pop()
	if digit == '1':
		value = value + pow(2, i)
print("Decimal value is : {}".format(value))