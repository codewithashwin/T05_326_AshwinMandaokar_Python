"""
Operators
"""

"""
Operators is just a symbols that help us to perform operations on data types and variables
the data types and variables are called as operands and symbol is a operator.
for ex 2 + 3 ==== 2 and 3 are the operands and addition symbol is a operator


Types of Operators
1 Arithmetic operator --> +,-,*,/, //, **
= arithmatic operators are the symbol that help us to do arithmetic operations.
symbol ---------------- Name ----------------- Example
+      ---------------- Addition -------------- 2 + 3, 
                                                x = 10
                                                y = 20
                                                x + y
-     ----------------- Subtraction ----------- x - y
*     ----------------- Multiplication -------- x * y
/     ----------------- Division -------------- x / y
%     ----------------- Modulus --------------- x % y
**    ----------------- Exponent -------------- x ** y
//    ----------------- Floor Division -------- x // y

2 Relational (Comparision) operator
= These operators compare the values on either sides of them and decide the relation among them. They are also called
Relational operators.Assume variable a holds 10 and variable b holds 20, then –

Operator	Description	                                        Example
==	        If the values of two operands are equal,        (a == b) is not true.
            then the condition becomes true.
            It will compare contents of two values	

!=	        If values of two operands are not equal,        (a != b) is true.
            then condition becomes true.	
            
<>	        If values of two operands are not equal,        (a <> b) is true. This is similar to != operator.
            then condition becomes true.
            
>	        If the value of left operand is greater         (a > b) is not true.
            than the value of right operand, 
            then condition becomes true.	
            
<	        If the value of left operand is less            (a < b) is true.
            than the value of right operand, 
            then condition becomes true.	
            
>=	        If the value of left operand is greater         (a >= b) is not true.
            than OR equal to the value of right operand,    20>= 20 OR
            then condition becomes true.	


<=	        If the value of left operand is less            (a <= b) is true.
            than OR equal to the value of right operand,
            then condition becomes true.	
            
3 Assignment Operators
= Assume variable a holds 10 and variable b holds 20, then –
a = 10,  b = 20 example of assignment operators
following are the augmented assignment operators
i. += , ii. -=, iii. *=, iv. /=, v. **=, vi. //=

4 Logical Operators
In Python, Logical operators are used on conditional statements (either True or False). They perform Logical AND,
Logical OR and Logical NOT operations.
OPERATOR	                  DESCRIPTION	                                SYNTAX
and	Logical AND:            True if both the operands are true	            x and y
or	Logical OR:             True if either of the operands is true	        x or y
not	Logical NOT:             True if operand is false	                     not x

5 Membership Operators
Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples.  Set1 = {1, 2, 3, 4}  
There are two membership operators
1   in          {1, 2, 3, 4}    True
5	in          {1,2,3,4}       False
6	not in      {1,2,3,4}        True
1   not in      {1,2,3,4}       False


6 Identity operators
Identity operators compare the memory locations of two objects. 

x = 10, y = 10

is          x is y        True
is not      x is not y    False


* Operator Precedence
It guides the order in which these operations are carried out,
when there are multiple operators written in single line of code.
The correct order of precedence is given by PEMDAS 
which means Parenthesis (), Exponential **, Multiplication *, Division /, Addition +, Subtraction -

"""
