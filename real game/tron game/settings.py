import pygame
from button import Button  # Import the Button class from your button module

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.menu_state = "Main"

        # Loading button images
        play_img = pygame.image.load('assets/backgrounds/Play button.png').convert_alpha()
        quit_img = pygame.image.load('assets/backgrounds/Quit button.png').convert_alpha()
        instructions_img = pygame.image.load('assets/backgrounds/Instructions button.png').convert_alpha()
        back_img = pygame.image.load('assets/backgrounds/back button.png').convert_alpha()

        # Creating button instances
        self.play_button = Button(100, 800, play_img, 3)
        self.quit_button = Button(700, 800, quit_img, 3)
        self.settings_button = Button(1300, 800, settings_img, 3)
        self.back_button = Button(0, 0, back_img, 3)

        # Background image
        self.BG = pygame.image.load('assets/backgrounds/main menu.png')

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def run_menu(self):
        run = True
        while run:
            self.screen.blit(self.BG, (0, 0))
            if self.menu_state == "Main":
                if self.play_button.draw(self.screen) == 1:
                    print('Play')
                if self.quit_button.draw(self.screen) == 1:
                    run = False
                if self.settings_button.draw(self.screen) == 1:
                    self.menu_state = "instructions"
            elif self.menu_state == "instructions":
                if self.back_button.draw(self.screen) == 1:
                    self.menu_state = "Main"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
