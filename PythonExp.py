'''
1.Demonstrate about fundamental Data types in Python Programming. (i.e., int, float, complex, bool and string types)
'''

#int type
a = 5
print("Type of a: ", type(a))

#float type
b = 5.0
print("\nType of b: ", type(b))

#complex type
c = 2 + 4j
print("\nType of c: ", type(c))

# Boolean type
d = True
print("\nType of d: ", type(d))

#string type
e = "Python OP"
print("\nType of e: ", type(e))


'''
2.Demonstrate the working of following functions in Python. i) id( ) ii) type( ) iii) range( )
'''

#id()
x = ('apple', 'banana', 'cherry')
print(id(x))

#type()
print(type(x))

#range()
for i in range(len(x)):
    print(x[i])


'''
3.Demonstrate the following Operators in Python with suitable examples.
i) Arithmetic Operators
ii) Relational Operators
iii) Assignment Operator
iv) Logical Operators
v) Bit wise Operators
vi) Ternary Operator
vii) Membership Operators
viii) Identity Operators
'''

########################### Arithmetic Operators (+,-,*,/) ###########################
val1 = 2
val2 = 3
res = val1 + val2
print(res)


########################### Relational Operators (>,<,=) ###########################
a = 9
b = 5
print(a > b)


########################### Assignment Operators (=,+=,-=) ###########################
a = 3
b = 5

a += b
print(a)
a -= b
print(a)


########################### Logical Operators (AND, OR, NOT) ###########################
a = 10
b = 10
c = -10
  
if a > 0 and b > 0:
    print("The numbers are greater than 0")
  
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")


########################### Bitwise operations (&,|,~.^,>>,<<) ###########################
a = 10
b = 4
 
# Print bitwise AND operation
print("a & b =", a & b)
# Print bitwise OR operation
print("a | b =", a | b)
# Print bitwise NOT operation
print("~a =", ~a)
# print bitwise XOR operation
print("a ^ b =", a ^ b)

a = 10
b = -10
 
# print bitwise right shift operator
print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)
a = 5
b = -10
# print bitwise left shift operator
print("a << 1 =", a << 1)
print("b << 1 =", b << 1)


########################### Ternary Operators (if-else) ###########################
a, b = 10, 20

min = a if a < b else b
print(min)


########################### Membership Operators (in, not in) ###########################
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if (a in list):
   print("Line 1 - a is available in the given list")
else:
   print("Line 1 - a is not available in the given list")

if (b not in list):
   print("Line 2 - b is not available in the given list")
else:
   print("Line 2 - b is available in the given list")

a = 2
if (a in list):
   print("Line 3 - a is available in the given list")
else:
   print("Line 3 - a is not available in the given list")


########################### Identity Operators (is, is not) ###########################
x = '101'
y = '101'
z = '102'
if (x is y):
  print ('x is y')
else:
  print ('x is not y')
if (x is z):
  print('x is z')
else:
  print ('x is not z')
if (y is z):
  print('y is z')
else:
  print ('y is not z')


'''
4.Demonstrate the following Conditional statements in Python with suitable examples. i) if 
statement ii) if else statement iii) if – elif – else statement
'''

string ="Python"

if string == "Py":
    print ("The first condition is true")

elif string == "Pthon":
    print("The second condition is true")

elif string == "Pytho":
    print("The third condition is true")

elif string=="Python":
    print("The fourth condition is true")

else:
    print ("All the above conditions are false")


'''
Demonstrate the following Iterative statements in Python with suitable examples. i) while 
loop ii) for loop
'''

########################### While Loop ###########################
i = 1
n = 10

while i <= n:
    print(i)
    i = i + 1



########################### For Loop ###########################
values = range(10)

for i in values:
    print(i)

'''
5.Demonstrate the following control transfer statements in Python with suitable examples. i) 
break ii) continue iii) pass
'''

########################### Break ###########################

while True:
       age = int(input("Please enter your age:"))
       if age >= 18:
              break
       else:
             print("You’re not eligible to vote")


