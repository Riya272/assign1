#Question1. Write a program that takes two numbers as input and prints their sum.

input1 = int(input("enter 1st number:"))
input2 = int(input("enter 2nd number:"))
print("Sum is ",input1 + input2)

#Question2. Write a python program that checks whether a given number is even or odd.

input_2 = int(input("enter a number:"))
if(input_2 %2==0):
    print("Even")
else:
    print("Odd")

#Question3. Write a python program that calculates the factorial of a given number.

fact = int(input("Enter a number:"))
i = 1
factorial = 1
while(i<=fact):
    factorial = i*factorial
    i = i+1

print(factorial)

#Question4. Write a program that asks the user for their name and then prints a greeting message.

name = input("Enter your name:")
print("good morning",name)

#Question5. Write a program that takes a string input from the user and writes it to a text file.

samplefile =open('C:/Users/hp/Desktop/python internship/demo.txt.docx','w')
stringinput = input("enter a string:")
print(stringinput, file=samplefile)
samplefile.close()

#Question6. Write a program that reads the content of a text file and prints it to the console.

samplefile =open('C:/Users/hp/Desktop/python internship/demo.txt.docx','r')
print(samplefile.read())
samplefile.close()

#Question7. Write a python program that takes a string as input and returns its length.

str_7 = input("Enter a string:")
print(len(str_7))

#Question8. Write a python program that concatenates two strings and returns the result.

strr1 = input("enter string1:")
strr2 = input("enter string2:")
print(strr1+" "+strr2)

#Question9. Write a python program that checks if a substring is present in a given string.

strr_9 = input("enter a string:")
substr = input("enter a substring:")
if(substr in strr_9):
    print("substring is present in a given string")
else:
    print("substring is not present in a given string")

#Question10. Write a python program that converts a given string to uppercase.

str_10 = input("enter a string")
print(str_10.upper())

#Question11. Write a python program that generates the first n numbers in the Fibonacci sequence.

n = int(input("enter a number:"))
a = 0
b = 1
if(n > 0):
    print(a)
if(n > 1):
    print(b)
for i in range(2,n):
    c=a+b
    print(c)
    a,b=b,c

#Question12. Write a python program that calculates the sum of the digits of a given number.

number = int(input("enter a number:"))
sum_of_digits=0
while(number >0):
    digit = number%10
    sum_of_digits = sum_of_digits + digit
    number = number//10

print(sum_of_digits)

#Questioon13. Write a program that asks the user for their birth year and calculates their age.

birthyear = int(input("enter birth year:"))
print(2024-birthyear)

#Question14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
print("Enter multiple lines of text (enter an empty line to finish):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("\nYou entered:")
for line in lines:
    print(line)

#Question15. Write a program that reads data from a CSV file and prints it to the console.

import csv

file_path = 'C:/Users/hp/Desktop/python internship/csv file read demo.csv'

try:
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(', '.join(row))
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

#Question16. Write a program in python that counts the frequency of each character in a string.

input_string_16 = input("enter a string:")

frequency_dict = {}

# Iterate over each character in the string
for char in input_string_16:
    # If the character is already in the dictionary, increment its count
    if char in frequency_dict:
        frequency_dict[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        frequency_dict[char] = 1

# Print the frequency of each character
print(frequency_dict)

#Question17. Write a program in python that converts a given string to title case (first letter of each word capitalized).

inputstring_17  = input("enter a string:")
print(inputstring_17.title())

#Question18. Write a python program that checks if two strings are anagrams of each other.

inputstring1_18 = input("enter string1:")
inputstring2_18 = input("enter string2:")

frequency_dict1= {}

# Iterate over each character in the string
for char in inputstring1_18:
    # If the character is already in the dictionary, increment its count
    if char in frequency_dict1:
        frequency_dict1[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        frequency_dict1[char] = 1

frequency_dict2 = {}

# Iterate over each character in the string
for char in inputstring2_18:
    # If the character is already in the dictionary, increment its count
    if char in frequency_dict2:
        frequency_dict2[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        frequency_dict2[char] = 1

if(frequency_dict1 == frequency_dict2):
    print("anagrams")
else:
    print("not anagrams")

#Question19. Write a python program that removes all punctuation from a given string.

input_string_19 = input("enter a string:")

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

result_string = ""

for char in input_string_19:
    # If the character is not a punctuation, add it to the result string
    if char not in punctuation:
        result_string += char

print(result_string)

#Question20. Write a python program that takes a list of numbers and returns their sum.

input_string = input("Enter a list of integers separated by spaces: ")

integer_list = list(map(int, input_string.split()))
sum_20 = 0
for i in integer_list:
    sum_20 = sum_20 + i

print("sum is:",sum_20)

#Question21. Write a python program that counts the occurrences of a specific element in a list.

input_lst_21 = input("enter a list:")

frequency_dict_21 = {}


for char in input_lst_21:
    # If the character is already in the dictionary, increment its count
    if char in frequency_dict_21:
        frequency_dict_21[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        frequency_dict_21[char] = 1

print(frequency_dict_21)

#Question22. Write a python program that returns the minimum and maximum values in a list of numbers.

input_lst_22 = input("enter a list:")
minimum = min(input_lst_22)
maximum = max(input_lst_22)
print("minimum is", minimum ,"and maximum is ", maximum)

#Question23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

celsius = int(input("enter celsius temperature:"))
fahren_23 = (celsius * 9/5) + 32
print("fahrenheit temperature is :",fahren_23)
fahrenheit = int(input("enter fahrenheit temperature:"))
cel_23 = (fahrenheit - 32) * 5/9
print("celsius temperature is :",cel_23)

#Question24. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.

num1_24 = int(input("enter 1st number:"))
num2_24 = int(input("enter 2nd number:"))
operator_24 = input("enter operator:")

if (operator_24 == '+'):
    print(num1_24+num2_24)
elif(operator_24 == '-'):
    print(num1_24 - num2_24)
elif(operator_24 == '*'):
    print(num1_24*num2_24)
elif(operator_24 == '/'):
    print(num1_24/num2_24)
else:
    print("choose appropriate operator")

#Question25. Write a program that copies the contents of one text file to another.

# Specify the paths of the source and destination files
source_file_path = "C:/Users/hp/Desktop/python internship/demo file text.txt.docx"
destination_file_path = "C:/Users/hp/Desktop/python internship/copy of demo file text.txt.docx"

# Open the source file in read mode
with open(source_file_path, 'r', encoding='utf-8', errors='ignore') as source_file:
    contents = source_file.read()

    # Open the destination file in write mode
with open(destination_file_path, 'w', encoding='utf-8', errors='ignore') as destination_file:
    # Write the contents to the destination file
    destination_file.write(contents)

print(f"Contents copied from {source_file_path} to {destination_file_path} successfully.")


#Question26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.

string_26 = input("Enter the string: ")
prefix_26 = input("Enter the prefix to check: ")
suffix_26 = input("Enter the suffix to check: ")
if (string_26.startswith(prefix_26)):
    print("The string starts with the prefix")
else:
    print("The string does not start with the prefix")

if(string_26.endswith(suffix_26)):
    print("The string ends with the suffix")
else:
    print("The string does not end with the suffix")

#Question27. Write a program in python that converts a string into a list of its characters.

string_27 = input("enter a string:")
print(list(string_27))