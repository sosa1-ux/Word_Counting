candies = ["Snickers", "Reese's", "Sour Punch", "Almond Joy", "Candy Corn"]

len(candies)
candies[0]

for index in range(len(candies)):
    print(f"{candies[index]}")
print(candies)

for index in range(len(candies)): 
    candies[index] = candies[index].lower()
print(candies)

candies = ["Snickers", "Reese's", "Sour Punch", "Almond Joy", "Candy Corn"]
print(candies)

candies_lowercase = candies
for index in range(len(candies_lowercase)):
    candies_lowercase[index] = candies_lowercase[index].lower()
print(candies_lowercase)
print(candies)

candies = ["Snickers", "Reese's", "Sour Punch", "Almond Joy", "Candy Corn"]
candies_lowercase = candies.copy()
for index in range(len(candies_lowercase)):
    candies_lowercase[index] = candies_lowercase[index].lower()
print(candies_lowercase)
print(candies)

candies_uppercase = []
for candy in candies:
    candies_uppercase.append(candy.upper())
print(candies_uppercase)
print(candies)

snicker_letters = []
for letter in candies[0]:
    snicker_letters.append(letter.upper())
print(snicker_letters)
print(candies)

for letter in candies[0]:
    print(letter.upper())

for index in range(len(candies[0])):
    print(candies[0][index].upper())

candies = ["Snickers", "Reese's", "Sour Punch", "Almond Joy", "Candy Corn"]
likes = [16, 16, 10, 6, 11]
mehs = [13, 10, 21, 9, 15]
dislikes = [4, 8, 1, 17, 6]

for index in range(len(candies)):
    print(f"{candies[index]} had {likes[index]} likes")

candy_votes = {
    "Snickers": (16, 13, 4),
    "Reese's": (16, 10, 8),
    "Sour Punch": (10, 21, 1),
    "Almond Joy": (6, 9, 17),
    "candy corn": (11, 15, 6),
}

for item in candy_votes.items():
    candy_name = item[0]
    likes, mehs, dislikes = item[1]  # Unpack the tuple into separate variables
    print(f"{candy_name} had {likes} likes, {mehs} mehs, and {dislikes} dislikes.")
