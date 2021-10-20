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


#
equivalent

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
    ex1_file.write(user)
