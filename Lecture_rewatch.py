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

# remember to always close the file
file.close()

# experimenting with r+
file = open('test_file.txt', 'r+')
file.write("Now I have written over using r+")
file.close()

# experimenting with r+
file = open('test_file.txt', 'w+')
file.write("Now I have written over using w+")
file.close()

