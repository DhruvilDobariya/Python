# Program 15:

dnum = int(input("Enter a decimal number : "))
i = 0
bnum = []

while dnum!=0:
    rem = dnum%2
    bnum.insert(i, rem)
    i += 1 
    dnum = int(dnum/2)

i -= 1
print("Binary value is : ",end=" ")

while i>=0:
    print(end=str(bnum[i]))
    i -= 1