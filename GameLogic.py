import itertools
import random
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen.fill('white')
pygame.display.set_caption('WeSuckAtNamingCardGames')
fps_clock = pygame.time.Clock()

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


random.shuffle(deck)
card1 = deck[0][1]
card2 = deck[1][1]
card3 = deck[2][1]

def card_render(number):
    if number == 1:
        this_card1 = pygame.image.load('graphics/cards/ace_of_diamonds.png')
        this_card1 = pygame.transform.scale(this_card1, (100, 200))
        return this_card1
    elif number == 2:
        this_card2 = pygame.image.load('graphics/cards/2_of_diamonds.png')
        this_card2 = pygame.transform.scale(this_card2, (100, 200))
        return this_card2
    elif number == 3:
        this_card3 = pygame.image.load('graphics/cards/3_of_diamonds.png')
        this_card3 = pygame.transform.scale(this_card3, (100, 200))
        return this_card3
    elif number == 4:
        this_card4 = pygame.image.load('graphics/cards/4_of_diamonds.png')
        this_card4 = pygame.transform.scale(this_card4, (100, 200))
        return this_card4
    elif number == 5:
        this_card5 = pygame.image.load('graphics/cards/5_of_diamonds.png')
        this_card5 = pygame.transform.scale(this_card5, (100, 200))
        return this_card5
    elif number == 6:
        this_card6 = pygame.image.load('graphics/cards/6_of_diamonds.png')
        this_card6 = pygame.transform.scale(this_card6, (100, 200))
        return this_card6
    elif number == 7:
        this_card7 = pygame.image.load('graphics/cards/7_of_diamonds.png')
        this_card7 = pygame.transform.scale(this_card7, (100, 200))
        return this_card7
    elif number == 8:
        this_card8 = pygame.image.load('graphics/cards/8_of_diamonds.png')
        this_card8 = pygame.transform.scale(this_card8, (100, 200))
        return this_card8
    elif number == 9:
        this_card9 = pygame.image.load('graphics/cards/9_of_diamonds.png')
        this_card9 = pygame.transform.scale(this_card9, (100, 200))
        return this_card9
    elif number == 10:
        this_card10 = pygame.image.load('graphics/cards/10_of_diamonds.png')
        this_card10 = pygame.transform.scale(this_card10, (100, 200))
        return this_card10


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
    screen.blit(card2render, (75, 0))
    screen.blit(card3render, (160, 0))

    pygame.display.update()
    fps_clock.tick(60)
