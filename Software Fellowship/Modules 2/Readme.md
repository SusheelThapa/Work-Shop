# Modules Two

## What is Programming Language?

The language of computers is called Programming Languages.

Different level of Programming Language are::

1. Machine Level
2. Assemlby Level
3. High Level
4. Natural Language

## Where does Python fit in?

1. High level, general purpose programming language.
2. Interpreted Language
3. Dynamically typed
4. Multiple paradigms: objects oriented, impertive, functional, procedural

## Interpreter vs Compiler

### Why Python?

- Python is fast enough.
- Python can call other programs if needed.
- Python provides high level features for us programmers.
- Python is super easy.

## Python Shell invocation

**How to invoke a program?**
Just type the program's name(It must be in the PATH)

**How to invoke python?**
Just type the python(After you install it and add it to PATH)

## Run a python script

- Python files end in .py in default
- Python will execute each instruction line by line
- Run the python file
  ```python
  python first.py
  ```

## Python REPL

REPL stands for (Read Eval Print Loop)

- Useful for testing features
- Has some additional features.
- Sort of a playground.

## Python Program options

```python
python3 --version
python3 -c "print('apple')"
```

## Variables & Data Types

Variables are container to store the data.

**Analogy with buckets**

    Variables = names of buckets
    Data types = buckets

Static Typing: A bucket can hold only one type of thing

Dynamic Typing: A bucket can hold anything.

**Defining a variable**

```python
a = 4
Speech = "SoftwareFellowShip"
floating_variable = 4.0
```

_Note: Name are case sensitive_

**Literals in Python**

- string literals
- numeric literals
- boolean literals
- literal collection: `list`, `tuples`, `dictionaries`, `sets`
- A special literal: `None`

## User input and Output

1. `print`:

Syntax:
`print(object(s), sep=separator, end=end)`

```python
name = input("Enter your name")
print("Hello " + name);
```

2. Basic operators and Operator Precedence

3. String Operations

   String operations(startswith, split, indexing, slicing, formatting etc)

   Indexing: `"Python string"[3]`
   Slicing: `"Python string"[start:stop:step]`

   ```python
   "Python string".startswith("Pyth")
   "Python string".endswih("ing")
   ```

   Formatting
   `python 'Hello, {}'.format(name) f'Hello,{name}!'`

4. Flow Control

   Order in which the program's code executes

   - Sequential - default
   - Selection - decision and branching
   - Repetition - looping

5. `if...elif`

```python
	x = 15
	y = 12
	if x == y:
		print("Both are equal")
	elif x > y:
		print("x is greater than y")
	else:
		print("x is smaller than y")
```

6. Looping

   - to repeat a group of programming instrcutions
   - For loop(iterate over sequence)
   - While loop(repeat until the given condition is satisfied)

   **For loop**

   ```python
   lst  = [ 1, 2, 3, 4, 5];
   for i in range(len(lst)):
   	print(lst[i],end=" ")
   ```

   **While Loop**

   ```python
   m = 5
   i = 0
   while i < m
   	print(i, end = " ")
   	i = i + 1
   print("End")
   ```

   **Break and Continue**

   `break` is used to break out of the loop.

   `continue` is used to skip the remaining part of the loop

   ```python
   for i in range(10):
   	print("before")
   	print(i)
   	continue
   	print("after")
   ```

   ```python
   for i in range(10):
   	print("before")
   	print(i)
   	break
   	print("after")
   ```

7. List, Tuples, Dictionaries and Sets

8. List and Tuple operations

9. is vs ==

10. Dictionary

    1. Creating Dictionary

       - used to store data values in `key:values` pairs

       ```python
       actor={
       	"name": "Tom Cruise",
       	"age": "52",
       	"country":"USA",
       	"movie":["mission impossible", "Top Gun"]
       }
       ```

    2. Dictionary Operations

    3. Other Dictionary Operations

11. Sets

    1. Creating Sets
    2. Set operations

12. Function and Scope
