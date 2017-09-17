a, b  = input().split(" ")
a = int(a)
b = int(b)
c  = a -b

if c % 10 == 9:
    print(c -1)

else:
    print(c + 1)