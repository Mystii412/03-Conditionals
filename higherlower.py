import random

def higher_lower():
    """Sets tries to 0, and asks the user for a number, if higher or lower, it will say so, until the user guesses the number. Counts how many tries it takes"""
    global tries
    tries = 0
    global answer
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
            print(f'You guessed the number in {tries} tries.')
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

def bot_guess():
    """Makes the bot guess in the middle of the range, and splits the range in half based on whether it's higher or lower"""
    global guesses
    guesses = 0
    r1 = 0
    r2 = 100

    while True:
        guess = (r1 + r2)/2
        print(guess)
        if guess > answer:
            guesses+=1
            r2=guess
            r2 = round(r2)
        elif guess == answer:
            guesses+=1
            print(f'The bot guessed the number in {guesses} guesses.')
            break
        else:
            r1 = guess
            r1 = round(r1)

def results(bot_attempts,human_attempts):
    """Takes bot guesses and human guesses and compares them to see who wins"""
    if bot_attempts > human_attempts:
        diff = bot_attempts - human_attempts
        print(f'You win by {diff} guesses.')
    elif bot_attempts < human_attempts:
        diff = human_attempts - bot_attempts
        print(f"Bot Wins by {diff} guesses.")

def main():
    while True:
        higher_lower()
        bot_guess()
        results(guesses,tries)
        play = play_again()
        if play == 'y':
            pass
        else:
            print('Have a good day.')
            break
    


if __name__ == '__main__':
    main()