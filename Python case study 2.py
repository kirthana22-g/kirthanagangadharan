CASE STUDY 2

#Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
num1=20
num2=30
if num1*num2<=1000:
    print(num1*num2)
else:
    print(num1+num2)
600

num1=20
num2=300
if num1*num2<=1000:
    print(num1*num2)
else:
    print(num1+num2)
320

#Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
previous_num = 0
for i in range(10):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", previous_num + i)
    previous_num = i
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7
Current Number 5 Previous Number  4  Sum:  9
Current Number 6 Previous Number  5  Sum:  11
Current Number 7 Previous Number  6  Sum:  13
Current Number 8 Previous Number  7  Sum:  15
Current Number 9 Previous Number  8  Sum:  17

#Write a Python code to accept a string from the user and display characters present at an even index number.
a=input("enter a string:")
print(a[::2])
enter a string:pynative
Pntv

#Write a Python code to remove characters from a string from 0 to n and return a new string.
a=input("enter a string:")
n=int(input("enter a number:"))
print(a[n:])
enter a string:pynative
enter a number:3
ative

#Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
num1=[10,20,30,40,10]
if num1[0]==num1[4]:
    print("True")
else:
    print("False")
True

num1=[10,20,30,40,1]
if num1[0]==num1[4]:
    print("True")
else:
    print("False")
False

#Write a Python code to display numbers from a list divisible by 5
num=[10,20,33,46,55]
for i in num:
  if i%5==0:
    print(i)
10
20
55

#Write a Python code to find how often the substring “Emma” appears in the given string.
a = "Emma is good developer. Emma is a writer"
print(a.count("Emma"))
2

#pattern numbers
for i in range(5):
  for j in range(i):
    print(i,end=" ")
  print(i*1)
0
1 1
2 2 2
3 3 3 3
4 4 4 4 4
5 5 5 5 5 5


#Write a Python code to check if the given number is palindrome. A palindrome number is a number that is the same after reverse.
num = int(input("Enter a value:"))
temp = num
rev = 0
while(num > 0):
    dig = num % 10
    revrev = rev * 10 + dig
    numnum = num // 10
if(temp == rev):
    print("This value is a palindrome number!")
else:
    print("This value is not a palindrome number!")
Enter a value:121
This value is a palindrome number!


#Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []
for num in list1:
    if num % 2 != 0:
        list3.append(num)
for num in list2:
    if num % 2 == 0:
        list3.append(num)
[25, 35, 40]
[25, 35, 40]
[25, 35, 40, 60]
[25, 35, 40, 60]
[25, 35, 40, 60, 90]

#Get each digit from a number in the reverse order.
#For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
num = 7536
while num > 0:
    digit = num % 10
    num //= 10
    print(digit, end=" ")
6 3 5 7 


#Print multiplication table from 1 to 10
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()
1 2 3 4 5 6 7 8 9 10 
2 4 6 8 10 12 14 16 18 20 
3 6 9 12 15 18 21 24 27 30 
4 8 12 16 20 24 28 32 36 40 
5 10 15 20 25 30 35 40 45 50 
6 12 18 24 30 36 42 48 54 60 
7 14 21 28 35 42 49 56 63 70 
8 16 24 32 40 48 56 64 72 80 
9 18 27 36 45 54 63 72 81 90 
10 20 30 40 50 60 70 80 90 100 

#Print a downward half-pyramid pattern of stars
for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")
* * * * *  
* * * *  
* * *  
* *  
*  

#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
def exponent(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * exponent(base, exp - 1))
print(exponent(2, 5))
print(exponent(5,2))
32
25
CASE STUDY 2

#Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
num1=20
num2=30
if num1*num2<=1000:
    print(num1*num2)
else:
    print(num1+num2)
600

num1=20
num2=300
if num1*num2<=1000:
    print(num1*num2)
else:
    print(num1+num2)
320

#Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
previous_num = 0
for i in range(10):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", previous_num + i)
    previous_num = i
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7
Current Number 5 Previous Number  4  Sum:  9
Current Number 6 Previous Number  5  Sum:  11
Current Number 7 Previous Number  6  Sum:  13
Current Number 8 Previous Number  7  Sum:  15
Current Number 9 Previous Number  8  Sum:  17

#Write a Python code to accept a string from the user and display characters present at an even index number.
a=input("enter a string:")
print(a[::2])
enter a string:pynative
Pntv

#Write a Python code to remove characters from a string from 0 to n and return a new string.
a=input("enter a string:")
n=int(input("enter a number:"))
print(a[n:])
enter a string:pynative
enter a number:3
ative

#Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
num1=[10,20,30,40,10]
if num1[0]==num1[4]:
    print("True")
else:
    print("False")
True

num1=[10,20,30,40,1]
if num1[0]==num1[4]:
    print("True")
else:
    print("False")
False

#Write a Python code to display numbers from a list divisible by 5
num=[10,20,33,46,55]
for i in num:
  if i%5==0:
    print(i)
10
20
55

#Write a Python code to find how often the substring “Emma” appears in the given string.
a = "Emma is good developer. Emma is a writer"
print(a.count("Emma"))
2

#pattern numbers
for i in range(5):
  for j in range(i):
    print(i,end=" ")
  print(i*1)
0
1 1
2 2 2
3 3 3 3
4 4 4 4 4
5 5 5 5 5 5


#Write a Python code to check if the given number is palindrome. A palindrome number is a number that is the same after reverse.
num = int(input("Enter a value:"))
temp = num
rev = 0
while(num > 0):
    dig = num % 10
    revrev = rev * 10 + dig
    numnum = num // 10
if(temp == rev):
    print("This value is a palindrome number!")
else:
    print("This value is not a palindrome number!")
Enter a value:121
This value is a palindrome number!


#Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []
for num in list1:
    if num % 2 != 0:
        list3.append(num)
for num in list2:
    if num % 2 == 0:
        list3.append(num)
[25, 35, 40]
[25, 35, 40]
[25, 35, 40, 60]
[25, 35, 40, 60]
[25, 35, 40, 60, 90]

#Get each digit from a number in the reverse order.
#For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
num = 7536
while num > 0:
    digit = num % 10
    num //= 10
    print(digit, end=" ")
6 3 5 7 


#Print multiplication table from 1 to 10

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()
1 2 3 4 5 6 7 8 9 10 
2 4 6 8 10 12 14 16 18 20 
3 6 9 12 15 18 21 24 27 30 
4 8 12 16 20 24 28 32 36 40 
5 10 15 20 25 30 35 40 45 50 
6 12 18 24 30 36 42 48 54 60 
7 14 21 28 35 42 49 56 63 70 
8 16 24 32 40 48 56 64 72 80 
9 18 27 36 45 54 63 72 81 90 
10 20 30 40 50 60 70 80 90 100 

#Print a downward half-pyramid pattern of stars
for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")
* * * * *  
* * * *  
* * *  
* *  
*  

#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
def exponent(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * exponent(base, exp - 1))
print(exponent(2, 5))
print(exponent(5,2))
32
25
