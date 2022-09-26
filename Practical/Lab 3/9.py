n = int(input("How many element you have?")) 

a = [] 
for i in range(0,n):
     a.append(int(input("Enter an element no.{} : ".format(i+1))))

y = []
y.extend([(a[i]) for i in range(0,n) if a[i] > 0])
print(y)