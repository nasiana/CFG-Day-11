### DEMO 1 ###
"""
Demonstrate how to read file contents.

CHANGE the path to the location where your file called 'text_fle.txt' is saved
Note that you may need to change '\' to '\\' to espace symbols

Here is an example: file = open('C:\\Users\\olyan\\Desktop\\test_file.txt', 'r')

"""
file = open('C:\\path-to-the-file-location\\test_file.txt', 'r')

print(file) # What do we get?

"""
The file object returned by open() function is an object of type _io.TextIOWrapper. 

We need to use special methods to read/write data from/to this object. 
Let's go back to the slide deck to see how it is done.  
"""

### DEMO 2 ###
"""
Objective is to demonstrate how to read content(s) from a file object.

CHANGE the path to the location where your file called 'text_fle.txt' is saved
Note that you may need to change '\' to '\\' to espace symbols
Here is an example: file = open('C:\\Users\\olyan\\Desktop\\test_file.txt', 'r')
"""

file = open('C:\\path-to-the-file-location\\test_file.txt', 'r')

"""
Read() example
"""
content = file.read()  # NB: try passing a number as an arg. like read(3)
print(content)

"""
Readline() example
"""
content = file.readline()
print(content)

"""
Readline() example
"""
content = file.readlines()
print(content)

# alternatively try pretty print to see each file row on a new line

print('')
from pprint import pprint as pp
pp(content)

"""
IMPORTANT: now that we have finished our operations with the file, we must CLOSE it. 
Otherwise it would still be open and changes not save. 
Also others cannot access the file while it is open.
"""

# we need to run this

file.close()

### DEMO 3 ###
"""
Demonstrate how to write to a file

# CHANGE the path to the location where your file will be saved
# Note that you may need to change '\' to '\\' to espace symbols

"""

file = open('C:\\path-to-the-file-location\\NEW-FILE-NAME.txt', 'w')

file.write("Frankly, my dear, I don't give a damn. (GONE WITH THE WIND)")
file.close()

"""
Let's ADD more lines to the file
note the new line '\n'

CHANGE the path to the location where your file will be saved
"""

movie_quotes = [
    "\nI'm gonna make him an offer he can't refuse. (THE GODFATHER)",
    "\nMay the Force be with you. (STAR WARS)",
    "\nThere's no place like home. (THE WIZARD OF OZ)",
]

file = open('C:\\path-to-the-file-location\\NEW-FILE-NAME.txt', 'a')  # NB 'a' mode for append

file.writelines(movie_quotes)
file.close()

### EXERCISE 1 ###
"""
Create a to-do list program that writes user input to a file

The program should:

Ask the user to input a new to-do item
Read the contents of the existing to-do items
Add the new to do item to the existing to-do items
Save the updated to-do items

NB: You will need to manually create a new file called todo.txt in the same folder as your program before you start.
"""

# You solution here

"""
Example solution
"""
new_item = input('Enter a to-do item: ')

with open('todo.txt', 'r') as todo_file:
    todo = todo_file.read()

todo = todo + new_item + '\n'

with open('todo.txt', 'w+') as todo_file:
    todo_file.write(todo)

### DEMO 4 ###
"""
Writing and reading files using CSV library in Python.
"""

# Writing a csv

import csv

field_names = ['name', 'age']

data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28},
]

with open('team.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

    spreadsheet.writeheader()
    spreadsheet.writerows(data)

# ======================================
# Reading a CSV

import csv

with open('team.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))

### EXERCISE 2 ###
"""
This program is supposed to read data about trees from a file to find the shortest tree. 
Complete the program adding code to open 'trees.csv'.

The trees.csv file included with your student guides. 
Save the csv file in the same folder as your Python program!
"""

spreadsheet = # Add code to open the csv file

heights = []

for row in spreadsheet:
    tree_height = row['height']
    heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)

'''
Example Solution
'''
import csv

with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    heights = []

    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)

### EXERCISE 3 ###
"""
PROBLEM SOLVING WITH PYTHON --> 

Write a Python program to count the occurrences of a word in a text file.
Your program will take a word from the user and count the number of occurrences of that word in a file.

(use file: 5.3_example_one.txt, save this file in the same folder as your Python program! )
"""

##########################################################################################
# NB: solve this problem together with the group                                         #
# start with example one, it is a file without any punctuation, so it is easier to start #
# we solve one level of complexity and then move on to another                           #
##########################################################################################


fname = input("Enter file name: ")
search_word = input("Enter word to be searched:").lower()

count = 0

with open(fname, 'r') as text:
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to  lowercase to avoid case mismatch
        line = line.lower()

        # Split the line into words
        words = line.split()

        for word in words:
            if (word == search_word):
                count = count + 1

print("Occurrences of the word: " + search_word)
print(count)

"""
EXAMPLE 2

(!!! use file: 5.3_example_two.txt, save this file in the same folder as your Python program! )

We need to demonstrate that our first solution would not work with a file that has any punctuation. 
So try running file No 2 with our code to demonstrate that the result is wrong. 

Now we need to modify our solution to make it compatible with ANY file with or without punctuation. 

NB: there are two examples on how to solve EXAMPLE 2. Let's work with both of them. 
"""

#  SOLUTION 1 -- it is OK
#  file with punctuation (use file: 5.3_example_two.txt)
#  ------------------------------------------------------------

fname = input("Enter file name: ")
search_word = input("Enter word to be searched:").lower()

count = 0

with open(fname, 'r') as text:
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to  lowercase to avoid case mismatch
        line = line.lower()

        # NB: 'clean up' each word from the punctuation
        for char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            line = line.replace(char, "")

        # Split the line into words
        words = line.split()

        for word in words:
            if (word == search_word):
                count = count + 1

print("Occurrences of the word: " + search_word)
print(count)

#  SOLUTION 2 -- MUCH BETTER
#  file with punctuation (use file: 5.3_example_two.txt)
#  ------------------------------------------------------------

import string

fname = input("Enter file name: ")
search_word = input("Enter word to be searched:").lower()

count = 0

with open(fname, 'r') as text:
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to  lowercase to avoid case mismatch
        line = line.lower()

        # Remove the punctuation marks from the line
        line = line.translate(line.maketrans("", "", string.punctuation))  # much cleaner solution (we review this next)

        # Split the line into words
        words = line.split()

        for word in words:
            if (word == search_word):
                count = count + 1

print("Occurrences of the word: " + search_word)
print(count)

### DEMO 5 ###
"""
Review our solution for a previous exercise, namely

line = line.translate(line.maketrans("", "", string.punctuation))
"""

# import string
#
# """
# Let's build a translator
# 1. This uses the 3-argument version of str.maketrans
# 2. There are 3 arguments (x, y, z) where 'x' and 'y'must be equal-length strings and characters in 'x' are replaced by characters in 'y'.
# 3. 'z' is a string (string.punctuation here) where each character in the string is mapped to None
#
# """
# translator = str.maketrans('', '', string.punctuation)
#
# """
# This is an alternative that creates a dictionary mapping of every character from string.punctuation to None
# (this will also work)
#
# translator = str.maketrans(dict.fromkeys(string.punctuation))
# """
#
#
# s = 'This#! is a string, with-- all (sorts) of punctuation& that needs to be!!! cleaned up?'
#
# # pass the translator to the string's translate method.
# print(s.translate(translator))