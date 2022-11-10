import itertools
import random
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen.fill('blue')
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

card1selected = False
card2selected = False
card3selected = False

click_timer = 0
mouse_down = False


def get_cards():
    random.shuffle(deck)
    # draws three cards
    print("You got:")
    for i in range(3):
        print(deck[i][0], "of", deck[i][1])


def get_card():
    random.shuffle(deck)
    return deck[1][1]


def card_render(number):
    if number == 1:
        this_card = pygame.image.load('graphics/cards/ace_of_diamonds.png')
        this_card = pygame.transform.scale(this_card, (100, 145))
        return this_card
    elif number == 2:
        this_card = pygame.image.load('graphics/cards/2_of_diamonds.png')
        this_card = pygame.transform.scale(this_card, (100, 145))
        return this_card
    elif number == 3:
        this_card = pygame.image.load('graphics/cards/3_of_diamonds.png')
        this_card = pygame.transform.scale(this_card, (100, 145))
        return this_card
    elif number == 4:
        this_card = pygame.image.load('graphics/cards/4_of_diamonds.png')
        this_card = pygame.transform.scale(this_card, (100, 145))
        return this_card
    elif number == 5:
        this_card = pygame.image.load('graphics/cards/5_of_diamonds.png')
        this_card = pygame.transform.scale(this_card, (100, 145))
        return this_card
    elif number == 6:
        this_card = pygame.image.load('graphics/cards/6_of_diamonds.png')
        this_card = pygame.transform.scale(this_card, (100, 145))
        return this_card
    elif number == 7:
        this_card = pygame.image.load('graphics/cards/7_of_diamonds.png')
        this_card = pygame.transform.scale(this_card, (100, 145))
        return this_card
    elif number == 8:
        this_card = pygame.image.load('graphics/cards/8_of_diamonds.png')
        this_card = pygame.transform.scale(this_card, (100, 145))
        return this_card
    elif number == 9:
        this_card = pygame.image.load('graphics/cards/9_of_diamonds.png')
        this_card = pygame.transform.scale(this_card, (100, 145))
        return this_card
    elif number == 10:
        this_card = pygame.image.load('graphics/cards/10_of_diamonds.png')
        this_card = pygame.transform.scale(this_card, (100, 145))
        return this_card


def get_shield(atk, defense):
    defense -= atk
    return defense


def get_hp(defense, hp):
    if defense < 0:
        return hp + defense
    else:
        return hp


card1 = get_card()
card2 = get_card()
card3 = get_card()

card1render = card_render(card1)
card1rect = card1render.get_rect(topleft=(480, 500))

card2render = card_render(card2)
card2rect = card1render.get_rect(topleft=(590, 500))

card3render = card_render(card3)
card3rect = card1render.get_rect(topleft=(700, 500))

shuffle_icon = pygame.image.load('graphics/UI/Shuffle.png')
shuffle_icon = pygame.transform.scale(shuffle_icon, (100, 100))
shuffle_rect = shuffle_icon.get_rect(topleft=(590, 350))

while True:
    # actually runs game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        else:
            mouse_down = False

    screen.fill("blue")

    card1render = card_render(card1)
    card2render = card_render(card2)
    card3render = card_render(card3)

    screen.blit(card1render, card1rect)
    screen.blit(card2render, card2rect)
    screen.blit(card3render, card3rect)
    screen.blit(shuffle_icon, shuffle_rect)

    cursor = pygame.mouse.get_pos()
    cursor_click = pygame.mouse.get_pressed()

    click_timer -= 1  # Ensures there isn't always a selected card or repeated actions, the refresh was too fast before

    if shuffle_rect.collidepoint(cursor) and mouse_down and click_timer <= 0:
        card1 = get_card()
        card2 = get_card()
        card3 = get_card()
        click_timer = 30

    # Big else-if used to switch the cards around, feel free to optimize if you have any ideas
    if card1rect.collidepoint(cursor) and mouse_down and not card1selected and click_timer <= 0:
        if card2selected:
            temp_card = card1
            card1 = card2
            card2 = temp_card
            card2selected = False
            card2rect.y += 10
            click_timer = 30
        elif card3selected:
            temp_card = card1
            card1 = card3
            card3 = temp_card
            card3selected = False
            card3rect.y += 10
            click_timer = 30
        else:
            card1rect.y -= 10
            screen.blit(card1render, card1rect)
            card1selected = True

    elif card2rect.collidepoint(cursor) and mouse_down and not card2selected and click_timer <= 0:
        if card1selected:
            temp_card = card1
            card1 = card2
            card2 = temp_card
            card1selected = False
            card1rect.y += 10
            click_timer = 30
        elif card3selected:
            temp_card = card2
            card2 = card3
            card3 = temp_card
            card3selected = False
            card3rect.y += 10
            click_timer = 30
        else:
            card2rect.y -= 10
            card2selected = True

    elif card3rect.collidepoint(cursor) and mouse_down and not card3selected and click_timer <= 0:
        if card1selected:
            temp_card = card3
            card3 = card1
            card1 = temp_card
            card1selected = False
            card1rect.y += 10
            click_timer = 30
        elif card2selected:
            temp_card = card3
            card3 = card2
            card2 = temp_card
            card2selected = False
            card2rect.y += 10
            click_timer = 30
        else:
            card3rect.y -= 10
            screen.blit(card3render, card3rect)
            card3selected = True

    pygame.display.update()
    fps_clock.tick(60)
