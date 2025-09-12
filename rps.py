import random

print('Rock Paper Scissors')
rounds = int(input('Input how many rounds you would like to play: '))
round = 1
hmn_wins = 0
cpu_wins = 0
while rounds > 0:
    player_choice = 'yes'
    print(f"Round {round}")
    round += 1
    while True:
        if player_choice != 'r' and player_choice != 'p' and player_choice != 's':
            player_choice = input('Do you want to play Rock (r), Paper(p), or Scissors(s): ').strip().lower()
        else:
            break
    if player_choice == 'r' or player_choice == 'R' or player_choice == 'p' or player_choice == 'P' or player_choice == 's' or player_choice == 'S':
        cpu_moves = ['r', 'p', 's']
        cpu_move = random.choice(cpu_moves)

        if player_choice == 'r' or player_choice == 'R':
            pc = 'Rock'
        elif player_choice == 'p' or player_choice == 'P':
            pc = 'Paper'
        else:
            pc = 'Scissors'

        if cpu_move == 'r':
            cc = 'Rock'
        elif cpu_move == 'p':
            cc = 'Paper'
        else:
            cc = 'Scissors'

        print(f"You picked {pc}.")
        print(f"The computer picked {cc}.")

        if pc == cc:
            print('It\'s a tie.')
        elif pc == 'Rock' and cc == 'Paper':
            print('You lose.')
            cpu_wins += 1
        elif pc =='Rock' and cc == 'Scissors':
            print('You win.')
            hmn_wins += 1
        elif pc == 'Paper' and cc == 'Rock':
            print('You win.')
            hmn_wins += 1
        elif pc == 'Paper' and cc == 'Scissors':
            print('You lose.')
            cpu_wins += 1
        elif pc == 'Scissors' and cc == 'Paper':
            print('You win.')
            hmn_wins += 1
        elif pc == 'Scissors' and cc == 'Rock':
            print('You lose.')
            cpu_wins += 1

        rounds = rounds -1

if hmn_wins > cpu_wins:
    print(f"You won, {hmn_wins} : {cpu_wins}")
elif hmn_wins == cpu_wins:
    print(f"It's a tie. {hmn_wins} : {cpu_wins}")
else:
    print(f"You lost, {hmn_wins} : {cpu_wins}")