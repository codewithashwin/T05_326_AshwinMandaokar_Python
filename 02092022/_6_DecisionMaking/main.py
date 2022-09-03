"""
Conditional Statements
"""

"""
what is conditional statements? why we use conditional statements or decision-making?
using conditional statement we change the flow of the program. if the conditions is True
perform this block of code else perform that block of code.(anticipation of code)
conditional statement generally use it for taking decision based on conditions.

Decision making is anticipation of conditions occurring while execution of the program and specifying actions taken
according to the conditions.
Decision structures evaluate multiple expressions which produce True or False as outcome. You need to determine which 
action to take and which statements to execute if outcome is TRUE or FALSE otherwise.

syntax:
if something is True:
    Do something
else:
    Do something

There are two types of value
0 = value
None = not applicable (the absence of value)

types of conditionals statement
1. if statement = if you have just only one condition for check, just use single statement.
2. if else statement = if you have more than one condition then use if else condition
3. if elif else : if you have more than two conditions then use if elif else
EX if some condition:
    Do something
elif some condition:
    Do something
else:
    Do something
    
    
4. nested if : condition inside condition
EX if condition:
        if condition:
            Do something
        else:
            Do something
    else:
        Do something


non-zero and not-None values as True, and if it is either
zero or None, then it is assumed as False value.

in if conditions we can use every type of operators.


"""
a = 19
if a == 10:
    print("Welcome to Hello World")

print("ok")

a = 10
if a >= 20:
    print("Condition is True")
else:
    if a >= 15:
        print("Checking second value")
    else:
        print("All Conditions are false")

"""
Requirements
1.Find grade of a student based on below requirement.
marks >= 80  => A+  , 60-79 => A,  50-60=> B, 40-50 => C,  Below 35 FAIL
"""
# Design
"""
step 1 : Ask for the user for marks
step 2 : check conditions 
step 3 : print the output based on conditions
"""

# Development
marks = int(input("Enter the student marks: "))

if marks > 0 and marks < 100:  # validations
    if marks >= 80:
        print("A+")
    elif marks >= 60 and marks < 80:
        print("A")
    elif marks >= 50 and marks <= 60:
        print("B")
    elif marks >= 40 and marks <= 50:
        print("c")
    elif marks > 35:
        print("PASS")
    else:
        print("FAIL")
else:
    print("Enter the valid number between 0 and 100")

#  2nd requirement
"""
2.Find maximum number below. Implement using if elif…..else logic
a=10,  b=30,  c=20 
"""

# analysis
"""
functional analysis:
1. start -->2. input -->3. check the number between each other -->4. if a > b and a >c : highest --> if b > a and b>c : highest
--> else c highest --> 5. exit
"""
# Design
"""
step 1. get the input
step2. compare numbers with each other
step3. print the highest number
"""

# Development
a = 50
b = 30
c = 90

if a > b and b > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

# 3rd requirement
"""
Check whether entered year is leap year or not.
a year, occurring once every four years, which has 366 days including 29 February as an intercalary day.
"""

# analysis / step
"""
1. start
2. year input
3. year % 4 == 0 --> True go to 4
4. year % 100 != 0 or year % 400 == 0: True
5. else: not a leap year
"""

year = int(input("Enter the year "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")

# 4th requirement
"""
5. Check an entered number is odd or even
if the number is divisible by 2 then its even number
"""
# analysis / design
"""
step 1. take input
step 2. check number if divisible by 2 its even else odd
step 3. exit
"""

number = int(input("Enter the number to check: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

"""
========================Treasure Island Game, use-case for if else statements=================================
"""

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Write your code below this line 👇
user_input = input('Where do you want to go? "left" or "right"?').lower()

if user_input == "right":
    print("You fell into a hole, 'GAME OVER.'")
else:
    user_input = input("There is a lake, what do you want to choose? 'swim' or 'wait'").lower()
    if user_input == "swim":
        print("Attacked By trout, GAME OVER.")
    else:
        user_input = input("There are 3 DOORS, Which door? 'Red', 'Blue', 'Green'.").lower()
        if user_input == "yellow":
            print("You Win!")
        else:
            print("GAME OVER.")

