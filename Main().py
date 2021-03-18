'''

import time
import pygame
pygame.init()

Delta_V = 0
Numb_Engines = 2
Payload_Mass = 3000 # kg
Tank_Mass = 5000 # kg

RP1_Mass_Launch = 178389 # kg
Oxid_Mass_Launch = 68611 # kg

RP1_Mass = RP1_Mass_Launch # kg
Oxid_Mass = Oxid_Mass_Launch # kg

RD191_Mass = 2290 # kg
RD191_Thrust = 1920 # kN
Isp = 300 # m/s

Earth_Gravity = 9.81     # m/s^2

Ship_Velocity = 0
Ship_Acc = 0

Dry_Mass = Payload_Mass + Tank_Mass + Numb_Engines*RD191_Mass # kg

Ship_Mass = Dry_Mass + RP1_Mass + Oxid_Mass

Thrust = RD191_Thrust * Numb_Engines

Thrust_to_weight = Thrust*1000 / (Ship_Mass*Earth_Gravity)


screen = pygame.display.set_mode((1200,720))
pygame.display.flip()

Ship_Mass_current = 0

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

sysfont = pygame.font.get_default_font()

img = font.render(sysfont, True, RED)
rect = img.get_rect()
pygame.draw.rect(img, BLUE, rect, 1)

run = True
while run:

    screen.blit(Ship_Mass_current,(50,50))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    screen.blit(img, (20, 20))
    pygame.display.update()





for i in range (0,500):

    if RP1_Mass > 0:
        RP1_Mass = RP1_Mass - 830       # burn rate is 830 kg/s for RP1
    else:
        RP1_Mass = 0

    if Oxid_Mass > 0:
        Oxid_Mass = Oxid_Mass - 318     # burn rate is 830 kg/s for RP1
    else:
        Oxid_Mass = 0

    Ship_Mass = Dry_Mass + RP1_Mass + Oxid_Mass
    Ship_Acc = Thrust*1000 / Ship_Mass
    Ship_Velocity = Ship_Velocity + Ship_Acc

    Ship_Mass_current = pygame.display.load(Ship_Mass)

    time.sleep(1)
'''

import pygame
# import time
from pygame.locals import *

Window_Size = (800, 800)
background_color = (137, 209, 234)
rocket_icon = pygame.image.load('rocket_icon.png')
font_color = (255, 255, 255)

clock = pygame.time.Clock()

RP1_Mass_Launch = 178389 # kg
Oxid_Mass_Launch = 68611 # kg
Ship_Dry_Mass = 5000 # kg
ship_mass = 0 # kg
RP1_Mass = RP1_Mass_Launch
Oxid_Mass = Oxid_Mass_Launch
ship_velocity = 0 # m/s
ship_velocity_value = '-'
ship_acc = 0 # m/s^2


def Update_Ship_Velocity():
    global ship_velocity
    global ship_mass
    global ship_acc

    ship_acc = 3400 * 1000 / ship_mass
    ship_velocity = round(ship_velocity + ship_acc, 3)
def Update_Ship_Mass():
    global ship_mass
    global Ship_Dry_Mass
    global RP1_Mass
    global Oxid_Mass

    if RP1_Mass > 0:
        RP1_Mass = RP1_Mass - 830
    else:
        RP1_Mass = 0
    if RP1_Mass > 0:
        Oxid_Mass = Oxid_Mass - 318
    else:
        Oxid_Mass = 0
    ship_mass = Ship_Dry_Mass + RP1_Mass + Oxid_Mass

def main():
    # Initialize Screen
    pygame.init()
    screen = pygame.display.set_mode(Window_Size)
    pygame.display.set_caption("A Rocket Window")
    pygame.display.set_icon(rocket_icon)

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(background_color)

    # Display some text
    font = pygame.font.Font(None, 40)
    text = font.render("Mission Control", True, font_color)
    text_position = text.get_rect()
    text_position.centerx = background.get_rect().centerx
    background.blit(text, text_position)

    # Display Mission Time
    clock = pygame.time.Clock()

    counter = 0

    text3 = '0'
    text4 = 'seconds of Mission Time'
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Arial', 30)

    # Mission Time Position on Display
    text3_x, text3_y = 30, 30
    text4_x, text4_y = text3_x + 40, text3_y
    text3_pos = (text3_x, text3_y)
    text4_pos = (text4_x, text4_y)

    # Ship Mass Position on Display
    ship_mass_value = '-'
    ship_mass_unit = 'kg'
    ship_mass_value_x, ship_mass_value_y = 30, 60
    ship_mass_unit_x, ship_mass_unit_y = ship_mass_value_x + 120,  ship_mass_value_y
    ship_mass_value_pos = (ship_mass_value_x, ship_mass_value_y)
    ship_mass_unit_pos = (ship_mass_unit_x, ship_mass_unit_y)

    # Ship Velocity Position on Display
    ship_mass_value = '-'
    ship_velocity_unit = 'm/s'
    ship_velocity_value_x, ship_velocity_value_y = 30, 90
    ship_velocity_unit_x, ship_velocity_unit_y = ship_velocity_value_x + 120,  ship_velocity_value_y
    ship_velocity_value_pos = (ship_velocity_value_x, ship_velocity_value_y)
    ship_velocity_unit_pos = (ship_velocity_unit_x, ship_velocity_unit_y)





    # Event Loop
    run = True
    while run:
        for event in pygame.event.get():

            # The Display of Mission Time
            if event.type == pygame.USEREVENT:
                counter += 1
                text3 = str(counter)

            # For the Ship Mass
            if event.type == pygame.USEREVENT:
                Update_Ship_Mass()
                ship_mass_value = str(ship_mass)

            # For the Ship Velocity
            if event.type == pygame.USEREVENT:
                Update_Ship_Velocity()
                global ship_velocity_value
                ship_velocity_value = str(ship_velocity)

            # Exit the program
            if event.type == QUIT:
                run = False

        # Load the background
        screen.blit(background, (0, 0))

        # Writing Mission Information on the Display

        # Mission Time
        screen.blit(font.render(text3, True, font_color), text3_pos)
        screen.blit(font.render(text4, True, font_color), text4_pos)

        # Ship Mass
        screen.blit(font.render(ship_mass_value, True, font_color), ship_mass_value_pos)
        screen.blit(font.render(ship_mass_unit, True, font_color), ship_mass_unit_pos)

        # Ship Velocity
        screen.blit(font.render(ship_velocity_value,True,font_color), ship_velocity_value_pos)
        screen.blit(font.render(ship_velocity_unit, True, font_color), ship_velocity_unit_pos)

        clock.tick(60)

        #Update the Display
        pygame.display.update()


if __name__ == '__main__': main()
