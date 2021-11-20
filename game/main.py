import random
hp = 25
doors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dx=[]
while hp > 0:
    for i in range(len(doors)):
        x = random.randint(0, 1)
        if x == 1:
            dx.append(doors[i]+1)

        else:
            dx.append(doors[i]-1)
    dg = int(input('Выберите одну из десяти дверей:'))
    print('Выбранная дверь:', dg)
    if doors[dg-1] > dx[dg-1]:
        print('Вам повезло! За этой дверью магический артефакт.')
        ma = random.randint(10, 80)
        hp += ma
        print('Ваша сила:',hp)
    else:
        print('Вам не повезло...За этой дверью монстр')
        monster_power = random.randint(5, 100)
        print('Сила монстра:', monster_power)
        if hp >= monster_power:
            print('Вы выиграли!')
            print('Ваше здоровье:', hp)
        else:
            print('Вы проиграли...')
            hp -= monster_power
            if hp<=0:
                print('Игра окончена')








