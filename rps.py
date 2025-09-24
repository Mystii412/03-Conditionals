import random

print('Rock Paper Scissors')

round = 1
hmn_wins = 0
cpu_wins = 0


def get_valid_input():
    """Asks the player for an input (r,  p, s), then strips it and makes it lowercase."""
    global player_choice
    player_choice = 'yes'
    while True:
        if player_choice != 'r' and player_choice != 'p' and player_choice != 's':
            player_choice = input('Do you want to play Rock (r), Paper(p), or Scissors(s): ').strip().lower()
        else:
            global letter
            letter = player_choice
            break

def cpu_move():
    """Makes the variable 'cpu' a random value out of 'Rock', 'Paper', or 'Scissors'."""
    global cpu
    cpu_moves = ['Rock', 'Paper', 'Scissors']
    cpu = random.choice(cpu_moves)

def convert_letter_to_word(letter):
    """Converts the letter input to a word"""
    global pc
    if letter == 'r':
        pc = 'Rock'
    elif letter == 'p':
        pc = 'Paper'
    elif letter == 's':
        pc = 'Scissors'
    else :
        raise Exception("convert_letter_to_word(letter) - Invalid value passed in. Value must be \“r\”, \“p\” or \“s\”") 

    print(f"You picked {pc}.")
    print(f"The computer picked {cpu}.")

def print_results():
    """Prints the results of the game"""
    global hmn_wins
    global cpu_wins
    if pc == cpu:
        print('It\'s a tie.')
    elif pc == 'Rock' and cpu == 'Paper':
        print('You lose.')
        cpu_wins += 1
    elif pc =='Rock' and cpu == 'Scissors':
        print('You win.')
        hmn_wins += 1
    elif pc == 'Paper' and cpu == 'Rock':
        print('You win.')
        hmn_wins += 1
    elif pc == 'Paper' and cpu == 'Scissors':
        print('You lose.')
        cpu_wins += 1
    elif pc == 'Scissors' and cpu == 'Paper':
        print('You win.')
        hmn_wins += 1
    elif pc == 'Scissors' and cpu == 'Rock':
        print('You lose.')
        cpu_wins += 1


def final_score():
    """Prints the results of the entire series"""
    if hmn_wins > cpu_wins:
        print(f"You won, {hmn_wins} : {cpu_wins}")
    elif hmn_wins == cpu_wins:
        print(f"It's a tie. {hmn_wins} : {cpu_wins}")
    else:
        print(f"You lost, {hmn_wins} : {cpu_wins}")


def main():
    global rounds
    rounds = int(input('Input how many rounds you would like to play: '))
    while rounds > 0:
        get_valid_input()
        cpu_move()
        convert_letter_to_word(letter)
        print_results()
        rounds -= 1
    final_score()

if __name__ == '__main__':
    main()
