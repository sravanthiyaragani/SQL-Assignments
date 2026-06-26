num = int(input("Enter a number: "))

original = num
length = len(str(num))

print("Length of Number =", length)

total = 0

while num > 0:
    digit = num % 10
    print("Digit =", digit)

    power = digit ** length
    print(digit, "^", length, "=", power)

    total += power
    num = num // 10

print("Sum =", total)

if total == original:
    print(original, "is an Armstrong Number")
else:
    print(original, "is Not an Armstrong Number")