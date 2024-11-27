# **User Manual to Amanda's Word Count 4.0 Program**

**Description:**

**Word Count 4.0 is a Python program that counts the amount of times an entered word occurs in text files within a given directory determined by the user. It allows for both case sensitive and insensitive counting and it also writes the results to a textfile called 'wordcount_result.txt'.**

**How to Use:**

1. **Download the program files**: Ensure that both the 'word_count4.py' and 'count_spaces.py' are in the same directory/folder.

2. **Prepare your directory**: Specify the path to a different directory when running the program if you so desire. Otherwise specify whether you'd like to continue in the current program. 

3. **Run the program**: Open a terminal, navigate to the directory where the files are located, and run the program using the following command:

- **[directory_path]**: Optional. The path to the directory containing the `.txt` files you want to analyze. If not specified, the program will work in the current directory.

- **[word_to_count]**: Required. The word you want to count. Make sure it does not exceed two words. 

- **[case_sensitive_choice]**: Optional. Choose whether the word count should be case-sensitive. Enter `y` for case-insensitive counting, or `n` for case-sensitive counting.

4. **Check the results**: Once the program finishes running, it will create a file called `wordcount_result.txt` in the same directory. This file will contain the count of the entered word in each file.

5. **Review the output**: The program will also display the word counts in the terminal/command prompt as it processes each file.

## Example Output

If you run the program with a word to count (`example`), it might display something like: The word 'example' was found 5 times in this file: pet_shoppe.txt

**Why README:**
The readme is useful since it walks the user through the application step by step, giving them information on how to install and execute it. This makes it easier to understand its functionality and avoids confusion. Without it, users may have difficulty understanding command arguments, choosing a directory, or dealing with case sensitivity for word counting. The user could run into problems if they are unaware that .txt files are supported or if the directory path is incorrect. The readme facilitates the process of using the program overall. 






