<h1>Handbook on Programming in Python</h1>

**AP Computer Science Principles 2023-2024**

Andrew Rynes

<!-- This is a comment (which will not be displayed in the live file);
replace all "???" with your own text. -->




___





<h1>Table of Contents</h1>

- [1. Compiling and Running](#1-compiling-and-running)
- [2. Data Types](#2-data-types)
- [3. Console I/O](#3-console-io)
- [4. Arithmetic Operations](#4-arithmetic-operations)
- [5. Assignment Operations](#5-assignment-operations)
- [6. Comments](#6-comments)
- [7. Decision Structures](#7-decision-structures)
- [8. Conditional Operators](#8-conditional-operators)
- [9. Logic Operators](#9-logic-operators)
- [10. Advanced Decision Structures](#10-advanced-decision-structures)
- [11. String Methods](#11-string-methods)
- [12. Random Generation](#12-random-generation)
- [13. Looping Structures](#13-looping-structures)
- [14. Functions/Methods](#14-functionsmethods)
- [15. Elementary Data Structures](#15-elementary-data-structures)
  - [15.1 Arrays/Lists](#151-arrayslists)
  - [15.2 Matrices](#152-matrices)
- [References](#references)

<!-- 
- [16. Major Keywords](#16-major-keywords)
- [17. Error Handling](#17-error-handling)
- [18. Working with Files](#18-working-with-files)
- [19. Major Language Features](#19-major-language-features)
  - [19.1 Classes](#191-classes)
  - [19.2 Inheritance](#192-inheritance)
  - [19.3 Generic Typing (Templates)](#193-generic-typing-templates)
  - [19.4 Pointers](#194-pointers)
- [20. Importing Local Libraries](#20-importing-local-libraries)
- [21. Working with Time](#21-working-with-time)
- [22. Importing Libaries from Package managers](#22-importing-libaries-from-package-managers)
- [23. Bitwise Operators](#23-bitwise-operators)
- [24. Common Data Structures](#24-common-data-structures)
- [25. Advanced Language Features](#25-advanced-language-features)
-->




___





# 1. Compiling and Running

In Python, there isn't any sort of code  you have to set up
before you can run the file. You can just put the code you want to run
directly to a file an run it.

**For example, here's Hello World in python.**
```python
print("Hello, world!")
```

```sh
>    Hello, world!
```

There also isn't any sort of need for a line ending character (i.e. a semicolon) like in Javascript.

___





# 2. Data Types

In Python, data types are dynamically assigned, which means you don't need to explicitly declare them. Python has several built-in data types, including:

**Integers:** These are whole numbers. For example:
```python
age = 25
```
**Floats:** These are numbers with decimal points. For example:
```python
pi = 3.14159
```
**Strings:** These are sequences of characters. For example:
```python
name = "John"
```
**Booleans:** These represent truth values, either True or False. For example:
```python
is_student = True
```
**Lists:** These are ordered, mutable collections of elements. For example:
```python
fruits = ["apple", "banana", "cherry"]
```
**Tuples:** These are ordered, immutable collections of elements. For example:
```python
coordinates = (3, 4)
```
**Dictionaries:** These are collections of key-value pairs. For example:
```python
person = {"name": "Alice", "age": 30}
```

Python also supports more advanced data types, like sets and custom-defined classes. 
Python's dynamic typing allows you to change the type of a variable during runtime.





# 3. Console I/O

In Python, you can perform input and output operations using the console.

## Input:

You can use the input() function to read input from the console. For example:
```python
name = input("Enter your name:")
```
```shell
>    Enter your name:
```

## Output:

You can use the print() function to display output in the console. For example:

```python
print("Hello, world!")
```

```shell
>    Hello, world!
```

### You can also format the output using string concatenation or f-strings:
```python
name = "Alice"
age = 30
print("Name: " + name + ", Age: " + str(age))
# or
print(f"Name: {name}, Age: {age}")
```

```shell
>    Name: Alice, Age: 30
```

The input() function reads input as strings, so if you need numeric input, you'll need to convert it to the appropriate data type using functions like int() or float().




___





# 4. Arithmetic Operations

In Python, you can perform various arithmetic operations on numbers. Some of the basic arithmetic operators include:

## Addition (+): 
- Adds two numbers together. For example:
```python
result = 5 + 3
print(result)
```
```shell
>    8
```

## Subtraction (-): 
- Subtracts one number from another. For example:
```python
result = 5 - 3
print(result)
```
```shell
>    2
```

## Multiplication (*): 
- Multiplies two numbers together. For example:
```python
result = 5 * 3
print(result)
```
```shell
>    15
```

## Division (/): 
- Divides one number by another. For example:
```python
result = 5 / 3
print(result)
```
```shell
>    1.6666666666666667
```

## Modulus (%): 
- Divides one number by another and returns the remainder. For example:
```python
result = 5 % 3
print(result)
```
```shell
>    2
```

## Exponent (**): 
- Raises a number to the power of another. For example:
```python
result = 5 ** 3
print(result)
```
```shell
>    125
```

## Floor Division (//): 
- Divides one number by another and returns the quotient without the remainder. For example:
```python
result = 5 // 3
print(result)
```
```shell
>    1
```
Python follows the standard order of operations (PEMDAS) when evaluating expressions, where parentheses are used to specify the order of operations.

Arithmetic operations are fundamental in mathematical and computational tasks and are extensively used in Python programming.






# 5. Assignment Operations

???





___





# 6. Comments

There are two types of comments in Python:

## 1. Single-Line Comments:
Single-line comments are used for brief explanations on a single line. They begin with the `#` symbol. For example:
```python
# This is a single-line comment
```

## 2. Multi-Line Comments: 
Python does not have a specific syntax for multi-line comments.
However, you can use triple quotes (either single or double) to **create** multi-line comments. For example:

```python
"""
This is a multi-line comment
It can span multiple lines
"""
```

Comments are essential for documenting code, providing context, and making it more understandable for both the original coder and others who may work on the code in the future.

___





# 7. Decision Structures

???





___





# 8. Conditional Operators

???





___





# 9. Logic Operators

???





___





# 10. Advanced Decision Structures

???





___





# 11. String Methods

???





___





# 12. Random Generation

???





___





# 13. Looping Structures

???





___





# 14. Functions/Methods

???





___





# 15. Elementary Data Structures

???





## 15.1 Arrays/Lists

???






## 15.2 Matrices

???





___





<!-- 
EVERYTHING BELOW IS OPTIONAL; 
UNCOMMENT BY REMOVING THE ARROW TAGS SURROUNDING
(i.e., delete the "< !--" and "-- >" tags)

CHANGE THE SECTION NUMBERS AS DESIRED
-->

<!-- # 16. Major Keywords

???





___ -->





<!-- # 17. Error Handling

???





___ -->





<!-- # 18. Working with Files

???





___ -->





<!-- # 19. Major Language Features

???







## 19.1 Classes

???





## 19.2 Inheritance

???





## 19.3 Generic Typing (Templates)

???





## 19.4 Pointers

???





___ -->





<!-- # 20. Importing Local Libraries

???





___ -->





<!-- # 21. Working with Time

???





___ -->





<!-- # 22. Importing Libaries from Package managers

???





___ -->





<!-- # 23. Bitwise Operators

???





___ -->





<!-- # 24. Common Data Structures

???





___ -->





<!-- # 25. Advanced Language Features

???





___ -->





# References

* [Markdown Cheatsheet](https://gist.github.com/jonschlinkert/5854601)
* [description](http://example.com)

