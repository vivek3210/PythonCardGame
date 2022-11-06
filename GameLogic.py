import itertools
import random
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen.fill('white')
pygame.display.set_caption('We Suck At Naming Card Games')
fps_clock = pygame.time.Clock()

card1 = pygame.image.load('graphics/cards/3_of_clubs.png')
card2 = pygame.image.load('graphics/cards/9_of_clubs.png')
card3 = pygame.image.load('graphics/cards/5_of_clubs.png')

deck = list(
    itertools.product(range(1, 2), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

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

card1 = deck[0][0]
card2 = deck[1][0]
card3 = deck[2][0]

def get_shield(atk, defense):
    defense -= atk
    return defense


def get_hp(defense, hp):
    if defense < 0:
        return hp + defense
    else:
        return hp


get_cards()
player_two_shield = get_shield(player_one_attack, player_two_shield)
player_two_hp = get_hp(player_two_shield, player_two_hp)

print(player_two_hp)

while True:
    # actually runs game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(card1, (0, 0))
    screen.blit(card2, (200, 0))
    screen.blit(card3, (400, 0))

    pygame.display.update()
    fps_clock.tick(60)
