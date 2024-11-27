# example using input()

import sys

if len(sys.argv) >= 3:
    # get values from command line
    word_to_repeat = sys.argv[1]
    times_to_repeat = sys.argv[2]
else:
    # get values from user
    word_to_repeat = input("What word or phrase would you like me to repeat?\n")
    times_to_repeat = input("How many times should I repeat it?\n")

# process values
word_to_repeat = word_to_repeat + " "
times_to_repeat = int(times_to_repeat)
string_to_print = word_to_repeat * times_to_repeat

# print results
print(string_to_print)