########################### Continue ###########################
for letter in 'Python ': 
    if letter == ' ': 
        continue 
    print ('Letters: ', letter)


########################### Pass ###########################
for letter in 'Programming': 
    if letter == 'x': 
        pass 
    print ('Letters: ', letter)


'''
6.Write Python programs to print the following Pattern alphabet pyramid
'''

import math

rows= int(input("Enter number of rows brother: "))
# outer loop for ith row
for i in range (0,rows+1):
    if i == 0:
        continue
    asciichr = 65
    for space in range(rows-i+1): 
       print(' ',end=' ')

    # inner loop for jth columns
    for j in range(1, i+1):
        char = chr(asciichr)
        print(char+' ' ,end=" ")
        asciichr += 1

    print()


'''
7.Write Python programs to print the following Pattern Number half diamond
'''

rows = int(input("Enter number of rows: "))

#uppar ka traingle
for i in range(rows+1):
    for j in range(rows-i,rows+1):
        print(j,end='')
    print("\t")

#neeche ka triangle
for i in range(0, rows):
    for j in range(i+1,rows+1):
        print(j,end='')
    print("\t")



'''
8.Write Python programs to print the following Pattern Alphabet diamond
'''

rows = int(input("Enter number of rows: "))

for i in range(rows,1,-1):
    for space in range(i): 
        print(' ', end="")
    for j in range(i,rows+1):
        print(chr(j+64),end=" ")
    print("")

for i in range(1, rows+1):
    for space in range(i): 
        print(' ', end="")
    for j in range(i,rows+1):
        print(chr(j+64),end=" ")
    print("")


'''
9.Python program to perform read and write operations on a file.
'''

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


'''
10. Python program to copy the contents of a file to another file.
'''

# open both files
'''
Isse phele bana lena dono files bhai
'''
with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile:
    for line in firstfile:
        secondfile.write(line)


'''
11.Python program to count frequency of characters in a given file
'''

import collections
import pprint
file_input = input('File Name: ')
with open(file_input, 'r') as info:
  count = collections.Counter(info.read().upper())
  value = pprint.pformat(count)
print(value)


'''
12.Python program to print each line of a file in reverse order.
'''

filename=input("Enter file name: ")
for line in reversed(list(open(filename))):
    print(line.rstrip())


'''
13.Python program to compute the number of characters, words and lines in a file
'''

file__IO ="<file path>"

with open(file__IO, 'r') as f:
    data = f.read()
    line = data.splitlines()
    words = data.split()
    spaces = data.split(" ")
    charc = (len(data) - len(spaces))

print('\n Line number ::', len(line), '\n Words number ::', len(words), '\n Spaces ::', len(spaces), '\n Characters ::', (len(data)-len(spaces)))


'''
14.Demonstrate the following functions/methods which operates on lists in Python with suitable 
examples: i) list( ) ii) len( ) iii) count( ) iv) index ( ) v) append( ) vi) insert( ) vii) extend() viii) 
remove( ) ix) pop( ) x) reverse( ) xi) sort( ) xii) copy( ) xiii) clear( )
'''

import random

text = 'Python'

text_list = list(text)
print("List: ", text_list)
print("Lnegth of list: ", len(text_list))
print("Count of 'P' in list: ", text_list.count('P'))
print("Index of 'y' in list: ", text_list.index('y'))

text_list.append('s')
print("List after appending: ", text_list)

text_list.insert(0, 'A ')
print("List after inserting: ", text_list)

list_2 = [1,2,3]
text_list.extend(list_2)
print("List after extending: ",text_list)

text_list.remove('A ')
print("List after removing: ", text_list)

text_list.pop()
print("List after poping: ", text_list)

text_list.reverse()
print("List after reversing: ", text_list)

num_list = []
for i in range(0, 10):
    num_list.append(random.randint(0,10))
num_list.sort()
print("List after sorting: ", num_list)

text_list_2 = text_list.copy()
print("List after copying: ", text_list_2)

text_list_2 = text_list.clear()
print("List after clearing: ", text_list_2)



