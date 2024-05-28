"""
v2 of the spawn vehicle module
A Module to spawn a enemy vehicle on the screen
This module just works on the spawning of the enemy vehicle on the screen
not the ai or the movement of the vehicle

Things will be a lot easier now I have classes for everything
"""

import random
import pygame
from vehicles_vars import NPCVehicle, SpecialVehicle, TruckVehicle, EnemyVehicle, EnemyLanes, PLAYER_PREFIX, IMAGE_SUFFIX


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
        
        player_filename = self.get_player_filename(color)
        image = pygame.image.load(player_filename)
        self.image = image
        
        # Initiate the sprite class with the image object and x, y coords
        super().__init__(100, 500, image, 1.25)
        
        self.color = color
 

        

    def get_player_filename(self, color):
        return PLAYER_PREFIX + color + IMAGE_SUFFIX

    def get_coords(self):
        """Return the x, y coords as a tuple (x, y)"""
        return self.format()
    
        
class Background:
    """A class to represent the background image on the screen"""
    def __init__(self):
        """Initiator."""
        self.y1 = 0  # Start the first image at the top of the screen
        self.y2 = -background_image_object.get_height()  # Start the second image immediately above the first

        self.image_object = background_image_object

    def update_background(self):
        """Update the position of the background for scrolling effect."""
        self.y1 += 5
        self.y2 += 5

        # Reset y1 and y2 to create a seamless loop
        if self.y1 >= background_image_object.get_height():
            self.y1 = self.y2 - background_image_object.get_height()

        if self.y2 >= background_image_object.get_height():
            self.y2 = self.y1 - background_image_object.get_height()
    
    def show(self, screen: pygame.Surface):
        screen.blit(self.image_object, (0, self.y1))
        screen.blit(self.image_object, (0, self.y2))



class Enemy(Sprite):    
    """A class to represent the enemy vehicle on the screen"""
    def __init__(self, enemy_vehicle: EnemyVehicle, lane_x: int, spawn_in_y:int = -400):
        """Initiator"""
        
        enemy_image = pygame.image.load(enemy_vehicle.get_random_vehicle())

        # Initiate the inherited class 
        super().__init__(lane_x, spawn_in_y, enemy_image)
        # self.speed = random.randint(GameController.enemy_speed_range)
        
        self.speed = global_enemy_velocity

        enemy_objects.append(self)
    
    def move(self):
        """Move the enemy vehicle down the screen"""
        self.y += self.speed
    
    def offscreen_check(self):
        """Check if the enemy vehicle is offscreen if it is then delete it"""
        if self.y > DISPLAY_SIZE[1]:
            return True


class GameController:
    """A class to control the game state"""
    def __init__(self, fps=60):
        self.enemy_speed_range = (1, 5)
        self.enemy_objects = []
        self.spawn_rate = fps * 2
        self.next_car_spawn_interval = 0
        self.previous_lane = 0
        self.offscreen_limits = (-300, DISPLAY_SIZE[1] + 300)
    
    
   
            
            
    
    
    def update(self, screen: pygame.Surface, player_object: Player,
                enemy_objects: list[Enemy], spawn_cooldown: int):
        
        """Update the game state"""
        
       
        player_object.show(screen)
        
        # Move the enemy vehicles and check if they are offscreen
        # Create a copy so nothing breaks if anything is removed
        for enemy in enemy_objects[:]:
            enemy.move()

            # If the enemy is offscreen remove it from the list
            if enemy.offscreen_check():
                print("Removed enemy")
                enemy_objects.remove(enemy)
            else:
                enemy.show(screen)


        # Spawn a new enemy vehicle if the cooldown is 0
        if spawn_cooldown <= 0:
            
            # Randomly decide if the player should rest
            let_player_rest = random.randint(0, 9)
            if let_player_rest == 0:
                spawn_cooldown = random.randint(fps, int(fps * 2))
            else:
                spawn_cooldown = random.randint(int(fps / 2), fps)
            
            spawned_enemy: EnemyVehicle = self.decide_what_enemy()
            lane_chosen, lane_chosen_x = EnemyLanes.pick_random_lane()

            if lane_chosen == self.previous_lane:
                # Less repetition
                lane_chosen, lane_chosen_x = EnemyLanes.pick_random_lane()

             
            if lane_chosen == self.previous_lane + 1 or lane_chosen == lane_chosen - 1:
                # Less chance of being softlocked or randomly trapped
                Enemy(spawned_enemy, lane_chosen_x, spawn_in_y=-600)
            else:
                Enemy(spawned_enemy, lane_chosen_x)
                
            self.previous_lane = lane_chosen
                        

            
            
            
            return spawn_cooldown


        # Change the enemy spawn cooldown if it hasnt been reset
        spawn_cooldown -= 1

        return spawn_cooldown

        # self.spawn_enemy()
        # self.move_enemies()
        # self.check_collision()
    
    def decide_what_enemy(self) -> EnemyVehicle:
        """Spawn an enemy vehicle on the screen"""
        
        enemy_chance = random.randint(0, enemy_max_chance)

        if enemy_chance > 5:
            if enemy_chance % 2 == 0 and random.randint(0, 1) == 0: # 1 in 4 chance to be a truck
                return NPCVehicle()
            else:
                return TruckVehicle()
        
        else:

            return SpecialVehicle()
                

    
        
