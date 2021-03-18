# Set up Python
import pygame, sys

# Set up pygame/window

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Rocket Game')
screen = pygame.display.set_mode((900, 720), 0, 32)

font = pygame.font.SysFont('Arial', 40)
pygame.image.load('images/option_menu_button.png')

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:

        screen.fill((0, 0, 0))
        draw_text('Main Menu', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(40, 100, 100, 50)
        button_2 = pygame.Rect(40, 200, 100, 50)

        # pygame.Rect() is (top,left,width,height)


        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()

        pygame.draw.rect(screen, (120, 120, 120), button_1)
        opt_butt = pygame.image.load('images/option_menu_button.png')
        screen.blit(opt_butt,(40,200))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('Options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

main_menu()
