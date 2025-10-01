import random


def higher_lower():
    """Sets tries to 0, and asks the user for a number, if higher or lower, it will say so, until the user guesses the number. Counts how many tries it takes"""
    tries = 0
    answer = random.randint(0,101)
    while True:
        num = 0
        try:
            num = int(input('Pick a number 1 - 100: '))
        except:
            print('Invalid')
            continue

        if num == answer:
            tries+=1
            print(f'You win in {tries} tries.')
            print(f"The number was {answer}")
            break
        elif num > 100 or num < 0 or num == str:
            print('Invalid.')
        elif num > answer:
            tries += 1
            print('Lower')
        elif num < answer:
            tries += 1
            print('Higher')

def play_again():
    """Asks the user for input on whether or not they would like to play again, and then returns that value."""
    play = ''
    play = str(input('Would you like to play again? (y)es / (n)o: ')).lower().strip()
    return play


def main():
    while True:
        higher_lower()
        play = play_again()
        if play == 'y':
            pass
        else:
            print('Have a good day.')
            break
    

if __name__ == '__main__':
    main()