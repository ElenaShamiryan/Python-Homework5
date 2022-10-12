print('Здравствуйте! Представьтесь, пожалуйста:')
player_name = input()
print(f'Здравствуйте, {player_name}! Давайте сыграем в игру с конфетами.'
      f' Выиграет тот, кто забирает в конце <=28 конфет. Поехали!')

import random
sweet = 100

def the_game(player_name, sweet):
    while sweet >= 28:
        try:
            player =int(input(f'{player_name}, возьмите <= 28 конфет: '))
            if player > 28:
                player = int(input('Вы хотите взять слишком много конфет, возьмите <= 28 конфет: '))
            sweet = sweet - player
            print(f'Осталось {sweet} конфет')
            if sweet <= 28:
                print('Победил компьютер!')
                break
        except:
            print('Введен неверный символ. Переход хода.')
        comp = random.randint(1, 28)
        print(f'Компьютер взял {comp} конфет')
        sweet = sweet - comp
        print(f'Осталось {sweet} конфет')
        if sweet <= 28:
            print(f'{player_name}, Вы победили!')
            break
   
the_game(player_name, sweet)
