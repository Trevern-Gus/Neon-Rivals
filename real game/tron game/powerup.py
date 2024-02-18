import pygame
import sys
import random
from button import Button
# Initialize Pygame
pygame.init()
import settings
# Set up the screen
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Neon Rivals')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

#state
game_over = True

# Define constants
cell_size = 20  # Size of each cell in the grid
border_thickness = 20  # Thickness of the border

pygame.mixer.music.load('assets/Music and FX/Main Game Music.mp3')
pygame.mixer.music.play(-1, 0.0 , 9000)
# Clock to control the game's speed
clock = pygame.time.Clock()

#define font
font_small = pygame.font.Font('assets/font/adrip1.ttf', 36)
font_big = pygame.font.Font('assets/font/adrip1.ttf', 48)
font_very_small = pygame.font.SysFont("arialblack", 26)
# Define border dimensions
border_rect = pygame.Rect(0, 0,
                          1000,
                          800)
#basically everything needed and in the main game loop
class Main():
    #creating instances easier
    def __init__(self):
        self.player1 = Player1(blue, 300, 400 )
        self.player2 = Player2(red, 700, 400)
        self.speed_p = SpeedPowerUp('assets/sprites/speed.png')
        self.speed_sound = pygame.mixer.Sound('assets/Music and FX/speed.wav')
        self.death_sound = pygame.mixer.Sound('assets/Music and FX/death.wav')
    #----------------------------------------------------------
    #drawing text as an image on screen
    def draw_text(self,text, font , text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img,(x,y))
    #----------------------------------------------------------
    #drawing players, borders and powerups
    def draw_elements(self):
        screen.fill(black)
        #Draw border 
        pygame.draw.rect(screen, white, border_rect, border_thickness)
         # Draw players
        self.player1.draw()
        self.player2.draw()
        self.speed_p.draw()
    #----------------------------------------------------------
    #detects collision and update player position stuff
    def update(self):
        self.player1.update()
        self.player2.update()
        self.p_collision()
        self.p1_crash()
        self.p2_crash()
        self.check_win()
        self.check_win()
    #----------------------------------------------------------
    #fun crash go brrr checks for loser 
    def p1_crash(self):
        if self.player1.check_collision() or self.player1.check_collision_with_other_player(self.player2):
            self.player2.score += 1 
            self.death_sound.play()
            self.round_reset()
    def p2_crash(self):
        if self.player2.check_collision() or self.player2.check_collision_with_other_player(self.player1):
            self.death_sound.play()
            self.player1.score += 1 
            self.round_reset()
    #----------------------------------------------------------
    # power up collision to decide if and who gets the speed boost
    def p_collision(self):
        if self.player1.body[0] == self.speed_p.position:
            self.player1.increase_speed()
            self.speed_sound.play()
            self.speed_p.active = False
            self.speed_p.position = self.speed_p.generate_position()
        if self.player2.body[0] == self.speed_p.position:
            self.player2.increase_speed()
            self.speed_sound.play()
            self.speed_p.active = False
            self.speed_p.position = self.speed_p.generate_position()
    #----------------------------------------------------------
    #check for a winner 
    def check_win(self):
        global game_over
        if self.player1.score >= 3:
            game_over = True
        elif self.player2.score >= 3:
            game_over = True
    #----------------------------------------------------------
    #reset the round
    def round_reset(self):
        screen.fill(black)
        self.player1.body = []
        self.player2.body = []
        self.player1.body = [(300, 400)]
        self.player2.body = [(700, 400)]
        self.player1.direction = pygame.K_d
        self.player2.direction = pygame.K_LEFT
        self.player1.reset_speed()
        self.player2.reset_speed()
        self.speed_p.active = True
        self.draw_elements()
    #----------------------------------------------------------
    #reset the game after a winner
    def hard_reset(self):
        global game_over
        game_over = False
        self.player1.score = 0
        self.player2.score = 0
        self.draw_elements()
    #----------------------------------------------------------
