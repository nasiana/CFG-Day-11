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
print(os.getcwd())


# You solution here
new_to_do = input("input a new to-do item")

with open('C:/Users/owned/Documents/CFG_Nanodegree/CFG-Day-11 (Python foundation 5)/to-do_items.txt', 'r') as to_do:
    todo2 = to_do.read()

todo2 = todo2 + new_to_do + '\n'

with open('C:/Users/owned/Documents/CFG_Nanodegree/CFG-Day-11 (Python foundation 5)/to-do_items.txt', 'w+') as to_do:
    to_do.write(new_to_do)

file = open('C:/Users/owned/Documents/CFG_Nanodegree/CFG-Day-11 (Python foundation 5)/to-do_items.txt', 'r')
content2 = file.read()
print(content2)
file.close()

# SOLUTION FROM SLACK

new_item = input('Enter a to-do item: ')

with open('C:/Users/owned/Documents/CFG_Nanodegree/CFG-Day-11 (Python foundation 5)/to-do_items.txt', 'r') as todo_file:
    todo = todo_file.read()

todo = todo + new_item + '\n'

with open('C:/Users/owned/Documents/CFG_Nanodegree/CFG-Day-11 (Python foundation 5)/to-do_items.txt', 'w+') as todo_file:
    todo_file.write(todo)

file = open('C:/Users/owned/Documents/CFG_Nanodegree/CFG-Day-11 (Python foundation 5)/to-do_items.txt', 'r')
content = file.read()
print(content)
file.close()


### EXERCISE 2 ###
"""
This program is supposed to read data about trees from a file to find the shortest tree. 
Complete the program adding code to open 'trees.csv'.

The trees.csv file included with your student guides. 
Save the csv file in the same folder as your Python program!
"""

import csv

with open('trees.csv', r) as csv_file:
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
