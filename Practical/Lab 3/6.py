n = int(input("How many element you have?")) 

a = [] 
for i in range(0,n):
     a.append(input("Enter an element no.{} : ".format(i+1)))

occurrence = input("Enter an occurrence which you want remove : ")
N = int(input("Enter a number of occurrence which you want remove : "))

occurrenceIndex = []
for i in range(0,n):
    if a[i] == occurrence:
        occurrenceIndex.append(i)

N = occurrenceIndex[N-1]
a.remove(a[N])

print(a)