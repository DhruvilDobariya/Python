a = int(input("Enter a first number : "))
b = int(input("Enter a second number : "))
c = int(input("Enter a third number : "))
if a > b and a > c:
    print("{} is grater then {} and {}.".format(a,b,c))
elif b > a and b > c:
    print("{} is grater then {} and {}.".format(b,a,c))
elif c > a and c > b:
    print("{} is grater then {} and {}.".format(c,a,b))
elif a == b and a > c:
    print("{} and {} is grater then {}.".format(a,b,c))
elif b == c and b > a:
    print("{} and {} is grater then {}.".format(b,c,a))
elif c == a and c > b:
    print("{} and {} is grater then {}.".format(c,a,c))
else:
    print("{} and {} and {} is equle.".format(a,b,c))
