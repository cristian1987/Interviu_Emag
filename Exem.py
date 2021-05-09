import random


class Player:
    def __init__(self, name, health, strength, defence, speed, luck):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.luck = luck


def fight(p1, p2):
    print('Luptatorii')
    print(p1.name)
    print('health', p1.health)
    print('strength', p1.strength)
    print('defence', p1.defence)
    print('speed', p1.speed)
    print('luck', p1.luck)
    print('-----------')
    print(p2.name)
    print('health', p2.health)
    print('strength', p2.strength)
    print('defence', p2.defence)
    print('speed', p2.speed)
    print('luck', p2.luck)

    print('---------------------------------------')

    print('inceputul luptei')
    print('--------------')
    print('--------------')
    if (p1.speed > p2.speed) or (p1.luck > p2.luck):
        while (p1.health > 0) and (p2.health > 0):
            print(p1.name, 'ataca')
            damage = p1.strength - p2.defence
            p2.health -= damage
            print(p1.name, 'strength', p1.strength, 'health', p1.health)
            print(p2.name, 'strength', p2.strength, 'health', p2.health)
            print('--------------2')
            if p1.health <= 0:
                print(p1.name, 'a pierdut')
                print(p2.name, 'a castigat')
            elif p2.health <= 0:
                print(p1.name, 'a castigat')
                print(p2.name, 'a pierdut')
            print(p2.name, 'ataca')
            damage1 = p2.strength - p1.defence
            p1.health -= damage1
            print(p2.name, 'strength', p2.strength, 'health', p2.health)
            print(p1.name, 'strength', p1.strength, 'health', p1.health)
            print('--------------3')
            if p1.health <= 0:
                print(p1.name, 'a pierdut')
                print(p2.name, 'a castigat')
            elif p2.health <= 0:
                print(p1.name, 'a castigat')
                print(p2.name, 'a pierdut')
    elif (p2.speed > p1.speed) or (p2.luck > p1.luck):
        while (p1.health > 0) and (p2.health > 0):
            print(p2.name, 'ataca')
            damage = p2.strength - p1.defence
            p1.health -= damage
            print(p2.name, 'strength', p2.strength, 'health', p2.health)
            print(p1.name, 'strength', p1.strength, 'health', p1.health)
            print('--------------4')
            if p1.health <= 0:
                print(p1.name, 'a pierdut')
                print(p2.name, 'a castigat')
            elif p2.health <= 0:
                print(p1.name, 'a castigat')
                print(p2.name, 'a pierdut')
            print(p1.name, 'ataca')
            damage1 = p1.strength - p2.defence
            p2.health -= damage1
            print(p1.name, 'strength', p1.strength, 'health', p1.health)
            print(p2.name, 'strength', p2.strength, 'health', p2.health)
            print('--------------5')
            if p1.health <= 0:
                print(p1.name, 'a pierdut')
                print(p2.name, 'a castigat')
            elif p2.health <= 0:
                print(p1.name, 'a castigat')
                print(p2.name, 'a pierdut')


p1 = Player('Orderus', random.randint(70, 99), random.randint(70, 79), random.randint(45, 54), random.randint(40, 49), random.randint(10, 30))
p2 = Player('Beast', random.randint(60, 89), random.randint(60, 89), random.randint(40, 60), random.randint(40, 60), random.randint(25, 40))


fight(p1, p2)
