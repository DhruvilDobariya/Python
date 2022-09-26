# Program 8:

import math
 
n = int(input("Enter the number : "))

maxPrimeFactor = 0

while n % 2 == 0:
	maxPrimeFactor = 2
	n = n/2	

for i in range(3, int(math.sqrt(n)) + 1, 2):
	while n % i == 0:
		maxPrimeFactor = i
		n = n / i
if n > 2:
	maxPrimeFactor = n
		
print("Largest prime factor is : ",int(maxPrimeFactor))