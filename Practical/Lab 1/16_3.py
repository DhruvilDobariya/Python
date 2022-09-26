# Program 16.3:

n = int(input("Enter a number : "))

i = 0
while i <= n - 1:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= n - 1:
        print('#', end=' ')
        k += 1
    print()
    i += 2

i = n - 2
while i >= 0:
    j = 0
    while j < i-1:
        print('', end=' ')
        j += 1
    k = i
    while k <= n:
        print('#', end=' ')
        k += 1
    print('')
    i -= 2