#menu class with menu things
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.menu_state = "Menu"
        # Loading button images
        play_img = pygame.image.load('assets/backgrounds/Play button.png').convert_alpha()
        quit_img = pygame.image.load('assets/backgrounds/Quit button.png').convert_alpha()
        instructions_img = pygame.image.load('assets/backgrounds/Instructions button.png').convert_alpha()
        back_img = pygame.image.load('assets/backgrounds/back button.png').convert_alpha()

        # Creating button instances
        self.play_button = Button(100, 800, play_img, 3)
        self.quit_button = Button(700, 800, quit_img, 3)
        self.instructions_button = Button(1300, 800, instructions_img, 3)
        self.back_button = Button(0, 0, back_img, 3)

        # Background image
        self.BG = pygame.image.load('assets/backgrounds/main menu.png')

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def run_menu(self):
        global screen
        run = True
        while run:
            if self.menu_state == "Menu":
                self.screen.blit(self.BG, (0, 0))
                if self.play_button.draw(self.screen) == 1:
                    self.menu_state = "play"
                if self.quit_button.draw(self.screen) == 1:
                    run = False
                if self.instructions_button.draw(self.screen) == 1:
                    self.menu_state = "instructions"
            elif self.menu_state == "instructions":
                screen.fill(black)
                menu.draw_text("Each player pilots their own avatar,", font_very_small,white, 100,300)
                menu.draw_text("Get you opponent to crash into your line or the border. First person to 3 points wins", font_very_small,white, 100,400)
                menu.draw_text("First person to 3 points wins", font_very_small,white, 100,500)
                menu.draw_text("P1 controls: w a s d", font_very_small,white, 100,600)
                menu.draw_text("P2 controls: up lefrt right down arrows ", font_very_small,white, 100,700)
                if self.back_button.draw(self.screen) == 1:
                    self.menu_state = "Menu"
            elif self.menu_state == "play":
                screen = pygame.display.set_mode((1000 , 800))
                screen.fill(black)
                play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()     
#Player1 stuff
class Player1:
    #Player1 basic declarations and properties
    def __init__(self, color, start_x, start_y):
        self.color = color
        self.body = [(start_x, start_y)]
        self.direction = pygame.K_d
        self.speed_multiplier = 1 
        self.score = 0
    #----------------------------------------------------------
    # check for new direction and player is heading and its new head
    def update(self):
        head_x, head_y = self.body[0]
        if self.direction == pygame.K_w:
            new_head = (head_x, head_y - cell_size)
        elif self.direction == pygame.K_s:
            new_head = (head_x, head_y + cell_size)
        elif self.direction == pygame.K_a:
            new_head = (head_x - cell_size, head_y)
        elif self.direction == pygame.K_d:
            new_head = (head_x + cell_size, head_y)

        self.body.insert(0, new_head)

    def change_direction(self, new_direction):
        if new_direction == pygame.K_w and self.direction != pygame.K_s:
            self.direction = new_direction
        elif new_direction == pygame.K_s and self.direction != pygame.K_w:
            self.direction = new_direction
        elif new_direction == pygame.K_a and self.direction != pygame.K_d:
            self.direction = new_direction
        elif new_direction == pygame.K_d and self.direction != pygame.K_a:
            self.direction = new_direction
    #----------------------------------------------------------
    #checks for collision with border, itself or other player
    def check_collision(self):
        head_x, head_y = self.body[0]
        if head_x < border_rect.left or head_x >= border_rect.right or \
                head_y < border_rect.top or head_y >= border_rect.bottom or \
                (head_x, head_y) in self.body[1:]:
            return True
        return False

    def check_collision_with_other_player(self, other_player):
       return self.body[0] in other_player.body
    #----------------------------------------------------------
    #draws the player
    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (segment[0], segment[1], cell_size, cell_size))
    #----------------------------------------------------------
    #manipulates speed for use of powerup
    def increase_speed(self):
        self.speed_multiplier = 2  # Double the speed
        clock.tick(10 * self.speed_multiplier)  # Adjust clock tick value
    
    def reset_speed(self):
        self.speed_multiplier = 1
        clock.tick(10 * self.speed_multiplier)
    #----------------------------------------------------------