'''
15.Demonstrate the following functions/methods which operates on tuples in Python with 
suitable examples: i) len( ) ii) count( ) iii) index( ) iv) sorted( ) v) min ( ) vi)max( ) vii) cmp( ) viii) 
reversed( )
'''

text = 'Python'

text_tuple = tuple(text)
print("Tuple: ", text_tuple)
print("Lnegth of list: ", len(text_tuple))
print("Count of 'P' in tuple: ", text_tuple.count('P'))
print("Index of 'y' in tuple: ", text_tuple.index('y'))

tuple_ = (5, 2, 24, 3, 1, 6, 7)  
sorted_ = tuple(sorted(tuple_))  
print("Tuple after sortings: ", sorted_)

print("Minimum element in tuple: ", min(tuple_,))
print("Maximum element in tuple: ", max(tuple_,))

# cmp() doesn't exist in Python 3.0 so we will make a cmp function for this
def cmp(a, b):
    return (a > b) - (a < b) 

tuple1, tuple2 = (123, 'xyz'), (456, 'abc')

print(cmp(tuple1, tuple2))
print(cmp(tuple2, tuple1))

reversed_ = tuple(reversed(tuple_))
print("Tuple after reversing: ", reversed_)



'''
16.Demonstrate the following functions/methods which operates on sets in Python with suitable 
examples: i) add( ) ii) update( ) iii) copy( ) iv) pop( ) v) remove( ) vi)discard( ) vii) clear( ) viii) 
union() ix) intersection( ) x) difference( )
'''

## add()
my_set = {1, 2, 3}
# Use add() to add an element to the set
my_set.add(4)
# The set now contains 1, 2, 3, and 4
print(my_set)


## update()
my_set = {1, 2, 3}
# Use update() to add multiple elements to the set
my_set.update([4, 5, 6])
# The set now contains 1, 2, 3, 4, 5, and 6
print(my_set)


##copy()
my_set = {1, 2, 3}
# Use copy() to create a copy of the set
new_set = my_set.copy()
# The new set contains the same elements as the original set
print(new_set)


## union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Create the union of the two sets using the "|" operator
union_set = set1 | set2 ## or use union() in place of | operator
# The union set contains all the elements from both sets
print(union_set)  # Output: {1, 2, 3, 4, 5}


##intersection()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Create the intersection of the two sets using the "&" operator
intersection_set = set1 & set2 ## or use intersection() in place of & operator
# The intersection set contains only the elements that are present in both sets
print(intersection_set)  # Output: {3}


## difference()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Create the difference of the two sets using the "-" operator
difference_set = set1 - set2 ## or use difference() in place of - operator
# The difference set contains only the elements that are present in set1 but not set2
print(difference_set)  # Output: {1, 2}



'''
18.Write a Regular Expression to represent all language identifiers. 
Rules: 
1. The allowed characters are a-z, A-Z,0-9, #. 
2. The first character should be a lower case alphabet symbol from a to k. 
3. The second character should be a digit divisible by 3. 
4. The length of identifier should be at least 2.
Write a python program to check whether the given string is RGM language identifier or not?
'''

import re

def is_rgm_identifier(s: str) -> bool:
    regex = r"^[a-k][0369][a-zA-Z0-9#]*$"

    return bool(re.match(regex, s))


print(is_rgm_identifier("a3"))    # True

##Aise 5-6 examples aur bata dena.


'''
19.Write a Regular Expression to represent all 10 digit mobile numbers. 
Rules: 
1. Every number should contains exactly 10 digits. 
2. The first digit should be 7 or 8 or 9 
Write a Python Program to check whether the given number is valid mobile number or not?
'''

import re

def is_valid_mobile_number(number):
  # Compile the regular expression
  pattern = re.compile(r"^[7-9][0-9]{9}$")
  
  # Use the `search` method to search for a match
  # in the given string
  match = pattern.search(number)
  
  # If the match is not `None`, the number is valid
  if match:
    return True
  else:
    return False

# Test the function
print(is_valid_mobile_number("12897834567890"))  # False
print(is_valid_mobile_number("9865432100"))  # True



