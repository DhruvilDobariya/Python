n = int(input("How many element you have?")) 

a = [] 
for i in range(0,n):
     a.append(int(input("Enter an element no.{} : ".format(i+1))))

y = int(input("Enter an element which you want to check, it element is exist in list or not : "))

for i in range(0,n):
    if a[i] == y:
        print("{} is exist in list.".format(y))
        break
else:
    print("{} is not exist in list.".format(y))