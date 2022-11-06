import itertools
import random
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen.fill('white')
pygame.display.set_caption('We Suck At Naming Card Games')
fps_clock = pygame.time.Clock()

card1render = pygame.image.load('graphics/cards/3_of_clubs.png')
card2render = pygame.image.load('graphics/cards/9_of_clubs.png')
card3render = pygame.image.load('graphics/cards/5_of_clubs.png')

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


def card_render(number):
    if number == 1:
        return pygame.image.load('graphics/cards/ace_of_diamonds.png')
    elif number == 2:
        return pygame.image.load('graphics/cards/2_of_diamonds.png')
    elif number == 3:
        return pygame.image.load('graphics/cards/3_of_diamonds.png')
    elif number == 4:
        return pygame.image.load('graphics/cards/4_of_diamonds.png')
    elif number == 5:
        return pygame.image.load('graphics/cards/5_of_diamonds.png')
    elif number == 6:
        return pygame.image.load('graphics/cards/6_of_diamonds.png')
    elif number == 7:
        return pygame.image.load('graphics/cards/7_of_diamonds.png')
    elif number == 8:
        return pygame.image.load('graphics/cards/8_of_diamonds.png')
    elif number == 9:
        return pygame.image.load('graphics/cards/9_of_diamonds.png')
    elif number == 10:
        return pygame.image.load('graphics/cards/10_of_diamonds.png')



random.shuffle(deck)
card1 = deck[0][1]
card2 = deck[1][1]
card3 = deck[2][1]

print(card1)
print(card2)
print(card3)


def get_shield(atk, defense):
    defense -= atk
    return defense


def get_hp(defense, hp):
    if defense < 0:
        return hp + defense
    else:
        return hp


player_two_shield = get_shield(player_one_attack, player_two_shield)
player_two_hp = get_hp(player_two_shield, player_two_hp)

while True:
    # actually runs game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    card1render = card_render(card1)
    card2render = card_render(card2)
    card3render = card_render(card3)

    screen.blit(card1render, (0, 0))
    screen.blit(card2render, (200, 0))
    screen.blit(card3render, (400, 0))

    pygame.display.update()
    fps_clock.tick(60)
