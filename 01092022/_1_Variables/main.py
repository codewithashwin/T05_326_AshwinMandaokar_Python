"""
Variables
"""

"""
variable is a very important component in programming languages

* what is variables?
- Variable is a name which is used to refer memory location of value. 
- Variable also known as identifier and used to hold value.
- A variable, as the name indicates is something whose value is changeable over time.  x = 10
- In Python, we don't need to specify the type of variable (int, float) because Python is a type infer language and 
smart enough to get variable type.
x = 10     int x = 10;
y = 11.2
10 + 15.5 =>   10.0 + 15.5  => 25.5

* Rules to declare the variable names.
1. variable name consist of letters, numbers & underscores
2. variable can't start with numbers but it starts with 

* convention to writing the variable names:
1. variable name should not be a keyword
2. it recommends all letter to be a lower letter

* what happened behind the scenes?
X = 10
1.Python interpreter allocates memory(2 bytes)  
2. Converts to binary format  (00010100)
3. Copy above binary data to reserved memory
4. Give address of above memory location to variable “x”

* Type casting
It is a method to convert the variable data type into a certain data type for the operation required to be performed by 
users.
There are two types of type casting in python:
1.Implicit typecasting:
 It converts data type into another data type automatically.No need of user intervention in this.
2.Explicit typecasting:
 It converts the variable datatype into certain datatype in order of the operation required.Here user involvement will 
 be there.
 

* How the assignment of a variable works?
The equal (=) operator is used to assign value to a variable.
The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign 
values to variables.
For Ex :   age = 20   x = 20
In above ex. operand to the left of the = operator is the name of the variable and the operand to the right of 
the = operator is the value stored in the variable. 

* Multiple assignments
i. Assigning single value to the multiple variables
--> a = b = c = 10
ii.Assigning multiple values to the multiple variables
--> a, b, c = 10, "string", True

* Tokens and their Types:
The smallest individual units in the give python program
Types of tokens
i. keywords: 
Are reserved words and has specific meaning in a language and they cannot be used as ordinary identifiers.

ii. Identifiers:
An identifier is a variable name. A Python identifier is a name used to identify a
variable, 
function name, 
class name, 
module name or 
other object name.
An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores
and digits (0 to 9)

iii. Literals:
In computer science, a literal is a notation for representing a fixed value  in source code.
name = “Madhu”   --- String literal
age = 10  --- integer literal
sal = 123.45 – float literal
age = 10+20

The literals include the string, unicode string, integer, float,  list, tuple and dictionary types

iv. Operators:
Operators are special symbols in Python that carry out arithmetic or logical computation.The value that the operator operates on is called the operand

>>> 2 + 3
5
Here + is an operator which is performing arithmetic computation.
2 and 3 are the operands and 
5 is the output of the operation.

v. Constants
A constant is a type of variable whose value cannot be changed. It is helpful to think of constants as containers that
hold information which cannot be changed later. Non technically, you can think of constant as a bag to store some books 
and those books cannot be replaced once placed inside the bag.

punctuators: (), . $


+++Questions+++
1. x = 10. Explain in detail for CRUD operations
- crud operation means create, retrieve, update, delete.
    x = 10 is a create operation there value 10 memory address will be stored in a variable x
    print(x) its a retrieve operation here print function goes that memory address, and printing in console
    x = 5 its a update operation but internally its create operation because new object will be created it not updating 
    previous one.
    del x its a delete operation, here the reference will be removed and not a value, after some time value will be 
    garbage collected

2. Garbage collection. How it works internally

- In python, garbage collection is a programme there this programme will help to remove the unwanted objects 
    like x = 10 here i create a object in memory
    x = 5 here 10 will unreferenced by variable x so it will be garbage collected
    if we talk about other languages like c, c++ there we as a programmer need to care of the garbage collection.

3. Memory Management in Python?
- Memory management is the process by which application read/write datas, In python, this process is handle by the 
python memory manager, so in python manages the objects in the form of private heap space and there reference will be 
stored in the stack memory.

"""