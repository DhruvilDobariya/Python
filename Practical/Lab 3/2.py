n = int(input("How many element you have?"))

b = []
for i in range(0,n):
    b.append(int(input("Enter an element no.{} : ".format(i+1))))
    
for i in range(0,n-1):
    if b[i] > b[i+1]:
        b[i],b[i+1] = b[i+1],b[i]

print("The lagest element of a list is : {}".format(b[-1]))