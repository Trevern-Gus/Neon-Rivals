import pygame
import sys
import random
# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Two-Player Snake')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)

# Define constants
cell_size = 20  # Size of each cell in the grid
border_thickness = 10  # Thickness of the border

# Define border dimensions
border_rect = pygame.Rect(border_thickness, border_thickness,
                          screen_width - 2 * border_thickness,
                          screen_height - 2 * border_thickness)
#main class where everything will eventually take place                          
class Main:
    def __init__(self):
        self.speed_image = pygame.image.load('assests/player models and items/speed.png')
        self.shield_image = pygame.image.load('assests/player models and items/shield.png')
        self.player1 = Player(green, screen_width // 4, screen_height // 2)
        self.player2 = Player2(blue, 3 * screen_width // 4, screen_height // 2)
        self.speed_up = PowerUp(screen_width, screen_height, self.speed_image, (20, 20), "speed")
        self.shield_up = PowerUp(screen_width, screen_height, self.shield_image, (20, 20), "invincibility")
    
    #def draw_elements():
        
    def handle_collisions_and_powerups(self):
        if self.player1.check_collision() or self.player2.check_collision() or self.player1.check_collision_with_other_player(self.player2) or self.player2.check_collision_with_other_player(self.player1):
            print("Game Over")
            pygame.quit()
            sys.exit()

        if self.speed_up.rect.colliderect(self.player1.body([0,0])):
            self.speed_up.apply_power_up(self.player1)
            self.speed_up.respawn()

        if self.shield_up.rect.colliderect(self.player1.body[0]):
            self.shield_up.apply_power_up(self.player1)
            self.shield_up.respawn()
    
        if self.speed_up.rect.colliderect(self.player2.body[0]):
            self.speed_up.apply_power_up(self.player2)
            self.speed_up.respawn()

        if self.shield_up.rect.colliderect(self.player2.body[0]):
            self.shield_up.apply_power_up(self.player2)
            self.shield_up.respawn()

# Player class
class Player2:
    def check_collision_with_other_player(self, other_player):
        return self.body[0] in other_player.body

    def __init__(self, color, start_x, start_y):
        self.color = color
        self.body = [(start_x, start_y)]
        self.direction = pygame.K_RIGHT
        self.speed_multiplier = 1  # Initial speed multiplier

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

    def check_collision(self):
        head_x, head_y = self.body[0]
        if head_x < border_rect.left or head_x >= border_rect.right or \
                head_y < border_rect.top or head_y >= border_rect.bottom or \
                (head_x, head_y) in self.body[1:]:
            return True
        return False

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (segment[0], segment[1], cell_size, cell_size))
    
    def increase_speed(self):
        self.speed_multiplier = 2  # Double the speed
        clock.tick(10 * self.speed_multiplier)  # Adjust clock tick value
# Player2 class
class Player:
    def check_collision_with_other_player(self, other_player):
        return self.body[0] in other_player.body

    def __init__(self, color, start_x, start_y):
        self.color = color
        self.body = [(start_x, start_y)]
        self.direction = pygame.K_d
        self.speed_multiplier = 1  # Initial speed multiplier

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

    def check_collision(self):
        head_x, head_y = self.body[0]
        if head_x < border_rect.left or head_x >= border_rect.right or \
                head_y < border_rect.top or head_y >= border_rect.bottom or \
                (head_x, head_y) in self.body[1:]:
            return True
        return False

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (segment[0], segment[1], cell_size, cell_size))

    def increase_speed(self):
        self.speed_multiplier = 2  # Double the speed
        clock.tick(10 * self.speed_multiplier)  # Adjust clock tick value
#Power up class
class PowerUp():
    def __init__(self, screen_width, screen_height, image, scale, power_type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(
            random.randint(border_thickness, screen_width - border_thickness - scale[0]),
            random.randint(border_thickness, screen_height - border_thickness - scale[1])
        ))
        self.scale = scale
        self.power_type = power_type  # Type of power-up (e.g., "speed", "invincibility")
        self.duration = 5000  # Duration of the power-up effect in milliseconds
        self.applied = False

    def draw(self, screen):
        screen.blit(pygame.transform.scale(self.image, self.scale), self.rect)

    def apply_power_up(self, player):
        if self.power_type == "speed":
            player.increase_speed()
        elif self.power_type == "invincibility":
            player.activate_invincibility()

    def update(self, player):
        if not self.applied and pygame.sprite.collide_rect(self, player):
            self.apply_power_up(player)
            self.applied = True

        # Reduce duration of power-up effect
        if self.applied:
            self.duration -= pygame.time.get_ticks()
            if self.duration <= 0:
                self.remove_power_up(player)

    def remove_power_up(self, player):
        if self.power_type == "speed":
            player.reset_speed()
        elif self.power_type == "invincibility":
            player.deactivate_invincibility()
        self.kill()  # Remove the power-up from the game

    def respawn(self):
        self.rect.topleft = (
            random.randint(border_thickness, screen_width - border_thickness - self.scale[0]),
            random.randint(border_thickness, screen_height - border_thickness - self.scale[1])
        )
        self.applied = False
        self.duration = 5000  # Reset the duration

    def check_collision_with_player(self, player_rect):
        return self.rect.colliderect(player_rect)

main = Main()
player1 = Player(green, screen_width // 4, screen_height // 2)
player2 = Player2(blue, 3 * screen_width // 4, screen_height // 2)
# Clock to control the game's speed
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                player2.change_direction(event.key)
            elif event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                player1.change_direction(event.key)

    # Draw the border
    pygame.draw.rect(screen, white, border_rect, border_thickness)

    # Draw players
    player1.draw()
    player2.draw()
    # Clear the screen
    screen.fill(black)
    player1_rect = pygame.Rect(player1.body[0][0], player1.body[0][1], cell_size, cell_size)
    player2_rect = pygame.Rect(player2.body[0][0], player2.body[0][1], cell_size, cell_size)
    # Update players
    player1.update()
    player2.update()

    main.handle_collisions_and_powerups()

    pygame.display.flip()
    clock.tick(10)  # Adjust this value to change the game speed

pygame.quit()
sys.exit()
