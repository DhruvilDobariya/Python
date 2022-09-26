n = int(input("How many element you have?"))
sumOfList = 0
b = []
for a in range(0,n):
    b.append(int(input("Enter an element no.{} : ".format(a+1))))
    sumOfList += b[a]
    
print("Your answer is : {}".format(sumOfList))
# Here we can also use sum() function like : sumOfList = sum(b)