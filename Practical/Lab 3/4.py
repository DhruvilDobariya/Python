n = int(input("How many element you have?")) 

a = [] 
for i in range(0,n):
     a.append(int(input("Enter an element no.{} : ".format(i+1))))

a[0],a[-1] = a[-1],a[0]
print(a)