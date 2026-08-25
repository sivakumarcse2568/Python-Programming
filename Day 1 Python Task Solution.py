#1.Write a program to check whether a student is eligible for admission based on marks in three subjects using comparison and logical operators.
  maths = int(input("Enter Maths mark: "))
  physics = int(input("Enter Physics mark: "))
  chemistry = int(input("Enter Chemistry mark: "))
  
  if (maths>=50 and physics>=50 and chemistry>=50):
      print("Student is eligible for admission")
  else:
      print("Student is not eligible for admission")

#2.Write a program to calculate an employee's bonus based on salary, experience, and performance rating using arithmetic, comparison, and logical operators.

  salary = int(input("Enter salary: "))
  experience = int(input("Enter experience: "))
  rating = int(input("Enter performance rating: "))
  
  if (experience>=5 and rating>=4):
      bonus=(salary*20)/100
  elif (experience>=3 and rating>=3):
      bonus=(salary*10)/100
  else:
      bonus=(salary*5)/100
  
  print("Bonus =",bonus)

#3.Write a program to calculate the final shopping amount after applying discounts based on purchase amount, membership status, and festival offer.
  amount = int(input("Enter purchase amount: "))
  member = input("Are you a member? yes/no: ")
  festival = input("Is festival offer available? yes/no: ")
  if (amount>=5000 and member=="yes" and festival=="yes"):
      discount=30
  elif (amount>=3000 and member=="yes"):
      discount=20
  elif (amount>=2000 and festival=="yes"):
      discount=15
  else:
      discount=5
  
  discount_amount = (amount*discount)/100
  final_amount = amount-discount_amount
  
  print("Discount =",discount_amount)
print("Final amount =",final_amount)

#4.Write a program to validate a username, password, and OTP using comparison and logical operators.
  username = input("Enter username: ")
  password = input("Enter password: ")
  otp = int(input("Enter OTP: "))
  
  if(username=="admin" and password=="12345" and otp==1234):
      print("Login successful")
  else:
      print("Invalid username, password or OTP")

#5.Write a program to check whether an ATM withdrawal is valid based on account balance, withdrawal amount, minimum balance, and multiples of ₹100.
  balance = int(input("Enter account balance: "))
  amount = int(input("Enter withdrawal amount: "))
  minimum = int(input("Enter minimum balance: "))
  
  if(amount%100==0 and amount<=balance-minimum):
      print("Withdrawal is valid")
  else:
      print("Withdrawal is not valid")

#6.Given two lists, check whether they have the same values and whether they refer to the same object using equality and identity operators.

#7.Write a program to check whether a particular word exists in a sentence and whether a particular item exists in a list using membership operators.

#8.Write a program to validate whether a number is within a given range and divisible by either 3 or 5, but not both.
  number=int(input("Enter a number: "))
  start=int(input("Enter starting range: "))
  end=int(input("Enter ending range: "))
  
  if(number>=start and number<=end and (number%3==0 or number%5==0) and not (number%3==0 and number%5==0)):
      print("Number is valid")
  else:
      print("Number is not valid")

'''9.Create a user permission system using bitwise operators where:
Read = 1
Write = 2
Execute = 4
Check which permissions a user has.
10.Create a feature toggle system using bitwise operators where:
Dark Mode = 1
Notifications = 2
Location = 4
Camera = 8
Enable, disable, toggle, and check features.'''
