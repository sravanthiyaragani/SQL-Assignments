print("1. Square Pattern")
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

print("\n2. Right Triangle")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n3. Number Triangle")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n4. Repeated Number Triangle")
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()


print("\n5. Alphabet Triangle")
for i in range(5):
    ch = 'A'
    for j in range(i + 1):
        print(chr(ord(ch) + j), end=" ")
    print()


print("\n6. Inverted Star Triangle")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


print("\n7. Inverted Number Triangle")
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


print("\n8. Continuous Number Pattern")
num = 1

for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


print("\n9. Right-Aligned Star Triangle")
for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(i):
        print("* ", end="")
    print()


print("\n10. Pyramid Pattern")
for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()