#Word_Counting_2.py

# This program is supposed to count words in a text file
import os

# Print current working directory
print("Your current working directory is\n", os.getcwd())
directory_path_option = input("Would you like to change your directory? (y/n): ").lower()
if directory_path_option == 'y':
    try:
        enter_path = input("Please enter the path to your desired directory: ")
        os.chdir(enter_path)
        specific_contents = f"The file {enter_path} contains:\n"
        print(specific_contents)
        print(os.listdir())
    except FileNotFoundError:
        print("Invalid path. Please try again")
        enter_path = input("Please enter the correct path to your desired directory: ")
        os.chdir(enter_path)
else:
    print("continue in current program")

#print("The file Word_Counting 1.0 contains:\n", os.listdir())
# os.chdir("monty_python_sketches")

# Ask the user for the filename 
file_name = input("please enter the file name:\n")

# open the text file in read mode 
with open(file_name, "r") as file_connection:
    file_contents = file_connection.read()
print(file_contents)

# Asking the user to provide the input of the word they want to count within the text file
word_to_count = input("please enter the word to count:\n")
choice = input("Do you want the counting to be case insensitive? (y/n): ").lower()
if choice == 'y':
    case_sensitivity = file_contents.casefold().count(word_to_count.casefold())
    print(word_to_count.casefold())
else:
    case_sensitivity = file_contents.count(word_to_count)

print(word_to_count.casefold().count(" "))  
word_count = word_to_count.casefold().count(" ")

if word_count > 1:
    raise ValueError("The phrase exceeds two words, limit your entry to single words or two word phrases. Exiting Program.")
    exit()
elif word_count == 0:
    print("Standby")
else:
    print("searching...")

# output stating how many times the word occurs inside the given text file 
results = print("The word '", (word_to_count), "' was found", case_sensitivity, "times in this file:", (file_name))

# Writing the printed statement above within a new text file called "wordcount_result.txt"
with open("wordcount_result.txt", "w") as file_connection:
    file_connection.write("The word ")
    file_connection.write( word_to_count)
    file_connection.write(" was found ")
    file_connection.write(str(case_sensitivity))
    file_connection.write(" times in this file: ")
    file_connection.write(file_name)