def make_background_object() -> pygame.Surface:
    # Define all background related variables
    background_image = pygame.image.load("background.png")
    background_scale_x =  DISPLAY_SIZE[0] / background_image.get_width()
    background_scale_y =  (DISPLAY_SIZE[1] * 2) / background_image.get_height()
    new_background_image = pygame.transform.scale(background_image, (int(background_image.get_width() * background_scale_x)
                                                            , int(background_image.get_height() * background_scale_y)))
    return new_background_image  



def display_text(screen: pygame.Surface, text: str, font_color = (255, 255, 255), x = DISPLAY_SIZE[0] // 2, y = 0 + 100):
    """Display text assuming the default x and y coords are the center top of the screen"""
    font = main_font
    text_object = font.render(text, True, font_color)
    text_rect = text_object.get_rect(center=(x, y))
    screen.blit(text_object, text_rect)
    



# Initialize pygame and set the display caption
pygame.init()
pygame.display.set_caption('Test sprites!')
screen = pygame.display.set_mode(DISPLAY_SIZE)


# Main routine

global_enemy_velocity = 3
background_image_object = make_background_object() # Used for testing purposes


available_fonts = pygame.font.get_fonts()
font_size = 30
print(available_fonts)
if "liberationmono" in available_fonts:
    main_font = pygame.font.SysFont("liberationmono", font_size)
else:
    # Handle case where Liberation Mono is not found
    print("Liberation Mono not found. Using a fallback font.")
    # Load a fallback font (e.g., pygame default font)
    main_font = pygame.font.Font(None, font_size)


# Defines the y upper and lower bound to give the illusion of screen wrapping for the background
# The upper bound is the highest the y of the image can be be so that the full image is displayed on the screen
# The lower bound is the lowest the image can be so the full image is displayed on the screen
# When the y is 0 the image isnt displayed on the screen (fully offscreen)
y_lower_bound = background_image_object.get_height() - DISPLAY_SIZE[1]
y_upper_bound = background_image_object.get_height()


background_object = Background()

fps = 90

enemy_spawn_cooldown = fps * 2 # First enemy will spawn after 2 seconds
last_lane_spawned_in = 0
enemy_max_chance = 100

finished = False
player_object = Player("blue")

in_menu = False

sound_death = pygame.mixer.Sound("other assets/goofy-crash.wav")
sound_game = pygame.mixer.Sound("other assets/racing_music.mp3")
game_controller = GameController(fps)

enemy_objects: list[Enemy] = []

clock = pygame.time.Clock()


print(f"Y upper bound: {y_upper_bound}, Y lower bound: {y_lower_bound}")
# Main loop
while not finished:
    
    
    background_object.update_background()
    background_object.show(screen)
    
    enemy_spawn_cooldown = game_controller.update(screen, player_object, 
                                                  enemy_objects, enemy_spawn_cooldown)
    
    pygame.display.update()
    
                
    clock.tick(fps)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player_object.x + player_object.image_object.get_width() >= 220:
            player_object.x -= 3
    if keys[pygame.K_RIGHT]:
        if player_object.x + player_object.image_object.get_width() <= DISPLAY_SIZE[0] - 150:
            player_object.x += 3
    
    if keys[pygame.K_UP]:
        if player_object.y + player_object.image_object.get_height() >= 122:
                player_object.y -= 3
    if keys[pygame.K_DOWN]:
        if player_object.y + player_object.image_object.get_height() <= DISPLAY_SIZE[1] - 2:
            player_object.y += 2

   
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


    # When the y get to y -787


# 190, 310, 430, 550