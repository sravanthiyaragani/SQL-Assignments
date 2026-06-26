# 1. Check whether the number is Positive or Not

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
else:
    print("Not a Positive Number")




# 2. Check whether the character is Uppercase or Lowercase
# (Without using built-in functions)

ch = input("\nEnter a character: ")

if ch >= 'A' and ch <= 'Z':
    print("Uppercase Letter")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase Letter")
else:
    print("Not an Alphabet")




# 3. Pass or Fail (6 Subjects)

print("\nEnter Marks of 6 Subjects")

s1 = int(input("Subject 1: "))
s2 = int(input("Subject 2: "))
s3 = int(input("Subject 3: "))
s4 = int(input("Subject 4: "))
s5 = int(input("Subject 5: "))
s6 = int(input("Subject 6: "))

if s1 >= 35 and s2 >= 35 and s3 >= 35 and s4 >= 35 and s5 >= 35 and s6 >= 35:
    print("Result : PASS")
else:
    print("Result : FAIL")