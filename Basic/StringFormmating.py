a = "I am Dhruvil Dobariya, I become a .Net Developer."

print(a[5]) # Return charecter of which is exist on arg index.
'''
We can pass three argument at a time.
For Ex : One argument : a[arg1] => here arg1 = strating index
         Two argument : a[arg1:arg2] => here arg2 = ending index
         Three argument : a[arg1:arg2:arg3] => here arg3 = number of steps from starting index
'''

print(a[5:21]) # Return string from starting index(arg1) to ending index-1(arg-1).
print(a[:21]) # If we don't take arg1, then it take by default 0.

print(a[5:21:2]) # Return string from starting index(arg1) to ending index-1(arg-1) with arg3 stap jump from starting index.
# arg3 is by default 1.

print(a[5::2]) # If we don't take arg2, then it take by default 0.
print(a[:21:2])
print(a[::2])

b = 5

print("This is number : {}".format(b))

c = "{} institute of {} and {}"
print(c.format("Darshan","Engineering","Technology"))

c = "{0} institute of {2} and {1}"
print(c.format("Darshan","Engineering","Technology"))

c = "{firstinstitute} institute of {collegename} and {secondinstitute}"
print(c.format(collegename="Darshan",firstinstitute="Engineering",secondinstitute="Technology"))

print("This is number : %s" % (b))

print("This is a number : ", b , "and this is also", b)