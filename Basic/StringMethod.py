a = "I am Dhruvil Dobariya, I become a .net Developer"
print(len(a)) # Here len() is a function, which is return length.
# Note : len() is not a part of string class, but it is a genaral purpose function.
'''
=> Function vs Method
=> If we want to access Function then, we can't required object.
=> But If we want to access Method then, we must required object.
=> For Ex : Function : len(args)
=> For Ex : Method : a.index(args) -> here 'a' is a object.
'''
# Methods of string class:
# In args we use both charecter and string.
# All String Methods is immutable.
print(a.count('i')) # Return count of arg

print(a.title()) # Return string in title case
print(a.lower()) # Return string in lower case
print(a.upper()) # return string in upper case

# Evrey Method which is used to verify particular think, It's always return boolean(True or False).
print(a.istitle()) 
print(a.islower())
print(a.isupper())

print(a.find('D')) # Return index number of arg which is first from 0th index.
print(a.rfind('D')) # Return index number of arg which is last from 0th index.
# If above two methods can't find char or string then return -1. 
#print(a.find('z'))
#print(a.rfind('z'))
#But below teo function can't find char or string then throw an exeption.
print(a.index('D'))
print(a.index('D'))
#print(a.index('z'))
#print(a.rindex('z'))

print(a.replace(".net",".Net")) # Return string with replacement of arg1 on arg2.

print(a.isalpha()) # Check alphabet string or not.
print(a.isalnum()) # Check alphabet or numeric or not.
print(a.isdecimal()) # Check it's decimal or not. (Allow unicode)
print(a.isdigit()) # Check is digit or not. (Not allow unicode)

y = "abcde1234"

print(y.isalpha())
print(y.isalnum())
print(y.isdecimal())
print(y.isdigit())

b = "       Dhruvil Dobariya       "

print(b)
print(b.strip()) # Remove whitespaces.
print(b.rstrip()) # Remove whitespaces only right side.
print(b.lstrip()) # Remove whitespaces only left side.