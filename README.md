## Project title
0x00. AirBnB clone - The console
Foundations - Higher-level programming ― AirBnB clone

## Motivation
The purpose of this project is to take the first step towards building a students' first full web application: The AirBnB clone. The first step is very important because it will use what is built during this project in all other following projects.

By the end of this project, students successfully learned:
- How to create a python package
- How to create a command interpreter in Python using the cmd module
- What is unit testing and how to implement it in a large project.
- How to serialize and deserialize a class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to  use it
- How to handle named arguments in a function

## Code Style
All code follows PEP8 coding standards and Google Style Python Docstring Documentation.

## Screenshots

## Tech/Framework Used
<b>Built with</b>
- Python3

## Features
- Store Objects
- Create new instance of BaseModel, save to JSON file and prints the id
- Print the string representation of an instance based on the class name and id
- Delete an instance based on the class name and id
- Print all the string representation of all instances based or not on the class name
- Update an instance based on the class name and id by adding or updating attribute

## Code Example

<b> Console Interactive mode </b>
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

<b> Console Non-Interactive Mode</b>
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Installation
```
$ git clone https://github.com/peytonbrsmith/AirBnB_clone.git
```

There are no additional libraries or dependencies for this program.

## Tests


## How to Use
![interactive mode](https://github.com/peytonbrsmith/AirBnB_clone/blob/main/images/consoleint.png)
![non-interactive mode](https://github.com/peytonbrsmith/AirBnB_clone/blob/main/images/consolenonint.png)