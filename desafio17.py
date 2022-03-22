x, y, z = input().split()

x = int(x)
y = int(y)
z = int(z)

if x < y:
    if x < z:
        if y < z:
            print(x)
            print(y)
            print(z)
        else:
            print(x)
            print(z)
            print(y)
    else:
        print(z)
        print(x)
        print(y)
else:
    if x < z:
        print(y)
        print(x)
        print(z)
    else:
        if y < z:
            print(y)
            print(z)
            print(x)
        else:
            print(z)
            print(y)
            print(x)

print()

print(x)
print(y)
print(z)
