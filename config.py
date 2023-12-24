SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
TILE_SIZE = 32

FPS = 60

PLAYER_SPEED = 3
ENEMY_SPEED = 2

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)

LEVEL = 0
MAX_LEVEL = 5

MAX_HEALTH = 3
HEALTH_DECREASE = 1

PLAYER_LAYER = 5
ENEMY_LAYER = 5
EXIT_LAYER = 4
BLOCK_LAYER = 3
LAVA_LAYER = 2
GROUND_LAYER = 1

Tile_Map = [
    'BBBBBBBBBBBBBBBBBBDDBBBBBBBB',
    'B....B........E.......B....B',
    'B....B...BBBBBBBBBBBBBB....B',
    'B....B.....................B',
    'BBBBBB.....................B',
    'B......BBB....BBBBBBBBBBBBBB',
    'B...BBBB..E...B......B.....B',
    'B...B.........B......B.....B',
    'B...B....BBBBBBBBB...B.....B',
    'B...B....B.......BBBBB.....B',
    'B...B....B..P........B.....B',
    'B...B....BBBB....E...B.....B',
    'B...B.......BB.............B',
    'B...B........BBBBBBB.E.....B',
    'BBBBB.......E..............B',
    'B..........................B',
    'B...BBBBBBBBBBBBBBB........B',
    'B...B......................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBB',
]

Tile_Map2 = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B..........................B',
    'B...BBBBBBBBBBBBBBBBBBBBBBBB',
    'B..........................D',
    'BBBBB.....E.BBBBBBBBBB.....D',
    'B...B.......B.......BBBBBBBB',
    'B...B.......B..E....B......B',
    'B...B...BBBBB.......B......B',
    'B...B.E.B......B....B......B',
    'B...B...B...P..B....B......B',
    'B...B...BBBBBBBB....B......B',
    'B...B.....B................B',
    'B...B.....B.........E......B',
    'B...B.....B................B',
    'B...B.....BBBBBBBBBBB......B',
    'B...B......................B',
    'B..............E...........B',
    'B..........................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBB',
]


Tile_Map3 = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B........E.................B',
    'B...BBBBBBBBBBBBBBBBBB..E..B',
    'B...B......................B',
    'B...B......................B',
    'B...B...BBBBBBBBB...BBBBBBBB',
    'B...B.......B...B...B......B',
    'B...B.......B...B..........B',
    'B...BBBBBBBBB...B...E......B',
    'B....E......P...B..........B',
    'BBBBBBBBBBBBBBBBBBBBB......B',
    'B...................B......B',
    'B............E......B......B',
    'B...................B......B',
    'B......BBBBBBBBBB...B......B',
    'B......B...................B',
    'B......B......B............B',
    'B......B......B............B',
    'BBDDBBBBBBBBBBBBBBBBBBBBBBBBB',
]

Tile_Map4 = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'D............E.............B',
    'D......BBBBBBBBBBBBBBBB....B',
    'B......B...................B',
    'B......B...................B',
    'B......BBBBBB.......BBBBBBBB',
    'B...........B..............B',
    'B...........B..............B',
    'BBBBBBBBBBBBBBBBBBBBBBB....B',
    'B...........P.........B....B',
    'B.....................B....B',
    'BBBBBBBBBBBBBBBB......B.E..B',
    'B................E....B....B',
    'B.....................B....B',
    'B.E.BBBBBBBBBBBBBBBBBBB....B',
    'B..........................B',
    'B..............E...........B',
    'B..........................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBB',
]

Tile_Map5 = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B.............E............B',
    'B......BBBBBBBBBBBBBBBB....B',
    'B......B.............E.....B',
    'B......B...................B',
    'B....BBBBBBBB.......BBBBBBBB',
    'B....B......B.......B......B',
    'B....B......BBB.E.BBB......B',
    'B....B......B.......B......B',
    'B....B......P.......B......B',
    'BB..BBBBBBBBBBBBBBBBBBBBBBBB',
    'B..........................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBB..B',
    'B...................E......B',
    'B......BBBBBBBBBBBBBBBBBBBBB',
    'B......B...................B',
    'B...............E..........D',
    'B..........................D',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBB',
]

