#1. Find the largest and smallest number in a list
numbers = [10, 25, 5, 40, 15]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)

#2. Remove duplicates from a list
numbers = [10, 20, 10, 30, 20, 40]
new_list = []
for num in numbers:
    if num not in new_list:
        new_list.append(num)
print("List:", new_list)

#3. Calculate the sum and average
numbers = [10, 20, 30, 40, 50]
sum = 0
for num in numbers:
    sum = sum + num
average = sum / len(numbers)
print("Sum:", sum)
print("Average:", average)

#4. Sort a list in ascending and descending order
numbers = [40, 10, 30, 20, 50]
numbers.sort()
print("Ascending:", numbers)
numbers.reverse()
print("Descending:", numbers)

#5. Create a list of cubes for numbers 1–10
cubes = []
for num in range(1, 11):
    cube = num ** 3
    cubes.append(cube)
print("Cubes:", cubes)

#6. Find the second largest number
numbers = [10, 40, 20, 50, 30]
numbers.sort()
print("Second largest:", numbers[-2])

#77. Merge two lists into one
