n = int(input("How many element you have?")) 

a = [] 
for i in range(0,n):
     a.append(int(input("Enter an element no.{} : ".format(i+1))))

for i in range(0,n):
    if a[i] < a[i+1]:
        print("This list is not monotonic.")
        break
else:
    print("This list is monotonic.")