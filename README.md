# python-learnings

## What is Python?

[Python](https://en.wikipedia.org/wiki/Python_(programming_language)) is a high-level programming language, and it is released in 1991. [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum "Guido van Rossum") is the father of Python.

it's a commonly-used modern programming language. String manipulation. Networking.

## Variables

### String

```python
from cs50 import get_string

print('hello, world') # This will output "hello, world"

answer = get_string('What's your name? ') # dynamic variables get_int, get_float
print('hello, ' + answer) # concatnate
print('hello, ', answer)
print(f'hello, {answer}')
print('hello, {}'.format(answer))

# some of String methods
text = input('This iS a String')
text.strip()
text.lower()
text.capitalize()
text.split()
```

```python
# Do you agree? project
s = input("Do you agree?")
s = s.lower()

if s in ["y", "yes"]:
	print("Agreed")
elif s in ["n", "no"]:
	print("Not agreed")

# uppercase project
before = input("Before: ")
print("After: ", end="")
for c in before:
	print(c.upper(), end="")
print()
# make it shorter
before = input("Before: ")
after = before.upper()
print(f"After: {after}") 
```

### Other Date Types

`boolean` (True/False), `float`, `int`, `str`

The `array` will be replaced by `range`, `list`, `tuple`, `dict` (dictionary), `set`, …

#### Lists

```python
# LISTS - mutable sets of data
empt_nums = [] # An empty List
integer_nums = [1, 2, 3, 4] # A List with all integer values
string_nums = ['one', "two", "three", "four"] # A List with all string values
float_nums = [1.2,2.3,3.4,4.5] # A List with all float values
mixed_nums = ['one',2,3.1,'four','five'] # A List with mixed values

# How to sort a List?
sorted(integer_nums)
integer_nums.sort()

# How to add an item to a List?
integer_nums.append(5) # This to insert number 5 as the last item to the list integer_nums
integer_nums.insert(4, 5) # This to new item to specific index of a list | insert(index, new_item)
integer_nums[4] = 5 # This works the same as insert(index, new_item) | variable[index] = new_item
integer_nums.extend([5, 6]) # This to insert multiple items to a list

# How to remove an item from a List?
mixed_nums.clear() # This to remove everything in the list
mixed_nums.remove(4) # This to remove one actual item from the list based on its index
mixed_numes.pop(0) # This to remove multiple items in the list by using index

# List Comprehensions
my_string = "hello"
my_list = []

for letter in my_string:
	my_list.append(letter)
print(my_list) # This will print ["h","e","l","l","o"]

# The above code can be replaced by the following code
my_list = [letter for letter in my_string]
print(my_list) # This will print ["h","e","l","l","o"] too

# Another examples of the above code
new_list = [num**2 for num in range(0,11)]
print(new_list) # This will print [0,1,4,9,16,25,36,49,64,81,100]

# Another examples of the above code with conditions
new_new_list = [x for x in range(0,11) if x%2==0]
print(new_new_list) # This will print [0,2,4,6,8,10]

# Another examples with complex calculation
c = [0,10,20,34.5]
f = [((9/5)*temp + 32) for temp in c]
print(f) # This will print [32.0,50.0,68.0,94.1]

# List Comprehension with nested For Loop
# Normal way
my_list = []
for x in [2,4,6]:
	for y in [1,10,100]:
		my_list.append(x*y)
print(my_list) # This will print [2,20,200,4,40,400,6,60,600]

# Shorter way
my_list [x*y for x in [2,4,6] for y in [1,10,100]]
print(my_list) # This will print same results as [2,20,200,4,40,400,6,60,600]
```

#### Tuples

```python
# TUPLE - immutable sets of data
presidents = [
	("George Washington", 1789),
	("John Adams", 1797),
	("Thomas Jefferson", 1801),
	("James Madison", 1809)
]

for prez, year in presidents:
	print("In {1}, {0} took office".format(prez, year))
```

#### Dictionaries

```python
# DICTIONARIES
pizzas = {
	"cheese": 9,
	"pepperoni": 10,
	"vegetable": 11,
	"buffalo chicken": 12
}

pizzas["cheese"] = 8 # This to change the associated value of "cheese"
pizzas["bacon"] = 14 # This to add "bacon" to pizzas dictionary

# This to do something when the condition meets
if pizzas["vegetable"] < 12:
	# do something
```

#### Sets

```python
"""
SETS
- Unordered: Sets don't maintain the order in which you add elements.
- Unique Elements: Sets cannot contain duplicate elements.
- Immutable Elements: The elements within a set must be immutable (e.g., numbers, strings, tuples). You cannot have lists, dictionaries, or other sets as direct elements of a set.
"""
num = {"one","two","three"}
num = {1,2,3,4,4} # This will return only 1,2,3,4 cause 4 is duplicated

# You can convert a List to a Set by using function set()
test_list = [1,2,3,2]
test_set = set(test_list) # With this, the duplicated 2 will be removed
words = set('Mississippi') # This gives you a hash table / create a set from String

def check(word):
	if word.lower() in words:
		return True
	else:
		return False

def load(dictionary):
	file = open(dictionary, "r")
	for line in file:
		word = line.rstrip()
		words.add(word)
	close(file)
	return True

def size():
	return len(words)

def unload():
	return True
```

## Comparison Operators/Chaining Comparison Operators (Logital Operators)

### Comparison Operators

| Operators | Description           | Examples       |
| --------- | --------------------- | -------------- |
| ==        | equal                 | 2 == 2 / True  |
| !=        | not equal             | 2 != 2 / False |
| <         | less than             | 2 < 2 / False  |
| >         | greater than          | 2 > 1 / True   |
| <=        | less than or equal    | 2 <= 2 / True  |
| >=        | greater than or equal | 5 >= 3 / True  |

### Logical Operators

It is used to combine comparisons. 3 values:

* **and** `'h' == 'h' and 2 > 3 / False`
* **or** `100 == 1 or 1 < 2 / True`
* **not** `not 400 > 5000 / True`

### Useful Operators

```python
# range() function
# range(start, stop, step side)
my_list = [1,2,3]

for num in range(10):
	print(num) # It will print from number 0 to 9, not include 10

for num in range(2,10):
	print(num) # It will print from number 2 to 9, not include 10

for num in range(0,11,2):
	print(num) # It will print 0,2,4,6,8,10. Because we have step side = 2

# You can create a list using range for convinence
my_new_list = list(range(0,11,2)) # This list will be [0,2,4,6,8,10]

# enumerate() function
words = "abcdef"

for item in words:
	print(item) # This will return tuples (1, "a") (2, "b") ...

# This will return
# 0
# a
# ------
# 1
# b
# ------
for index,letter in enumerate(words):
	print(index)
	print(letter)
	print("-"*6)

# zip() function - to combine list together
# You can zip multiple Lists together
# zip() ignores extra items on any Lists
my_list_1 = [1,2,3,4,5,6]
my_list_2 = ["one","two","three"]

for item in zip(my_list_1,my_list_2):
	print(item) # This will return tuples (1, "one") (2, "two") (3, "three")

# in operator, min(), max()
# random in Python
from random import shuffle
from random import randint

a_list = [1,2,3,4,5,6,7,8,9]
shuffle(a_list) # This will change index of the List randomly

random_number = randint(0,99) # This will return a random number between 0 and 99 
```

## Conditionals/Control Flow

### If/Else Statement

```python
name = "Me"

if name == "Me":
	print('Hello, nice to meet you!')
else:
	print("I don't know you")
```

### If/Elif/Else Statement

```python
x = int(input("Enter x number: "))
y = int(input("Enter y number: "))
if x < y:
	print("x is less than y")
elif x > y:
	print("x is not less than y")
else:
	print("x is equal to y")
```

## Loops

### While Loops

```python
i = 0
while i < 3:
	print(f"The current value of i is {i}")
	i += 1
else:
	print("I IS NOT LESS THAN 3")

while x < 5:
	if x == 3:
		break # It will stop when x equals to 3
	print(x)
	x += 1

while True:
	print("meow")
```

### For loops

iterable / going through something

```python
# Lists and For loop
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    print(f"Hello {num}")
print('=='*3)

for num in my_list:
    # Check to show even or odd number
    if num % 2 == 0:
        print(f'Even number: {num}')
    else:
        print(f'Odd number: {num}')

for i in range(3):
    print(f"Hello, world {i}")

# Lists, Tupples and For loop
my_list_tup = [(1,2),(3,4),(5,6),(7,8)]

print('length:',len(my_list_tup))

for a,b in my_list_tup:
    print(f'this is value of a: {a}')
    print(f'this is value of b: {b}')
    print('=='*3)

# Dictionaries and For loop
pizzas = {"cheese": 9, "pepperoni": 10, "vegetable": 11, "buffalo chicken": 12}

# To only get the key in the dict
for pie in pizzas:
    print(pie)
print("==" * 3)

# To only get the value in the dict
for price in pizzas.values():
    print("$" + str(price))
print('=='*3)

for pie, price in pizzas.items():
    print(pie + ' $' + str(price))
print('=='*3)

for pie, price in pizzas.items():
    print(f"A whole {pie} pizza costs ${price}")
    print('--'*3)

# pass function
x = [1,2,3]
for item in x:
	pass # Do nothing with this for loop

# continue function
name = "Parker"
for letter in name:
	if letter == "r":
		continue # It will not include letter r
	print("letter")

i = ["one","two","three","four"]
for num in i:
	if num == "three":
		break # It will stop when num is three
	print(num)
```

## Functions/Methods

```python
if __name__ == "__main__":
	main()

# How to define a function/method?
def square(x):
	return x * x
```

## Objects

```python
class Student():

	def __init__(self, name, id):
		self.name = name
		self.id = id

	def changeID(self, id):
		self.id = id

	def print(self):
		print("{} - {}".format(self.name, self.id))

jane = Student("Jane", 10)
jane.print()
jane.changeID(11)
jane.print()
```

## Sys

```python
from sys import argv

if len(argv) == 2:
	print(f"hello, {argv[1]}")
else:
	print("hello, world")

for arg in argv[1:]:
	print(arg)

from sys

if len(sys.argv) != 2:
	print("Missing command-line argument")
	sys.exit(1)

print(f"hello, {sys.argv[1]}")
sys.exit(0)
```

## Print()

```python
print("?" * 4) # This will print ? 4 times

for i in range(3):
	print("#" *3)
```

## I/O with Basic Files

```python
myfile = open('myfile.txt') # open() function is used to open the file in the directory you want
myfile.read() # read() function is used to read the content of the file
myfile.seek(0) # seek() function is used to reset the cursor to the beginning of the file, so you can read the file again
myfile.readlines() # readlines() function is used to read the content of the file, and make a List of each line as an index
myfile.close() # close() function is used to close the file if you do not use it any more

# Other way to open and read the file without remember to close it
with open('myfile.txt') as my_new_file:
	contents = my_new_file.read()

"""
Reading, Writing, Appending Modes
mode='r' is read only
mode='w' is write only (will overwrite files or create new)
mode='a' is append only (will add on to files)
mode='r+' is reading and writing
mode='w+' is writing and reading (Overwrites existing files or creates a new file)
"""

# Assume the new_file.txt has been created
with open('new_file.txt',mode='a') as f:
	f.write('This is new line')

with open('new_file.txt',mode='r') as f:
	print(f.read())

# Assume the new_file_new.txt does not exist
with open('new_file_new.txt',mode='w') as f:
	f.write('This is totally new file')

with open ('new_file_new.txt',mode='r') as f:
	print(f.read())
```

## Examples

### Simple Face Detection Project

```python
from PIL import Image
import face_recognition

image = face_recognition.load_image_file("office.jpg")

face_locations = face_recognition.face_locations(image)

for face_location in face_locations

	top, right, bottom, left = face_location

	face_image = image[top:bottom, left:right]
	pil_image = Image.fromarray(face_image)
	pil_image.show()

```

### Calculation

```python
scores = [72, 73, 33]

average = sum(scores) / len(scores)
print (f"Average: {average}")
```

```python
from cs50 import get_int

scores = []
for i in range(3):
	score = get_int("Score: ")
	scores.append(score) # scores += [score]

average = sum(scores) / len(scores)
print (f"Average: {average}")
```

### Search

```python
# To search name
import sys

names = ["James", "Peter", "Linda", "Tom", "Sam", "Tina", "Coco"]

name = input("Name: ")

# for n in names:
#	if name == n:
if name in names:
	print("Found")
	sys.exit(0)

print("Not found")
sys.exit(1)

# To search a person and his/her phone number
people = {
	"Phat": "123456789",
	"Thai": "234567890"
}

name = input("Name: ")
if name in people:
	print(f"Number: {people[name]}")
```

### Compare

```python
s = input("s: ")
t = input("t: ")

if s == t:
	print("Same")
else:
	print("Different")
```

### Swap

```python
x = 1
y = 2

print(f"x is {x}, y is {y}")
x, y = y, x
print(f"x is {x}, y is {y}")
```

### Phonebook file open

```python
import csv

# Open file and close file way
file = open("phonebook.csv", "a")

name = input("Name: ")
number = input("Number: ")

writer = csv.writer(file)
writer.writerow([name, number])

file.close()

# With open file way
with open("phonebook.csv", "a") as file:

	name = input("Name: ")
	number = input("Number: ")

	writer = csv.writer(file)
	writer.writerow([name, number])
```

### Text to speech

```python
import pyttsx3

engine = pyttsx3.init()
name = input("Name: ")
engine.say(f"hello, {name}")
engine.runAndWait()
```

## Flask

http-server is one of the web server services that you can use.

```
https://www.example.com/route?key=value&key=value -> (parsing)
```

How to run a project? `flash run`

What do you need at least to run a project?

* `app.py`
* `requirement.txt`
* `static/`
* `templates/`

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
```
