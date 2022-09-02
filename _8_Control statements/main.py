"""
Control statements
"""

"""

Control Statements :    
Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects
that were created in that scope are destroyed.

1. break statement : 
Terminates the loop statement and transfers execution to the statement immediately following the loop.
Break statement is a jump statement which is used to transfer execution control. It breaks the current execution and in 
case of inner loop, inner loop terminates immediately.
When break statement is applied the control points to the line following the body of the loop, hence applying break 
statement makes the loop to terminate and controls goes to next line pointing after loop body.

2. continue statements:
Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
Python Continue Statement is a jump statement which is used to skip execution of current iteration. After skipping,
 loop continue with next iteration.
We can use continue statement with for as well as while loop in Python.

3. pass statements
The pass statement in Python is used when a statement is required syntactically but you do not want any command or code
to execute.
In Python, pass keyword is used to execute nothing; it means, when we don't want to execute code, the pass can be used
to execute empty. It is same as the name refers to. It just makes the control to pass by without executing any code. 
If we want to bypass any code pass statement can be used.
"""

# Break example
# 0 to 50 even number first 10
# 0 2 4 6 8 10 12 14 16 18
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if i == 4:
        print(i)
        print("Element found")
        break
    print(i)
# ---------------------------
for letter in 'Python3':
    if letter == 'o':
        break
    print(letter)

# Continue example
a = 0
while a <= 5:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)
print("End of Loop")

# pass Example
# Do nothing
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        pass
    print(i)
