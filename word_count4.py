#word_count4.0

# This program is supposed to count words in a text file
import os
import sys
print(len(sys.argv))
from count_spaces import count_words

# Print current working directory
if len(sys.argv) >= 1:
    directory_path_option = sys.argv[1].lower()
else: 
    directory_path_option = input("Would you like to change your directory? (y/n): ").lower()

print("Your current working directory is\n", os.getcwd())
print(sys.argv[1])



if directory_path_option == 'y':
    if len(sys.argv) > 2:
        enter_path = sys.argv[2].lower()
    else:
        enter_path = input("Please enter the path to your desired directory: ")

    while True: #loop until user provides a valid path
        try:
            os.chdir(enter_path)
            specific_contents = f"The file {enter_path} contains:\n"
            print(specific_contents)
            print(os.listdir())
            break #exit loop if path is valid
        except FileNotFoundError:
            print("Invalid path. Please try again.")
            if len(sys.argv) <= 2:
                enter_path = input("Please enter the correct path to your desired directory: ")
            os.chdir(enter_path)
else:
    print("continue in current program")


#print("The file Word_Counting 1.0 contains:\n", os.listdir())
# os.chdir("monty_python_sketches")

# Ask the user for the filename or directory for word counting

if len(sys.argv) >= 3:
    word_to_count = sys.argv[3].lower()
else: 
    word_to_count = input("please enter the word to count:\n")

if len(sys.argv) > 4:
    choice = sys.argv[4].lower() 
else:
    choice = input("Do you want the counting to be case insensitive? (y/n): ").lower()

try:
    with open("wordcount_result.txt", "w") as file_connection:
        file_connection.write("")
    for file_name in os.listdir():
        with open(file_name, "r") as file_connection:
            file_contents = file_connection.read()
            if choice == 'y':
                case_sensitivity = file_contents.casefold().count(word_to_count.casefold())
            print(f"The word {word_to_count} was found {case_sensitivity} times in this file: {file_name}")
            with open("wordcount_result.txt", "a") as file_connection:
                file_connection.write("The word ")
                file_connection.write( word_to_count)
                file_connection.write(" was found ")
                file_connection.write(str(case_sensitivity))
                file_connection.write(" times in this file: ")
                file_connection.write(file_name)
                file_connection.write("\n")
    else: 
        for file_name in os.listdir():
            with open(file_name, "r") as file_connection:
                file_contents = file_connection.read()
            case_sensitivity = file_contents.count
except: 
    if choice == 'naw':
        exit()
    

#word_to_count = input("something: ")
print(word_to_count.casefold().count(" "))  
word_count = word_to_count.casefold().count(" ")
count_words(word_count)


# output stating how many times the word occurs inside the given text file 
#results = print("The word '", (word_to_count), "' was found", case_sensitivity, "times in this file:", (file_name))

# Writing the printed statement above within a new text file called "wordcount_result.txt"

print(sys.argv)
