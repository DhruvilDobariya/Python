# Program 7:

start = int(input("Enter start range: "))  
end = int(input("Enter end range: "))  
  
for n in range(start,end + 1):  
   if n > 1:  
       for i in range(2,n):  
           if (n % i) == 0:  
               break  
       else:  
           print(n,end=" ")