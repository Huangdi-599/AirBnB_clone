# AirBnB Clone: The Console
Introducing the AirBnB clone project, lets start!
First move: Create an interpreter for commands to control your AirBnB objects.

The AirBnB clone is the initial stage towards creating your own complete web application. This first step is crucial since all subsequent projects will make use of the things you produce during this project: Database storage, API access, front-end integration, HTML/CSS templating.

Each activity is connected to the next and will aid in:
Make BaseModel your parent class to handle the initialization, serialization, and deserialization of your future instances.
Make a straightforward serialization/deserialization flow: Example – Dictionary – a JSON string Create the first abstracted storage engine and all classes used by AirBnB (User, State, City, Place, etc.) that derive from BaseModel.
Build the project's initial abstracted storage engine: filing cabinets. generate all unittests to ensure that our classes and storage engine are working properly.

## Requirements:

* Contain the line #!/usr/bin/python3 as the very first line
* Properly use classes and imports
* Proper documentation of classes and files
* Pass PEP8 style
* Pass unittests

## Installation:
Step 1: Clone this repository 
Step 2: Switch to the repo's directory 


## How to Run and Use the Console:

1. Type "./console.py" (without quotation marks)
2. The prompt "(hbnb) " should appear. From here, enter a command. A list of available commands can be seen by typing help. For further information on a specific command, type help <command>. For example, help create. Note that many commands require arguments to be passed in
3. Depending on the command (and arguments), execute the proper programs
4. Wait for the next command(s) to be entered
5. Repeat step 3 as needed
6. Close the console using either quit or EOF

## Console Commands:

| Command Name | Description |
| --- | --- |
| quit | Exits the console |
| EOF | Exits the console |
| help <command> | Displays all commands. If a command is passed in, displays information about that specific command |
| create <class name> | Creates a new instance. Saves the instance to a JSON file and prints the id |
| show <class name> <id> | Displays information of a specific class name and id |
| destroy <class name> <id> | Removes an instance. The result will be saved to a JSON file |
| all <class name> | Displays all information. If a class name is passed in, displays all information only of that class name |
| update <class name> <id> <attribute name> <attribute value> | Updates an attribute name at a specific class name and id with the attribute value |
  
## Sample Output:
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) all
(hbnb) all AwesomeClass
** class doesn't exist **
(hbnb) create AwesomeClass
** class doesn't exist **
(hbnb) destroy
** class name missing **
(hbnb) destroy BaseClass
** class doesn't exist **
(hbnb) destroy BaseModel
** instance id missing **
(hbnb) destroy BaseModel 555
** no instance found **
(hbnb) create BaseModel
b8843b85-faa3-41c0-ace5-e17ae45d1e4b
(hbnb) all
["[BaseModel] (b8843b85-faa3-41c0-ace5-e17ae45d1e4b) {'updated_at': datetime.datetime(2020, 2, 19, 22, 26, 3, 766798), 'id': 'b8843b85-faa3-41c0-ace5-e17ae45d1e4b', 'created_at': datetime.datetime(2020, 2, 19, 22, 26, 3, 766751)}"]
(hbnb) show BaseModel b8843b85-faa3-41c0-ace5-e17ae45d1e4b
[BaseModel] (b8843b85-faa3-41c0-ace5-e17ae45d1e4b) {'updated_at': datetime.datetime(2020, 2, 19, 22, 26, 3, 766798), 'id': 'b8843b85-faa3-41c0-ace5-e17ae45d1e4b', 'created_at': datetime.datetime(2020, 2, 19, 22, 26, 3, 766751)}
(hbnb) create BaseModel
f3eb800d-2cb4-45a3-8fda-0f12d0c71d63
(hbnb) all
["[BaseModel] (b8843b85-faa3-41c0-ace5-e17ae45d1e4b) {'updated_at': datetime.datetime(2020, 2, 19, 22, 26, 3, 766798), 'id': 'b8843b85-faa3-41c0-ace5-e17ae45d1e4b', 'created_at': datetime.datetime(2020, 2, 19, 22, 26, 3, 766751)}", "[BaseModel] (f3eb800d-2cb4-45a3-8fda-0f12d0c71d63) {'updated_at': datetime.datetime(2020, 2, 19, 22, 26, 37, 56543), 'id': 'f3eb800d-2cb4-45a3-8fda-0f12d0c71d63', 'created_at': datetime.datetime(2020, 2, 19, 22, 26, 37, 56500)}"]
(hbnb) destroy BaseModel b8843b85-faa3-41c0-ace5-e17ae45d1e4b
(hbnb) all
["[BaseModel] (f3eb800d-2cb4-45a3-8fda-0f12d0c71d63) {'updated_at': datetime.datetime(2020, 2, 19, 22, 26, 37, 56543), 'id': 'f3eb800d-2cb4-45a3-8fda-0f12d0c71d63', 'created_at': datetime.datetime(2020, 2, 19, 22, 26, 37, 56500)}"]
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help EOF
EOF command to exit the program
(hbnb) quit
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
```