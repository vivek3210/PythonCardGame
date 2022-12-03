import itertools
import random
import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen.fill('blue')
pygame.display.set_caption('WeSuckAtNamingCardGames')
fps_clock = pygame.time.Clock()

deck = list(
    itertools.product(range(1, 2), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

player_one_hp = 25
player_one_shield = 5
player_one_attack = 0
player_one_energy = 0

player_two_hp = 25
player_two_shield = 5
player_two_attack = 0
player_two_energy = 0

turn_string = "Player One"

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

if card1 == 1:
    cardString = "attack"
elif card1 == 2:
    cardString = "shield"
elif card1 == 3:
    cardString = "energy"
elif card1 == 4:
    cardString = "attack"
elif card1 == 5:
    cardString = "shield"
elif card1 == 6:
    cardString = "energy"
elif card1 == 7:
    cardString = "attack"
elif card1 == 8:
    cardString = "shield"
elif card1 == 9:
    cardString = "energy"
elif card1 == 10:
    cardString = "attack"

if card2 == 1:
    cardString2 = "attack"
elif card2 == 2:
    cardString2 = "shield"
elif card2 == 3:
    cardString2 = "energy"
elif card2 == 4:
    cardString2 = "attack"
elif card2 == 5:
    cardString2 = "shield"
elif card2 == 6:
    cardString2 = "energy"
elif card2 == 7:
    cardString2 = "attack"
elif card2 == 8:
    cardString2 = "shield"
elif card2 == 9:
    cardString2 = "energy"
elif card2 == 10:
    cardString2 = "attack"

if card3 == 1:
    cardString3 = "attack"
elif card3 == 2:
    cardString3 = "shield"
elif card3 == 3:
    cardString3 = "energy"
elif card3 == 4:
    cardString3 = "attack"
elif card3 == 5:
    cardString3 = "shield"
elif card3 == 6:
    cardString3 = "energy"
elif card3 == 7:
    cardString3 = "attack"
elif card3 == 8:
    cardString3 = "shield"
elif card3 == 9:
    cardString3 = "energy"
elif card3 == 10:
    cardString3 = "attack"

card1render = card_render(card1)
card1rect = card1render.get_rect(topleft=(480, 500))

card2render = card_render(card2)
card2rect = card1render.get_rect(topleft=(590, 500))

card3render = card_render(card3)
card3rect = card1render.get_rect(topleft=(700, 500))

shuffle_icon = pygame.image.load('graphics/UI/Shuffle.png')
shuffle_icon = pygame.transform.scale(shuffle_icon, (100, 100))
shuffle_rect = shuffle_icon.get_rect(topleft=(590, 350))

play_icon = pygame.image.load('graphics/UI/Play.png')
play_icon = pygame.transform.scale(play_icon, (100, 100))
play_rect = play_icon.get_rect(topleft=(590, 200))

health_icon = pygame.image.load('graphics/UI/Heart.png')
health_icon = pygame.transform.scale(health_icon, (100, 100))
health_rect = health_icon.get_rect(topleft=(100, 50))

shield_icon = pygame.image.load('graphics/UI/Shield.png')
shield_icon = pygame.transform.scale(shield_icon, (140, 140))
shield_rect = shield_icon.get_rect(topleft=(78, 150))

health_icon2 = pygame.image.load('graphics/UI/Heart.png')
health_icon2 = pygame.transform.scale(health_icon2, (100, 100))
health_rect2 = health_icon2.get_rect(topleft=(1050, 50))

shield_icon2 = pygame.image.load('graphics/UI/Shield.png')
shield_icon2 = pygame.transform.scale(shield_icon2, (140, 140))
shield_rect2 = shield_icon2.get_rect(topleft=(1028, 150))

energy_icon = pygame.image.load('graphics/UI/Energy.png')
energy_icon = pygame.transform.scale(energy_icon, (100, 100))
energy_rect = energy_icon.get_rect(topleft=(100, 300))

energy_icon2 = pygame.image.load('graphics/UI/Energy.png')
energy_icon2 = pygame.transform.scale(energy_icon2, (100, 100))
energy_rect2 = energy_icon2.get_rect(topleft=(1050, 300))

attack_icon_cards = pygame.image.load('graphics/UI/Sword.png')
attack_icon_cards = pygame.transform.scale(attack_icon_cards, (40, 40))
attack_rect_cards = attack_icon_cards.get_rect(center=(580, 500))

shield_icon_cards = pygame.image.load('graphics/UI/Shield.png')
shield_icon_cards = pygame.transform.scale(shield_icon_cards, (40, 40))
shield_rect_cards = shield_icon_cards.get_rect(center=(690, 500))

energy_icon_cards = pygame.image.load('graphics/UI/Energy.png')
energy_icon_cards = pygame.transform.scale(energy_icon_cards, (40, 40))
energy_rect_cards = energy_icon_cards.get_rect(center=(800, 500))

font = pygame.font.SysFont('Arial', 30)
text = font.render(str(player_one_hp), True, 'white')
textRect = text.get_rect()
textRect.center = (230, 90)

text2 = font.render(str(player_two_hp), True, 'white')
textRect2 = text2.get_rect()
textRect2.center = (1025, 90)

text3 = font.render(str(player_one_shield), True, 'white')
textRect3 = text3.get_rect()
textRect3.center = (230, 190)

text4 = font.render(str(player_two_shield), True, 'white')
textRect4 = text4.get_rect()
textRect4.center = (1025, 190)

text5 = font.render(str(player_one_energy), True, 'white')
textRect5 = text5.get_rect()
textRect5.center = (230, 340)

text6 = font.render(str(player_two_energy), True, 'white')
textRect6 = text6.get_rect()
textRect6.center = (1025, 340)

text6 = font.render(str(player_two_energy), True, 'white')
textRect6 = text6.get_rect()
textRect6.center = (1025, 340)

turnText = font.render(str(turn_string), True, 'white')
turnRect = turnText.get_rect()
turnRect.center = (640, 100)

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

    # renders everything

    card1render = card_render(card1)
    card2render = card_render(card2)
    card3render = card_render(card3)

    screen.blit(card1render, card1rect)
    screen.blit(card2render, card2rect)
    screen.blit(card3render, card3rect)
    screen.blit(shuffle_icon, shuffle_rect)
    screen.blit(play_icon, play_rect)

    screen.blit(health_icon, health_rect)
    screen.blit(shield_icon, shield_rect)
    screen.blit(health_icon2, health_rect2)
    screen.blit(shield_icon2, shield_rect2)
    screen.blit(energy_icon, energy_rect)
    screen.blit(energy_icon2, energy_rect2)

    screen.blit(energy_icon_cards, energy_rect_cards)
    screen.blit(shield_icon_cards, shield_rect_cards)
    screen.blit(attack_icon_cards, attack_rect_cards)

    text = font.render(str(player_one_hp), True, 'white')
    text2 = font.render(str(player_two_hp), True, 'white')
    text3 = font.render(str(player_one_shield), True, 'white')
    text4 = font.render(str(player_two_shield), True, 'white')
    text5 = font.render(str(player_one_energy), True, 'white')
    text6 = font.render(str(player_two_energy), True, 'white')
    turnText = font.render(str(turn_string), True, 'white')

    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)
    screen.blit(text5, textRect5)
    screen.blit(text6, textRect6)

    cursor = pygame.mouse.get_pos()
    cursor_click = pygame.mouse.get_pressed()

    # Win Condition
    if player_two_hp <= 0 or player_two_hp <= 0:
        if player_two_hp <= 0:
            player_two_hp = 0
            turn_string = "Player One"
        else:
            player_one_hp = 0
            turn_string = "Player Two"
        turnText = font.render(turn_string + " Wins!", True, 'white')
        turnRect.center = (640, 100)
        screen.blit(turnText, turnRect)
        # wait 10 seconds before exiting
        pygame.display.update()
        fps_clock.tick(60)
        time.sleep(10)
        pygame.quit()

    screen.blit(turnText, turnRect)

    click_timer -= 1  # Ensures there isn't always a selected card or repeated actions, the refresh was too fast before

    # Shuffle Cards
    if shuffle_rect.collidepoint(cursor) and mouse_down and click_timer <= 0:
        if turn_string == "Player One":
            if player_one_energy == 10:
                card1 = get_card()
                card2 = get_card()
                card3 = get_card()
                player_one_energy = 0
                click_timer = 30
        else:
            if player_two_energy == 10:
                card1 = get_card()
                card2 = get_card()
                card3 = get_card()
                player_two_energy = 0
                click_timer = 30

    # Begins Turn
    if play_rect.collidepoint(cursor) and mouse_down and click_timer <= 0:
        if turn_string == "Player One":
            player_one_attack = card1
            player_one_shield += card2
            player_one_energy += card3
            player_two_shield -= player_one_attack

            if player_two_shield < 0:
                player_two_hp += player_two_shield
                player_two_shield = 0

            if player_one_shield > 10:
                player_one_shield = 10

            if player_one_energy > 10:
                player_one_energy = 10

            turn_string = "Player Two"

            card1 = get_card()
            card2 = get_card()
            card3 = get_card()

            click_timer = 30
        else:
            player_two_attack = card1
            player_two_shield += card2
            player_two_energy += card3
            player_one_shield -= player_two_attack

            if player_one_shield < 0:
                player_one_hp += player_one_shield
                player_one_shield = 0

            if player_two_shield > 10:
                player_two_shield = 10

            if player_two_energy > 10:
                player_two_energy = 10

            turn_string = "Player One"

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