'''
20.A positive integer n is said to be perfect if the sum of the factors of n, other than n itself, add 
up to n. For instance, 6 is perfect since the factors of 6 are {1,2,3,6} and 1+2+3=6. Likewise, 28 
is perfect because the factors of 28 are {1,2,4,7,14,28} and 1+2+4+7+14=28.
Write a Python function perfect(n) that takes a positive integer argument and returns True if 
the integer is perfect, and False otherwise
'''

def perfect(n):
      # Compute the sum of the factors of n, other than n itself
  sum = 0
  for i in range(1, n):
    if n % i == 0:
      sum += i

  # Return True if the sum equals n, and False otherwise
  return sum == n

# Test the function
print(perfect(6))   # True
print(perfect(28))  # True
print(perfect(29))  # False



'''
21.Implement a recursive function to solve tower of Hanoi Problem. Implement lambda function 
to find greater of the 2 input numbers
'''

def tower_of_hanoi(n, source, destination, auxiliary):
  if n == 1:
    print(f"Move disk 1 from {source} to {destination}")
    return

  tower_of_hanoi(n-1, source, auxiliary, destination)
  print(f"Move disk {n} from {source} to {destination}")
  tower_of_hanoi(n-1, auxiliary, destination, source)

# Test the function
tower_of_hanoi(3, "A", "B", "C")

## lambda function wala q
greater = lambda x, y: x if x > y else y

print(greater(3, 5))  # 5
print(greater(10, 4)) # 10



'''
22.Using map function perform element wise addition of elements of two lists. Using map and 
filter find the cube of all the odd numbers from the given input list
'''

# Define the two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Use the `map` function to add the elements of the two lists
result = list(map(lambda x, y: x+y, list1, list2))

# Print the result
print(result)  # [5, 7, 9]

##cube of odd numbers in two lists
# Define the input list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use the `filter` function to get only the odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Use the `map` function to compute the cubes of the odd numbers
cubes = list(map(lambda x: x**3, odd_numbers))

# Print the result
print(cubes)  # [1, 27, 125, 343]



'''
23.Classes: Employee, Developer, Tester, Manager
Developer, tester, Manager inherit Employee
Manager handles Developer, tester
Manager class: implement functions to add Developer/Tester and Remove Developer/ Tester
Display: to see the list of employees he manages
'''

class Employee:
      def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Developer(Employee):
  def __init__(self, name, salary, skills):
    super().__init__(name, salary)
    self.skills = skills


class Tester(Employee):
  def __init__(self, name, salary, experience):
    super().__init__(name, salary)
    self.experience = experience


class Manager(Employee):
  def __init__(self, name, salary, employees=None):
    super().__init__(name, salary)
    if employees is None:
      self.employees = []
    else:
      self.employees = employees

  def add_employee(self, employee):
    self.employees.append(employee)

  def remove_employee(self, employee):
    self.employees.remove(employee)

  def display_employees(self):
    for employee in self.employees:
      print(f"{employee.name} ({type(employee).__name__})")

# Test the classes
dev1 = Developer("John", 10000, ["Java", "Python"])
dev2 = Developer("Jane", 12000, ["JavaScript", "C++"])
tester1 = Tester("Mike", 9000, 2)
tester2 = Tester("Emily", 8500, 3)
manager = Manager("Sam", 15000, [dev1, tester1])

manager.add_employee(dev2)
manager.add_employee(tester2)
manager.display_employees()



'''
24.Display and handle at least 5 inbuilt exceptions: (Value error, Arithmetic Error). Create a user 
defined exception handling mechanism
'''
##Zero division 
try:
    x = 1 / 0
except ZeroDivisionError:
    print("You cannot divide a number by zero!")

##Value Error
try:
    x = int("hello")
except ValueError:
    print("Invalid input! Please provide an integer.")


##TypeError
try:
    x = "hello" + 5
except TypeError:
    print("Invalid operation! You cannot concatenate a string and an integer.")

##NameError
try:
    print(x)
except NameError:
    print("Unknown variable! Please make sure the variable has been defined.")