questions = [
    {
        "question": "What is the correct syntax on printing in python?",
        "choices": ["print()", "cout<<", "System.out.print()"],
        "correct_answer": "print()"
    },
    {
        "question": "What does the 'print' function do in Python?",
        "choices": ["Accepts user input", "Displays output to the console", " Performs mathematical operations"],
        "correct_answer": "Displays output to the console"
    },
    {
        "question": "Which data structure is ordered and immutable in Python?",
        "choices": ["List", "Tuple", "Dictionary"],
        "correct_answer": "Tuple"
    },
    {
        "question": "What is the purpose of 'if-else' statements in Python?",
        "choices": ["To create loops", "To handle exceptions", "To make decisions based on conditions"],
        "correct_answer": "To make decisions based on conditions"
    },
    {
        "question": "What will the following code snippet output: 'Python'[1:4]?",
        "choices": ["'yth;'", "'ytho'", "'ython'"],
        "correct_answer": "'ytho'"
    },
    {
        "question": "Which statement is used to exit from a loop in Python?",
        "choices": ["Break", "Exit", "Continue"],
        "correct_answer": "Break"
    },
    {
        "question": "What does the 'len()'' function do in Python?",
        "choices": [" Returns the last element of a list", "Returns the length of an object", "Returns the largest element in a list"],
        "correct_answer": "Returns the length of an object"
    },
    {
     
        "question": "How do you check the length of a list named my_list in Python?",
        "choices": ["'length(my_list)'","'count(my_list)'","'len(my_list)'"],
        "correct_answer": "'len(my_list)'"
    },
    {
        "question": "How do you remove an item with a specific value from a list in Python?",
        "choices": ["'list.remove(value)'","'list.delete(value)'","'list.discard(value)'"],
        "correct_answer": "'list.remove(value)'"
    },
    {
        "question": "Which of the following is the correct way to comment out multiple lines of code in Python?",
        "choices": ["// This is a comment","/* This is a comment */","# This is a comment"],
        "correct_answer": "# This is a comment"
    },
    {
         "question": "How do you compare values in a variable?",
        "choices": ["+","==","="],
        "correct_answer": "=="       
    },
    {
        "question": "What is the purpose of the else clause in a try-except block in Python?",
        "choices": [" It is used for iteration in the except block.","It is executed if the try block raises an exception.","It is not a valid part of a try-except block."],
        "correct_answer": "It is executed if the try block raises an exception."
    },
    {
        "question": "How do you concatenate two lists 'list1' and 'list2' in Python?",
        "choices": ["list1.add(list2)","list1.concatenate(list2)","list1 + list2"],
        "correct_answer": "list1 + list2"
    },
    {
        "question": "Which of the following is a valid way to create an empty list in Python?",
        "choices": ["list = ","list = []","list = new List()"],
        "correct_answer": "list = []"
    },
    {
        "question": "What is the purpose of the append() method for a list in Python?",
        "choices": ["It removes the last element from the list.","It adds a new element at the beginning of the list.","It adds a new element at the end of the list."],
        "correct_answer": "It adds a new element at the end of the list."
    },
    {
        "question": "What is the purpose of the max() function in Python?",
        "choices": ["It returns the smallest element in a list.","It returns the largest element in a list or among the arguments."," It calculates the average of a list."],
        "correct_answer": "It returns the largest element in a list or among the arguments."
    },
    {
        "question": "How do you check if a variable x is a boolean in Python?",
        "choices": ["isbool(x)","x.type() == 'bool'","type(x) == bool"],
        "correct_answer": "type(x) == bool"
    },
    {
        "question": "How do you remove the last item from a list in Python?",
        "choices": ["list.remove_last()","list.pop()","list.remove(-1)"],
        "correct_answer": "list.pop()"
    },
    {
        "question": "What is the purpose of the 'is' keyword in Python?",
        "choices": ["It is used for identity testing.","It is used for arithmetic operations.","It checks if a variable is initialized."],
        "correct_answer": "It is used for identity testing."
    },
    {
        "question": "How do you convert a string to uppercase in Python?",
        "choices": ["string.uppercase()","uppercase(string)","string.upper()"],
        "correct_answer": "string.upper()"
    },
    {
        "question": "What is the purpose of the del statement in Python?",
        "choices": ["It deletes a file from the filesystem.","Removes an element from a list","It defines a block of code."],
        "correct_answer": "Removes an element from a list"
    },
    {
        "question": "How do you display 'My name is Axel'",
        "choices": ["System.out.print(My name is Axel)","print(My name is Axel)","console.log(My name is Axel)"],
        "correct_answer": "print(My name is Axel)"
    },
    {
        "question": "How do you check if a value x is not equal to 10 in Python?",
        "choices": ["if x =! 10:","if x != 10:","if x <> 10:"],
        "correct_answer": "if x != 10:"
    },
    {
        "question": "What is the purpose of the set() function in Python?",
        "choices": ["It creates an empty set.","It converts a list to a set.","It removes duplicates from a list."],
        "correct_answer": "It creates an empty set."
    },
    {
        "question": "Which of the following is used to convert a string to a list of characters in Python?",
        "choices": ["string.to_list()","list(string)","split(string)"],
        "correct_answer": "list(string)"
    },
    {
        "question": "What is the purpose of the lambda keyword in Python?",
        "choices": ["It defines a multiline function.","It creates an anonymous function.","It declares a constant."],
        "correct_answer": "It creates an anonymous function."
    },
    {
        "question": "What is the purpose of the __str__ method in Python?",
        "choices": ["It converts an object to a string representation.","It creates a string from a list.","It defines the string type."],
        "correct_answer": "It converts an object to a string representation."
    },
    {
        "question": "What is the purpose of the next() function in Python?",
        "choices": ["It returns the next element in a list.","It generates the next random number.","It retrieves the next value from an iterator."],
        "correct_answer": "It retrieves the next value from an iterator."
    },
    {
        "question": "Which of the following is used to convert a string to a lowercase in Python?",
        "choices": ["string.lower()","lowercase(string)","string.to_lower()"],
        "correct_answer": "string.lower()"
    },
    {
        "question": "What is the purpose of the all() function in Python?",
        "choices": ["It checks if all elements in an iterable are true.","It checks if any element in an iterable is true.","It checks if an element exists in an iterable."],
        "correct_answer": "It checks if all elements in an iterable are true."
    },
    {
        "question": "What is the purpose of the range() function in Python?",
        "choices": [" Generates a list of numbers","Creates a range object representing a sequence of numbers"," Defines the range of a for loop"],
        "correct_answer": "Creates a range object representing a sequence of numbers"
    },
    {
        "question": "How do you check if a key exists in a dictionary in Python?",
        "choices": ["if key.exists(dictionary):","if key in dictionary:","if dictionary.contains(key):"],
        "correct_answer": "if key in dictionary:"
    },
    {
        "question": "What is the purpose of the *args syntax in a function definition in Python?",
        "choices": [" Indicates optional arguments","Allows passing a variable number of non-keyword arguments to a function","Is used for keyword arguments"],
        "correct_answer": "Allows passing a variable number of non-keyword arguments to a function"
    },
    {
        "question": "Which of the following is used to convert a string to uppercase in Python?",
        "choices": ["string.to_upper()","uppercase(string)","string.upper()"],
        "correct_answer": "string.upper()"
    },
    {
        "question": "Which of the following is used to sort a list in descending order in Python?",
        "choices": ["sorted(list, reverse=True)","list.reverse()","reverse(list)"],
        "correct_answer": "sorted(list, reverse=True)"
    },
    {
        "question": "What is the purpose of the 'int()' function in Python?",
        "choices": ["Converts a float to an integer","Checks if a variable is an integer","Converts a string to an integer"],
        "correct_answer": "Converts a string to an integer"
    },
    {
        "question": "What is the purpose of the 'sorted()' function in Python?",
        "choices": ["Sorts elements in descending order","Sorts elements in ascending order","Randomly shuffles elements"],
        "correct_answer": "Sorts elements in ascending order"
    },
    {
        "question": " What is Python?",
        "choices": ["A snake","A high-level programming language","A type of pasta"],
        "correct_answer": "A high-level programming language"
    },
    {
        "question": "How is memory managed in Python?",
        "choices": [" Manual memory allocation","Automatic memory management (garbage collection)","Memory pools"],
        "correct_answer": "Automatic memory management (garbage collection)"
    },
    {
        "question": "What is the difference between 'list' and 'tuple' in Python?",
        "choices": ["Lists are immutable, tuples are mutable","Lists are mutable, tuples are immutable","Both lists and tuples are mutable"],
        "correct_answer": "Lists are mutable, tuples are immutable"
    },
    {
        "question": "How can you open and close a file in Python?",
        "choices": ["openFile() and closeFile()","read() and write()","open() and close()"],
        "correct_answer": "open() and close()"
    },
    {
        "question": "How do you install external packages in Python?",
        "choices": ["Using the 'install' keyword"," With the 'import' statement","Using the 'pip' package manager"],
        "correct_answer": "Using the 'pip' package manager"
    },
    {
        "question": "How do you create a variable in Python?",
        "choices": ["var x = 5","x := 5","x = 5"],
        "correct_answer": "x = 5"
    },
    {
        "question": "How does garbage collection work in Python?",
        "choices": ["It manually deallocates memory","It automatically reclaims memory occupied by objects that are no longer in use"," It is a function in the 'gc' module"],
        "correct_answer": "It automatically reclaims memory occupied by objects that are no longer in use"
    },
    {
        "question": "Explain the concept of a set in Python.",
        "choices": ["An unordered collection of unique elements","An ordered collection of unique elements","A collection of ordered elements"],
        "correct_answer": "An unordered collection of unique elements"
    },
    {
        "question": "How do you define a function in Python?",
        "choices": ["method function_name():","def function_name():","define function_name():"],
        "correct_answer": "def function_name():"
    },
    {
        "question": "How do you iterate over a dictionary in Python?",
        "choices": ["for key, value in my_dict:","for value in my_dict:","for item in my_dict.items():"],
        "correct_answer": "for item in my_dict.items():"
    },
    {
        "question": "How do you convert a list to a tuple in Python?",
        "choices": ["tuple(my_list)","my_list.to_tuple()","list(my_tuple)"],
        "correct_answer": "tuple(my_list)"
    },
    {
        "question": "What is the purpose of the json module in Python?",
        "choices": ["To manipulate JavaScript objects in Python","To create Java objects in Python","To serialize and deserialize JSON data"],
        "correct_answer": "To serialize and deserialize JSON data"
    },
    {
        "question": "What is the purpose of the 'math' module in Python?",
        "choices": ["To perform advanced mathematical operations","To create mathematical models","To manipulate matrices"],
        "correct_answer": "To perform advanced mathematical operations"
    },
    {
        "question": "How can you convert a set to a list in Python?",
        "choices": ["list(set)","convert_set_to_list(set)","set.to_list()"],
        "correct_answer": "list(set)"
    },
    {
        "question": "What is the symbol of Addition?",
        "choices": ["+","#","*"],
        "correct_answer": "+"
    },
    {
        "question": "Wha is the symbol of Subtraction?",
        "choices": ["&","-","_"],
        "correct_answer": "-"
    },
    {
        "question": "What is the symbol of Multiplication?",
        "choices": ["*","%","!"],
        "correct_answer": "*"
    },
    {
        "question": "What is the symbol of Float Division?",
        "choices": ["/","%","#"],
        "correct_answer": "/"
    },
    {
        "question": "What is the symbol of Exponentiation?",
        "choices": ["++","==","**"],
        "correct_answer": "**"
    },
    {
        "question": "What is the operator for Absolute Value?",
        "choices": ["abs[]","abs''","abs()"],
        "correct_answer": "abs()"
    },
    {
        "question": "What is the operator for Integer Division?",
        "choices": ["!!","##","//"],
        "correct_answer": "//"
    },
    {
        "question": "What is the operator for Division with Remainder?",
        "choices": ["%","$","*"],
        "correct_answer": "%"
    },
    {
        "question": "What is the symbol for less than?",
        "choices": ["<",">","="],
        "correct_answer": "<"
    },
    {
        "question": "What is the symbol for greater than?",
        "choices": [">","<","+"],
        "correct_answer": ">"
    },
    {
        "question": "What is the meaning of this symbol '<='?",
        "choices": ["less than or equal to","greater than or equal to","less than"],
        "correct_answer": "less than or equal to"
    },
    {
        "question": "What is the meaning of this symbol '=='",
        "choices": ["for declaring value","equal to","nor equal"],
        "correct_answer": "equal to"
    },
    {
        "question": "what is the symbol for Greater than or equal to?",
        "choices": ["<=","=>",">="],
        "correct_answer": ">="
    },
    {
        "question": "What is the symbol for Greater than?",
        "choices": ["<",">",">="],
        "correct_answer": ">"
    },
    {
        "question": "What is the symbol for Not equal to?",
        "choices": ["!=","=!","!"],
        "correct_answer": "!="
    },
    {
        "question": "Index starts at 0.",
        "choices": ["yes","no","maybe"],
        "correct_answer": "yes"
    },
    {
        "question": "Tuples are changeable.",
        "choices": ["yes","no","maybe"],
        "correct_answer": "no"
    },
    {
        "question": "Who developed Python?",
        "choices": ["Guido Von Rosum","Guido Van Rossum","Guiddo Van Rossum"],
        "correct_answer": "Guido Van Rossum"
    },
    {
        "question": "When did the development of Python started?",
        "choices": ["1970's","1980's","1990's"],
        "correct_answer": "1980's"
    },
    {
        "question": "These are Python's reserved words except;",
        "choices": ["then","is","for"],
        "correct_answer": "then"
    },
    {
        "question": "What is Control statement?",
        "choices": ["determines the control flow of a set of statements","determines the control flow of a set of variables","determines the control flow of a set of Data"],
        "correct_answer": "determines the control flow of a set of statements"
    },
    {
        "question": "The 'if' statement is used to implement the?",
        "choices": ["loop","decision","condition"],
        "correct_answer": "decision"
    },
    {
        "question": "The 'for' statement allows us to?",
        "choices": ["loop through a sequence of values","iterate through a sequence of values","execute through a sequence of values"],
        "correct_answer": "iterate through a sequence of values"
    },
    {
        "question": "The for loop is a?",
        "choices": ["indefinite loop","definite loop","nested loop"],
        "correct_answer": "definite loop"
    },

    
]