#Player2 stuff
class Player2:
    #Player1 basic declarations and properties
    def __init__(self, color, start_x, start_y):
        self.color = color
        self.body = [(start_x, start_y)]
        self.direction = pygame.K_LEFT
        self.speed_multiplier = 1 
        self.score = 0
    #----------------------------------------------------------
    # check for new direction and player is heading and its new head
    def update(self):
        head_x, head_y = self.body[0]
        if self.direction == pygame.K_UP:
            new_head = (head_x, head_y - cell_size)
        elif self.direction == pygame.K_DOWN:
            new_head = (head_x, head_y + cell_size)
        elif self.direction == pygame.K_LEFT:
            new_head = (head_x - cell_size, head_y)
        elif self.direction == pygame.K_RIGHT:
            new_head = (head_x + cell_size, head_y)

        self.body.insert(0, new_head)

    def change_direction(self, new_direction):
        if new_direction == pygame.K_UP and self.direction != pygame.K_DOWN:
            self.direction = new_direction
        elif new_direction == pygame.K_DOWN and self.direction != pygame.K_UP:
            self.direction = new_direction
        elif new_direction == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
            self.direction = new_direction
        elif new_direction == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
            self.direction = new_direction
    #----------------------------------------------------------
    #checks for collision with border, itself or other player
    def check_collision(self):
        head_x, head_y = self.body[0]
        if head_x < border_rect.left or head_x >= border_rect.right or \
                head_y < border_rect.top or head_y >= border_rect.bottom or \
                (head_x, head_y) in self.body[1:]:
            return True
        return False

    def check_collision_with_other_player(self, other_player):
        return self.body[0] in other_player.body

    #----------------------------------------------------------
    #draws the player
    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (segment[0], segment[1], cell_size, cell_size))
    #----------------------------------------------------------
    def increase_speed(self):
        self.speed_multiplier = 2  # Double the speed
        clock.tick(10 * self.speed_multiplier)  # Adjust clock tick value
    
    def reset_speed(self):
        self.speed_multiplier = 1
        clock.tick(10 * self.speed_multiplier)
    #----------------------------------------------------------
#speed power stuff
class SpeedPowerUp:
    #basic properties of the speed power up
    def __init__(self, image):
        self.image = pygame.image.load('assets/sprites/speed.png')
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))  # Scale the image to match cell size
        self.position = self.generate_position()
        self.active = True
    #---------------------------------------------
    #getting a random position to spawn at
    def generate_position(self):
        # Generate a random position for the power-up within the game borders
        x = random.randint(0  + cell_size, 1000- cell_size)
        y = random.randint(0 + cell_size, 800 - cell_size)
        return x // cell_size * cell_size, y // cell_size * cell_size
    #---------------------------------------------
    #drawing the powerup on screen if it hasnt already been picked up
    def draw(self):
        if self.active:
            screen.blit(self.image, self.position)
    #---------------------------------------------
#Main initialization of instances through main class
menu = Menu(screen)
main = Main()

# Game loop
def play():
    global menu , main
    while menu.menu_state == "play":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu.menu_state = "Menu"
            elif event.type == pygame.KEYDOWN:
                if not game_over:  # Check if the game is not over
                    if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                        main.player2.change_direction(event.key)
                    elif event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                        main.player1.change_direction(event.key)
                else:
                    if event.key == pygame.K_SPACE:
                        main.hard_reset()
            # game_over conditions
        if game_over:
            screen.fill(black)
            main.draw_text("Finish!", font_big, white, 425, 100)
            main.draw_text("Player1 score: " + str(main.player1.score),font_small, blue, 400, 400)
            main.draw_text("Player2 score: " + str(main.player2.score),font_small, red, 400, 500)
            main.draw_text("Press spacebar to restart",font_big, white, 300, 700)
            pygame.display.flip()
        else: 
                
            main.draw_elements()
            main.update()
            pygame.display.flip()
            clock.tick(10)
    pygame.quit()
    sys.exit()   
#menu loop
while menu.menu_state == "Menu":
    menu.run_menu()
