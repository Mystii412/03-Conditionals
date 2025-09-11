import random

print('Rock Paper Scissors')
rounds = 3
while rounds > 0:
    player_choice = input('Do you want to play Rock (r), Paper(p), or Scissors(s): ')

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

        print(f"You picked {pc}")
        print(f"The computer picked {cc}")

        if pc == cc:
            print('It\'s a tie.')
        elif pc == 'Rock' and cc == 'Paper':
            print('You lose.')
        elif pc =='Rock' and cc == 'Scissors':
            print('You win.')
        elif pc == 'Paper' and cc == 'Rock':
            print('You win.')
        elif pc == 'Paper' and cc == 'Scissors':
            print('You lose.')
        elif pc == 'Scissors' and cc == 'Paper':
            print('You win.')
        elif pc == 'Scissors' and cc == 'Rock':
            print('You lose.')

        rounds = rounds -1

    else:
        print('That\'s not an option. Relaunch program to pick again')
        exit()