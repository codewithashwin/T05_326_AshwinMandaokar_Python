"""
Loops
"""

"""
what is loops?
ans = In computer programming, loop is a sequence of instructions that is continually repeated until a certain
condition is reached.
or
a group of code executed multiple times without writing it repeatedly.

Why we are using loops?
Sometimes our business logic required a repetition task that time we use loops for avoiding a repetitive code.
For ex print "Hello world" 5 times
for _ in range(5):
    print("hello world")

### Looping structure
# An application sometimes needs to perform some repetitive action like:
1. summing numbers
2. entering multiple data entries
3. prompting the user till the correct value entered

- Loops are similar to conditionals because they run on a True/False value
ex while True: or i <= 10
- Loops is continuously learning while the condition is True and terminates when it's false.
- Loops can be runs for a desired length(For loop) or until a flag terminates them(While loop).
-
-when a program repeatedly run a set of instructions it is referred to as loop, iteration or repetition structure.

Counter:
- a variable that is incremented or decremented each time a loop repeats.
- b can be used to control execution of the loop.(Loop control variable)
- c must be initialized before entering loops
"""

"""
Types of loops
1. While:
    while loops are known as indefinite or conditional loops, they keep iterating (do again and again and again) until
    certain conditions are met or False
    Syntax:
    while expression:
        statement  
2. For:
    for loop is a python loop which iterate a group of elements a specified number of times.
    Syntax:
    for <variable> in sequence:
        pass
    Ex 
    for letter in 'Python':
	    print('Current Letter :', letter)

3. Nested: 
    Python programming language allows us of loop inside another loop
    Syntax:
    for each in list1:
        for eah in list2:
            statements
        else:
            statement

    while expresion:
        while expression:
            statements
        statements

Else statement with loop
Python supports to have an else statement associated with a loop statement
•	If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating
 the list.
•	If the else statement is used with a while loop, the else statement is executed when the condition becomes false.

"""


# Examples
# """
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# example 1.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# """
#
# """
# Approach
# 1. use the nested loop
# 2. in second loop it start from i + 1 till len(nums)
# 3. check for addition and then return the list of indexes
# """
def two_sums(inp, tar):
    for i in range(len(inp)):  # 1, 4 -- > 1, 3 -- > 0   i == 1
        for j in range(i + 1, len(inp)):  # 2, 3 j == 2
            if inp[i] + inp[j] == tar:  # 7 + 15 == 22
                return [i, j]


print(two_sums([2, 7, 11, 15], 22))

# Get unique values

# it just like remove duplicates problem

# Remove duplicates
"""
1. create a empty container, that we want to put only unique elements
2. each iteration check if ele is already exists dont do anything, else append it
"""

list1 = [1, 2, 1, 2, 5]

list_of_unique_ele = []

for each_ele in list1:
    if each_ele not in list_of_unique_ele:
        list_of_unique_ele.append(each_ele)

print(list_of_unique_ele)
# another way
print(list(set(list1)))

# Remove even elements and print list
"""
1. iterate the list
2. check for even numbers
3. if its there use pop to remove it
4. print the original list
"""

list_of_elements = ["a", "s", "h", "w", "i", "n"]
new_list = []
for index, each_char in enumerate(list_of_elements):
    if index % 2 != 0:
        new_list.append(each_char)

print(new_list)

# Remove specified index from list and print

"""
1. first loop through all list elements
2. create blank list
3. check if index == given index don't append it.
4. else append it
"""

list_of_elements = [1, 2, 3, 4, 5, 6]

index = 2
new_list = []

for indx, each_ele in enumerate(list_of_elements):
    if indx != index:
        new_list.append(each_ele)
    else:
        print("The removed element is ", each_ele)

print(new_list)

# Finding a second-smallest number

"""
1. using sort methods
2. first find smaller no and remove from list again iterate through list find smaller one
    this is the 2nd smallest no
"""

list1 = [4, 5, 8, 9, 1, 3]

# using sort method

# list1.sort()
# print(f"the second largest number: {list1[1]}")

# using removing last element

smallest_ele = list1[0]
for i in list1:
    if smallest_ele > i:
        smallest_ele = i

list1.remove(smallest_ele)  # it removes last element from

smallest_ele = list1[0]
for j in list1:
    if smallest_ele > j:
        smallest_ele = j

print(f"second smallest no is {smallest_ele}")