##indexerror
try:
    x = [1, 2, 3]
    print(x[3])
except IndexError:
    print("Invalid index! Please provide an index that is within the range of the sequence.")



'''
25.##Zero division 
try:
    x = 1 / 0
except ZeroDivisionError:
    print("You cannot divide a number by zero!")

##Value Error
try:
    x = int("hello")
except ValueError:
    print("Invalid input! Please provide an integer.")


##TypeError
try:
    x = "hello" + 5
except TypeError:
    print("Invalid operation! You cannot concatenate a string and an integer.")

##NameError
try:
    print(x)
except NameError:
    print("Unknown variable! Please make sure the variable has been defined.")


##indexerror
try:
    x = [1, 2, 3]
    print(x[3])
except IndexError:
    print("Invalid index! Please provide an index that is within the range of the sequence.")
'''

# Take 10 numbers from the user and save them to a file
# numbers = []
# for i in range(10):
#   number = input(f"Enter number {i+1}: ")
#   numbers.append(number)

# with open("t1.txt", "w") as f:
#   for number in numbers:
#     f.write(f"{number}\n")

# # Read the contents of the file, sort the data, and save it to a different file
# with open("t1.txt", "r") as f:
#   numbers = [int(x) for x in f.read().split()]

# numbers.sort()

# with open("t2.txt", "w") as f:
#   for number in numbers:
#     f.write(f"{number}\n")


## part 2
import re

# Read the contents of the file
with open("textfile.txt", "r") as f:
  data = f.read()

# Compile the regular expressions
name_regex = re.compile(r"^(Mr|Ms|Mrs)\.[\s\w]+")
website_regex = re.compile(r"(https?://)?(www\.)?(\w+\.\w+)")
email_regex = re.compile(r"\w+@\w+\.\w+")
phone_regex = re.compile(r"\d{3}[-*]\d{3}[-*]\d{2,4}")

# Find the names of the users
names = name_regex.findall(data)
print("Names of the users:")
print(names)

# Find the website names excluding http/s
websites = website_regex.findall(data)
print("\nWebsite names excluding http/s:")
print(websites)

# Find the email IDs
emails = email_regex.findall(data)
print("\nEmail IDs:")
print(emails)

# Find the phone numbers
phones = phone_regex.findall(data)
print("\nPhone numbers:")
print(phones)



'''
26.Implement the following queries using menu driven approach:
Create Table
Insert values
Delete a row based on values
Display the rows of the table
Update the values of a specific row
'''

import mysql.connector;

mydb  = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'pass@123',
    database = 'comder'
);

if mydb:
    print('Succesfully connected to MySQL')

currentObj = mydb.cursor()

# createQuery = f'create table student (rollno int, name varchar(255), city varchar(255), division char(255))'
# currentObj.execute(createQuery)

print('1. Create Table \n2. Display Table \n3. Insert Data \n4. Update Data \n5. Delete Data \n6. Search Data');
choice = int(input('Your Choice: '))

if choice == 1:
    print('Table created')
elif choice == 2:
    tableName = str(input('Enter table name: '))
    query = f'SELECT * FROM {tableName}'
    currentObj.execute(query)
    print(currentObj.fetchall())
elif choice == 3:
    tableName = str(input('Enter table name: '))
    rollno = int(input('Enter roll no: '));
    name = str(input('Enter name: '));
    city = str(input('Enter city: '));
    division = str(input('Enter division: '))
    query = f'INSERT INTO {tableName} (rollno, name, city, division) VALUES (%s, %s, %s, %s)'
    val = (rollno, name, city, division);
    currentObj.execute(query, val);
    mydb.commit();
    print('Record Inserted');
elif choice == 4:
    table = str(input('Enter table name to update in: '));
    rollno = str(input('Enter roll no of record to update: '));
    name = str(input('Enter name: '));
    city = str(input('Enter city: '));
    division = str(input('Enter division: '));
    query = f"UPDATE {table} SET name = '{name}', city = '{city}', division = '{division}' WHERE rollno = {rollno}"
    currentObj.execute(query);
    mydb.commit();
    print('Record Updated');
