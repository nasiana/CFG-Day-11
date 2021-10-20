# EX 1.a - test with correct file path
file = open('test_file.txt', 'r')
print(file)

# EX 1.b - test with incorrect file path
# file = open('folder/test_file.txt', 'r')
# print(file)

# EX 1.c actually being able to see whats in the file
# stored the contents of the file into the variable content
content = file.read()
print(content)

# readline
file = open('test_file.txt', 'r')
# the parameter (bytes) seems to refer to characters in the text file including spaces
# if you execute it L1 first then L2 doesn't print anything as there is seemingly nothing left in the file to print
# print(file.readline())
# print L2 and L3 together means L3 will print the left over characters from the file after L2
print(file.readline(6))
print(file.readline())

# remember to always close the file or it can close many errors
file.close()

'''
# if a file exists already:
# w+ will override it (truncate it to length 0 - i.e. chop off the bits at the end until the length of the file is 0)
# r+ will not override the contents of the file so you can still read it
'''
'''
if a file does not exist:
# w+ will create a new file
# r+ will throw an error
'''

# experimenting with r+
file = open('test_file.txt', 'r+')
file.write("Now I have written over using r+")
file.close()

# experimenting with r+
file = open('test_file.txt', 'w+')
file.write("Now I have written over using w+")
file.close()

# writing a new file
file = open('my_new_file_for_writing.txt', 'w')
file.write("Frankly, my dear, I don't give a damn. (GONE WITH THE WIND)")
file.close()

# appending some more stuff to the file
movie_quotes = [
    "\nI'm gonna make him an offer he can't refuse. (THE GODFATHER)",
    "\nMay the Force be with you. (STAR WARS)",
    "\nThere's no place like home. (THE WIZARD OF OZ)",
]

# appending doesnt overwrite the file but instead adds more to the end of the file
movie_quotes = [
    "\nI'm gonna make him an offer he can't refuse. (THE GODFATHER)",
    "\nMay the Force be with you. (STAR WARS)",
    "\nThere's no place like home. (THE WIZARD OF OZ)",
]
file = open('my_new_file_for_writing.txt', 'a')  # NB 'a' mode for append

file.writelines(movie_quotes)
file.close()

# CONTEXT MANAGER

'''
Use the with statement to shorten code and make it more concise when file handling. Use with means that you/
don't need to add file.close() at the end of code. The file is automatically closed when executing 'with'.
'''

with open('people.txt', 'w+') as text_file:
    people = 'Nasian \n Maja \n Lana'
    text_file.write(people)

# alternative way to write it without the context manager

file = open('people.txt', 'w+')
try:
    file.write('Nasian \n Marwan \n Sara')
finally:
    file.close()

# reading
'''
Interesting behaviour, as I have previousled aliased using 'with open('people.txt', 'w+') as text_file', it seems/
that the following code will only work when I have 'as text_file' in the code. Without it I get
'''
with open('people.txt', 'r') as text_file:
    contents = text_file.read()
    print(contents)


# equivalent

file = open('people.txt', 'r')
try:
    print(file.read())
finally:
    file.close()

'''
Create a to-do list program that writes user input to a file
The program should:
- Ask the user to input a new to-do item
- Read the contents of the existing to-do items
- Add the new to do item to the existing to-do items
- Save the updated to-do items
Optional: You can create the new file either manually or using Python.
'''

# to-do programme
user = input('Input a new to-do item: ')

with open('to-do_items.txt', 'r') as ex1_file:
    contents_ex1 = ex1_file.read()
    print(contents_ex1)

with open('to-do_items.txt', 'a') as ex1_file:
# added the \n for a line break
    ex1_file.write('\n' + user)
    print(contents_ex1)

# experimenting with a+
# to-do programme
user = input('Input a new to-do item: ')
with open('to-do_items.txt', 'a+') as ex1_file:
    contents_ex2 = ex1_file.read()
    print(contents_ex2)
# added the \n for a line break
    ex1_file.write('\n' + user)
    print(contents_ex2)

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

import csv

# INDENTATION MATTERS
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


with open('5.3_example_one.txt', 'r') as read_file:
# x will store the contents of read_file in a readable format
    x = read_file.read()
    print(x)
# y splits x when strings are seperated by ' '
    y = x.split()
    print(y)
    count = 0
    filtered_list = [word for word in y if word == 'cat']
    for i in y:
        if i == 'cat':
            count +=1
    print(filtered_list)
    print(count)


#  EXAMPLE 1 -- sample solution

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

# #  SOLUTION 1 -- it is OK
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