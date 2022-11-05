import itertools
import random
import pygame

pygame.display.init()

deck = list(
    itertools.product(range(1, 2), ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']))

player_one_hp = 25
player_one_shield = 0
player_one_attack = 0
player_one_energy = 0

player_two_hp = 25
player_two_shield = 0
player_two_attack = 0
player_two_energy = 0


def get_cards():
    random.shuffle(deck)
    # draws three cards
    print("You got:")
    for i in range(3):
        print(deck[i][0], "of", deck[i][1])


def get_shield(atk, defense):
    defense -= atk
    return defense


def get_hp(defense, hp):
    if defense < 0:
        return hp + defense
    else:
        return hp


player_one_attack = 20
player_two_shield = 20

get_cards()
player_two_shield = get_shield(player_one_attack, player_two_shield)
player_two_hp = get_hp(player_two_shield, player_two_hp)

print(player_two_hp)