elif choice == 5:
    table = str(input('Enter table name to delete from: '));
    rollno = str(input('Enter roll no of record to delete: '));
    query = f"DELETE FROM {table} WHERE rollno = {rollno}";
    currentObj.execute(query);
    mydb.commit();
    print('Record Deleted');
elif choice == 6:
    table = str(input('Enter table name to search: '));
    rollno = str(input('Enter roll no of record to search: '));
    query = f'SELECT * FROM {table} WHERE rollno = {rollno}'
    currentObj.execute(query);
    print(currentObj.fetchall())



'''
27. Implement a client server communication application based on socket Programming.
'''

import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# Connect to the server using the port
s.connect(('127.0.0.1', port))

# Send a message to the server
message = "Hello from the client!"
s.send(message.encode())

# Receive data from the server
data = s.recv(1024)
print("Received from the server:", data.decode())

# Close the connection
s.close()



'''
28.Design a GUI application to show input and output operations using Tkinter.
'''

import tkinter as tk

# Create the root window
root = tk.Tk()

# Create a label to show a prompt for user input
label = tk.Label(root, text="Enter a number:")
label.pack()

# Create an input field for the user to enter a number
input_field = tk.Entry(root)
input_field.pack()

# Create a function that will be called when the user clicks the "Show result" button
def show_result():
    # Get the value entered in the input field
    input_value = input_field.get()

    # Convert the input value to an integer
    input_value = int(input_value)

    # Calculate the result of the operation
    result = input_value * 2

    # Create a label to show the result
    result_label = tk.Label(root, text=f"Result: {result}")
    result_label.pack()

# Create a button that will call the show_result function when clicked
button = tk.Button(root, text="Show result", command=show_result)
button.pack()

# Start the main event loop
root.mainloop()



'''
29. Using pandas:
 Show various operations using dataframe to read data, clean data and analyse data.
 Create own dataframe
 Read csv
 Delete NA values from the dataframe (all NA and NA values of specific columns)
 Fill NA values with random values, mean, median)
 display statistical information of the data frame
'''

import pandas as pd

# Create a dataframe from a csv file
df = pd.read_csv('fifa_world_cup_2022_tweets.csv')

# Display the first few rows of the dataframe
print(df.head())

# Delete rows with NA values in any column
df.dropna(inplace=True)

# Delete rows with NA values in specific columns
df.dropna(subset=['Date Created', 'Source of Tweet'], inplace=True)

# Fill NA values with random values
df.fillna(value=pd.np.random.randn(), inplace=True)

# Fill NA values with the mean of the column
df.fillna(value=df.mean(), inplace=True)

# Fill NA values with the median of the column
df.fillna(value=df.median(), inplace=True)

# Display statistical information about the dataframe
print(df.describe())



'''
30.Using matplotlib
 plot following graphs
 Barchart
 Piechart
 Scatter plot
 Histogram
'''

##BAR
import matplotlib.pyplot as plt

# x-coordinates of the bars
x = [1, 2, 3, 4, 5]

# heights of the bars
heights = [10, 20, 30, 40, 50]

# create the bar chart
plt.bar(x, heights)

# show the plot
plt.show()

##PIE
import matplotlib.pyplot as plt

# sizes of each slice of the pie
sizes = [10, 20, 30, 40, 50]

# labels for each slice of the pie
labels = ['A', 'B', 'C', 'D', 'E']

# create the pie chart
plt.pie(sizes, labels=labels)

# show the plot
plt.show()

##scatter
import matplotlib.pyplot as plt

# x-coordinates of the points
x = [1, 2, 3, 4, 5]

# y-coordinates of the points
y = [10, 20, 30, 40, 50]

# create the scatter plot
plt.scatter(x, y)

# show the plot
plt.show()

##HISTOGRAM
import matplotlib.pyplot as plt

# values to be plotted in the histogram
values = [10, 20, 30, 40, 50]

# create the histogram
plt.hist(values)

# show the plot
plt.show()

##




