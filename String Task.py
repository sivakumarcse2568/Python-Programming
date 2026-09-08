#1. Count vowels and consonants in a string
s = input("Enter a string: ")
vowels = 0
consonants = 0

for ch in s:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)

# 2. Reverse a string without using slicing
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed string:", rev)

#3. Check if a string is a palindrome
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")

#4. Count how many times a particular word appears in a sentence
sentence = input("Enter a sentence: ")
word = input("Enter the word to count: ")
words = sentence.split()
count = 0
for w in words:
    if w == word:
        count += 1
print("Count:", count)

#5. Find the longest word in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)

#6. Replace spaces in a string with hyphens
s = input("Enter a string: ")
result = ""
for ch in s:
    if ch == " ":
        result += "-"
    else:
        result += ch
print("Result:", result)

#7. Count digits, letters, and special characters
s = input("Enter a string: ")
letters = 0
digits = 0
special = 0
for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1
print("Letters:", letters)
print("Digits:", digits)
print("Special characters:", special)
