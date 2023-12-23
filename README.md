# python-learnings

## Python Syntax

it's a commonly-used modern programming language. String manipulation. Networking. Python is released in 1991.

## Variables

### String

```python
from cs50 import get_string

print("hello, world")

answer = get_string("What's your name? ") # dynamic variables get_int, get_float
print("hello, " + answer) # concatnate
print("hello, ", answer)
print(f"hello, {answer}")

# string methods
text = input(" This iS a String   ")
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

### Date type

`bool`, `float`, `int`, `str`, …

the `array` will be replaced by `range`, `list`, `tuple`, `dict` (dictionary), `set`, …

```python
# Lists - mutable sets of data
# it gives you a list OR num = list()
nums = []
nums = [1, 2, 3, 4]
nums = ["one", "two", "three", "four"]

# how to add stuff in the list?
# to insert a new item
nums.append(5)
# insert(index, new_item) or variable[index] = new_item
nums.insert(4, 5)
nums[4] = 5
# to insert multiple items to the list
nums.extend([5, 6])

# how to remove stuff in the list?
# to remove everything in the list
nums.clear()
# to remove one actual item in the list
nums.remove(4)
# to remove multiple items in the list by using index
numes.pop(0)

# Tuples - immutable sets of data
presidents = [
	("George Washington", 1789),
	("John Adams", 1797),
	("Thomas Jefferson", 1801),
	("James Madison", 1809)
]

for prez, year in presidents:
	print("In {1}, {0} took office".format(prez, year))

# Dictionaries
pizzas = {
	"cheese": 9,
	"pepperoni": 10,
	"vegetable": 11,
	"buffalo chicken": 12
}

# to change the associated value of "cheese"
pizzas["cheese"] = 8

# to do something when the condition meets
if pizzas["vegetable"] < 12:
	# do something

# to add "bacon" to pizzas dictionary
pizzas["bacon"] = 14

# Sets - mutable
words = set(); # it gives you a hash table

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

## Conditionals

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

```python
i = 0
while i < 3:
	print("meow")
	i += 1

for i in [0, 1, 2]: # in list
	print("hello, world")

for i in range(3):
	print("hello, world")

while True:
	print("meow")

# Loops (redux) - extremely flexible
# Dictionaries
pizzas = {
	"cheese": 9,
	"pepperoni": 10,
	"vegetable": 11,
	"buffalo chicken": 12
}

for pie in pizzas:
	# use pie in here as a stand-in for "i"
	print(pie)

for pie, price in pizzas.items():
	print(price)

for pie, price in pizzas.items():
	print("A whole {} pizza costs ${}".format(pie, price))
	print("A whole " + pie + " pizza costs $" + str(price))

```

## Functions/Methods

```python
if __name__ == "__main__":
	main()

# how to define a function?
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

## Print

```python
print("?" * 4)

for i in range(3):
	print("#" *3)
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

file = open("phonebook.csv", "a")

name = input("Name: ")
number = input("Number: ")

writer = csv.writer(file)
writer.writerow([name, number])

file.close()

# another way
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
engine.say(f"hellow, {name}")
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
