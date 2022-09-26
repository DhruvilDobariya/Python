n = int(input("How many element you have?")) 

a = [] 
for i in range(0,n):
     a.append(int(input("Enter an element no.{} : ".format(i+1))))

y = a[0 : len(a)//2]
a = a[len(a)//2 : len(a)]
a.extend(y)
print(a)