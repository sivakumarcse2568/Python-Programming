#1. Positive, Negative, or Zero
n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

#2. Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

#3. Multiplication Table
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "*", i, "=", n * i)

#4. Leap Year
year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#5. Student Passed or Failed
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

#6. Keep Asking for Password
password = ""

while password != "1234":
    password = input("Enter password: ")

print("Correct password")

#7. First 10 Fibonacci Numbers
a = 0
b = 1

for i in range(10):
    print(a)
    c = a + b
    a = b
    b = c

#8. Print 1–20, Skip Multiples of 3
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

#9. Factorial Using Loop
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(fact)

