import random

def roll_dice(num=3):
    #Rolls the specified number of dice, returning a list of results.
    return random.choices([1, 2, 3, 4, 5, 6], k=num)

def play_turn(player_name):
    # example turn 
    dice = roll_dice()
    print(f"\n{player_name}'s turn. You rolled: {dice}")
    
    while True:
        if dice[0] == dice[1] == dice[2]:
            print(f"{player_name} tupled out! No points this turn.")
            return 0

        # fixed dice
        fixed = [die for die in set(dice) if dice.count(die) == 2]
        if fixed:
            print(f"Fixed dice: {fixed}")
        
        # re-roll option if not all dice are fixed
        unfixed = [die for die in dice if die not in fixed]
        if unfixed:
            print(f"Unfixed dice: {unfixed}")
            choice = input("Do you want to re-roll unfixed dice? (y/n): ").lower()
            if choice == "y":
                new_rolls = roll_dice(len(unfixed))  
                print(f"New rolls: {new_rolls}")
                
                # Update dice
                for i in range(len(dice)):
                    if dice[i] in unfixed:
                        dice[i] = new_rolls.pop(0) 
                
                print(f"Updated dice: {dice}")
                continue  # Continue with the updated dice
            elif choice == "n":
                print(f"You stopped with {dice}. Your score: {sum(dice)} points!")
                return sum(dice)
            else:
                TypeError 
                print("Please enter yes or no")

# Main game logic
if __name__ == "__main__":
    target_score = 50
    player_scores = [0, 0]  # Total scores for each player
    turn_scores = [[], []]  # History of scores for each player
    player_names = ["Player 1", "Player 2"]
    current_player = 0  # Index to track who turn it is

    print("Welcome to the 'Tuple Out' Dice Game!")
    print(f"The first player to reach {target_score} points wins!\n")

    # Main game loop
    while max(player_scores) < target_score:
        # Current player's turn
        player_name = player_names[current_player]
        turn_score = play_turn(player_name)
        
        # Update scores
        player_scores[current_player] += turn_score
        turn_scores[current_player].append(turn_score)
        
        print(f"{player_name}'s total score: {player_scores[current_player]}")
        
        if player_scores[current_player] >= target_score: # did player win? 
            print(f"\n{player_name} wins with a total score of {player_scores[current_player]}!")
            break
        else:
            current_player = 1 - current_player

    print("\nGame Over!")
    print(f"Final scores: {player_names[0]}: {player_scores[0]}, {player_names[1]}: {player_scores[1]}")
    print(f"{player_names[0]}'s turn scores: {turn_scores[0]}")
    print(f"{player_names[1]}'s turn scores: {turn_scores[1]}")