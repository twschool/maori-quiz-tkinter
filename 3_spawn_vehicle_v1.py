"""
v1 of the spawn vehicle module
A Module to spawn a enemy vehicle on the screen
This module just works on the spawning of the enemy vehicle on the screen
not the ai or the movement of the vehicle
"""

import random
import copy
import pygame
from vehicles_vars import NPCVehicle, SpecialVehicle, TruckVehicle, PLAYER_PREFIX, IMAGE_SUFFIX


DISPLAY_SIZE = [800, 700]



class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def format(self):
        """Returns the players formatted coordinates (x, y) as a tuple"""
        return (self.x, self.y)


class Sprite(Coordinate):
    """A class to represent a sprite on the screen"""
    
    def __init__(self, x, y, image_object: pygame.Surface, scale=1):
        """Initialize the sprite object with the x, y coordinates and the scaled image object"""
        super().__init__(x, y)
        
        # Scales the player image object to the given scale
        self.image_object = pygame.transform.scale(
                                                    image_object, (
                                                        int(image_object.get_width() * scale),
                                                        int(image_object.get_height() * scale)
                                                                      )
                                                   )
        
    def show(self, screen: pygame.Surface):
        """Displays the sprite on the screen"""
        screen.blit(self.image_object, self.format())


class Player(Sprite):
    """A class to represent the player on the screen"""
    def __init__(self, color):
        image = pygame.image.load(self.get_player_filename(color))
        
        # Initiate the sprite class with the image object and x, y coords
        super().__init__(image, 100, 500)
        
        self.color = color
        
        # Scale the player 
        scale = 1.25

        

    def get_player_filename(self):
        return PLAYER_PREFIX + self.color + IMAGE_SUFFIX

    def get_coords(self):
        """Return the x, y coords as a tuple (x, y)"""
        return self.format()
    
        
class Background(Sprite):
    """A class to represent the background image on the screen"""
    def __init__(self, x, y):
        super().__init__(x, y, pygame.image.load("background.png"))
    
    def update_background(self):
        self.y += 5
        self.y += 5
                
                
        if self.y >= y_lower_bound:
            self.y = y_upper_bound



class Enemy(Sprite):    
    """A class to represent the enemy vehicle on the screen"""
    def __init__(self, color):
        """Initiator"""
        
        # Initiate the 
        super().__init__(100, 100, pygame.image.load(self.get_enemy_filename(color)))
        self.color = color
        self.speed = random.randint(GameController.enemy_speed_range)


class GameController:
    def __init__(self, player_object, fps=60):
        self.enemy_speed_range = (1, 5)
        self.enemy_objects = []
        self.spawn_rate = fps * 2
        self.next_car_spawn_interval = 0
        self.previous_lane = 0
        self.background_object = self.make_background_object()
        self.offscreen_limits = (-300, DISPLAY_SIZE[1] + 300)
    
    def update(self, screen: pygame.Surface, player_object: Player,
               background_objects: list[Background], enemy_objects: list[Enemy]):
        
        """Update the game state"""
        
        for background_object in background_objects:
            background_object.show(screen)
        
        player_object.show(screen)
        
        for enemy in copy.deepcopy(enemy_objects):
            if enemy.y > self.offscreen_limits[1]:
                enemy_objects.remove(enemy)
       
        self.spawn_enemy()
        self.move_enemies()
        self.check_collision()
    
        
        






# Initialize pygame and set the display caption
pygame.init()
pygame.display.set_caption('Test sprites!')
screen = pygame.display.set_mode(DISPLAY_SIZE)





# Defines the y upper and lower bound to give the illusion of screen wrapping for the background
y_upper_bound = -Background.image.get_height()
y_lower_bound = DISPLAY_SIZE[1]

# # Get the players sprite based on the color given
# player_images = ["black", "blue", "red", "white"]
# get_player_filename = lambda player_color: PLAYER_PREFIX + player_color + IMAGE_SUFFIX

# player_image_global = pygame.image.load( get_player_filename("red") )





# Main routine

fps = 60
finished = False
player_object = Player("blue")


game_controller = GameController()

enemy_objects: list[Enemy] = []

# Main loop
while not finished:

    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))
    
    
    game_controller.update(screen, player_object, background_object, enemy_objects)
    update_player(player_object)
    
    
    pygame.display.update()
    clock.tick(fps)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player_object.x + player_object.image.get_width() >= 220:
            player_object.x -= 6
    if keys[pygame.K_RIGHT]:
        if player_object.x + player_object.image.get_width() <= DISPLAY_SIZE[0] - 150:
            player_object.x += 6
    
    if keys[pygame.K_UP]:
        if player_object.y + player_object.image.get_height() >= 122:
                player_object.y -= 6
    if keys[pygame.K_DOWN]:
        if player_object.y + player_object.image.get_height() <= DISPLAY_SIZE[1] - 2:
            player_object.y += 4

    # Event handling
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            finished = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                print(player_object.get_coords())
                
        
        # For debugging purposes
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.dict["pos"])
