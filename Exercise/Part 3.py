import random
count_played = 0

if count_played == 0:
    choice_taking = True
    while choice_taking:
        start_input = input('Start Game ???? (y/n)').lower()
        if start_input in ['y', 'n']:
            choice_taking = False
        else:
            print('command Invalid !!!')

    if start_input == 'y':
        start = True
    else:
        start = False

while start:
    print('Try answering the following questions:')
    run = True
    point = 0
    while run:
        print('point: {}'.format(point))

        a = random.randint(1, 10)
        b = random.randint(1, 10)

        if random.random() <= 0.5:
            correct_result = a + b
            sign = '+'
        else:
            correct_result = a - b
            sign = '-'

        if random.random() <= 0.5:
            to_show_result = correct_result
            state = 'r'
        else:
            to_show_result = correct_result + random.randint(-3, 3)
            state = 'w'

        print('{0} {1} {2} = {3}'.format(a, sign , b, to_show_result))

        choice_taking = True
        while choice_taking:
            choice = input('Right or Wrong (r/w) ??????').lower()
            if choice in ['r', 'w']:
                choice_taking = False
            else:
                print('command Invalid !!!')

        if choice == state:
            point += 1
            print('Correct !!')
        else:
            print('Incorrect !! You lose')
            run = False

    choice_taking = True
    while choice_taking:
        play_again = input('Play Again? (y/n)').lower()
        if play_again in ['y', 'n']:
            choice_taking = False
        else:
            print('command Invalid !!!')

    print('')
    if play_again == 'n':
        start = False
        count_played = 1