"""
30/05/2024 2:30 AM
Made by: Thomas Wilson

This is 
v2 of the final version
This module is all of the previous modules combined into one

This is the polished and final version of this racing car program
"""

import random
import pygame
from vehicles_vars import NPCVehicle, SpecialVehicle, TruckVehicle, EnemyVehicle, EnemyLanes, PLAYER_PREFIX, IMAGE_SUFFIX


DISPLAY_SIZE = [800, 700]
HIGHSCORE_FILENAME = "other assets/highscore.txt"



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
        super().__init__(300, 500, image, 1.25)
        
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
        

        enemy_objects.append(self)
    
    def move(self):
        """Move the enemy vehicle down the screen"""
        self.y += global_enemy_velocity + random.uniform(0, 0.5) # Add a bit of randomness to the speed
    
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
    
    
    def collision_detection(self, player_object: Player, enemy_objects: list[Enemy]):
        """Check if the player has collided with an enemy vehicle"""
        
        player_rect = player_object.image_object.get_rect(topleft=player_object.format())
        
        
        
        for enemy in enemy_objects:
            # Collision detection using the rect method and colliderect
            if player_rect.colliderect(enemy.image_object.get_rect(topleft=enemy.format())):
                # If the player has collided with an enemy vehicle then return true
                return True
            
        return False
            
            
    
    
    def update(self, screen: pygame.Surface, player_object: Player,
                enemy_objects: list[Enemy], spawn_cooldown: int):
        
        """Update the game state"""
        
        global score
        global global_enemy_velocity
       
        player_object.show(screen)
        
        # Move the enemy vehicles and check if they are offscreen
        # Create a copy so nothing breaks if anything is removed
        for enemy in enemy_objects[:]:
            enemy.move()



            # If the enemy is offscreen remove it from the list
            if enemy.offscreen_check():
                if (score + 1) % 10 == 0:
                    global_enemy_velocity *= 1.2
                    print(f"New velocity: {global_enemy_velocity}")
                score += 1
                enemy_objects.remove(enemy)
            else:
                enemy.show(screen)


        # Spawn a new enemy vehicle if the cooldown is 0
        if spawn_cooldown <= 0:
            
            # Randomly decide if the player should rest
            let_player_rest = random.randint(0, 9)
            if let_player_rest == 0:
                ratioed_framerate = fps / (global_enemy_velocity / original_enemy_velocity)
                # print(f"{int(ratioed_framerate)} ratioed framerate")


                # spawn_cooldown = random.randint(fps, int(fps * 2))
                spawn_cooldown = random.randint(int(ratioed_framerate / 2), int(ratioed_framerate))
            else:
                ratioed_framerate = fps / (global_enemy_velocity / original_enemy_velocity)
                # print(f"{int(ratioed_framerate)} ratioed framerate")
                spawn_cooldown = random.randint(int(ratioed_framerate / 2), int(ratioed_framerate))
            
            spawned_enemy: EnemyVehicle = self.decide_what_enemy()
            lane_chosen, lane_chosen_x = EnemyLanes.pick_random_lane()

            if lane_chosen == self.previous_lane:
                # Less repetition
                lane_chosen, lane_chosen_x = EnemyLanes.pick_random_lane()
     
            
            
             
            if lane_chosen == self.previous_lane + 1 or lane_chosen == self.previous_lane - 1:
                # Less chance of being softlocked
                # If the player is going to be trapped then move the car up more to leave a gap
                spawn_cooldown += int(fps / 3)
                self.previous_lane = -1 # Make it so any car in any lane can spawn
                Enemy(spawned_enemy, lane_chosen_x, spawn_in_y=-600)
            else:
                Enemy(spawned_enemy, lane_chosen_x)
                
            self.previous_lane = lane_chosen
                        

            
            
            
            return spawn_cooldown


        # Change the enemy spawn cooldown if it hasnt been reset
        spawn_cooldown -= 1

        return spawn_cooldown

   
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


def play_music():
    """Play music in the background"""
    pygame.mixer.music.load("other assets/racing_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    
    return pygame.mixer.music.get_busy()


def stop_music():
    """Stop all music playing"""
    pygame.mixer.music.stop()
    


def display_text(screen: pygame.Surface, text: str, font_color = (255, 255, 255), x = DISPLAY_SIZE[0] // 2, y = 0 + 100):
    """Display text assuming the default x and y coords are the center top of the screen"""
    font = main_font
    text_object = font.render(text, True, font_color)
    text_rect = text_object.get_rect(center=(x, y))
    screen.blit(text_object, text_rect)
    

def start_screen():
    """Display the start screen before the game starts"""
    in_menu = True
    screen.fill((0, 0, 0))
    background_object.show(screen)
    display_text(screen, "Press space to start", y = DISPLAY_SIZE[1] // 2)
    pygame.display.update()
    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    in_menu = False
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        clock.tick(20)


def death_menu():
    """Display the death menu to see if the player wants to play again"""
    in_menu = True
    screen.fill((0, 0, 0))
    background_object.show(screen)
    # orange = (255, 165, 0)
    display_text(screen, "Game Over", y = 20, font_color=(255, 165, 0))
    display_text(screen, "Press [Enter] to play again or", y = 50, font_color=(255, 165, 0))
    display_text(screen, "Press [Esc] to exit", y = 80, font_color=(255, 165, 0))
    pygame.display.update()
    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_menu = False
                    return False
                elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    in_menu = False
                    return True
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        clock.tick(20)


# Initialize pygame and set the display caption
pygame.init()
pygame.display.set_caption('Test sprites!')
screen = pygame.display.set_mode(DISPLAY_SIZE)


# Main routine

global_enemy_velocity = 3
original_enemy_velocity = global_enemy_velocity
background_image_object = make_background_object() # Used for testing purposes


available_fonts = pygame.font.get_fonts()
font_size = 30
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
score = 0

try:
    with open(HIGHSCORE_FILENAME) as highscore_file:
        highscore = int(highscore_file.read())
        
except:
    with open(HIGHSCORE_FILENAME, "w") as highscore_file:
        highscore_file.write("0")
        highscore = 0

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

has_colided = False

print(f"Y upper bound: {y_upper_bound}, Y lower bound: {y_lower_bound}")
# Main loop


# Start screen - text displays (press space to start) and the when space is pressed the game loop is started


start_screen()
play_music()


while not finished:
    
    
    background_object.update_background()
    background_object.show(screen)
    
    enemy_spawn_cooldown = game_controller.update(screen, player_object, 
                                                  enemy_objects, enemy_spawn_cooldown)
    has_colided = game_controller.collision_detection(player_object, enemy_objects)
    display_text(screen, f"Score: {score}", y = 20, font_color=(120, 120, 255))
    
    score_display = highscore if score < highscore else score
    
    
    display_text(screen, f"Highscore: {score_display}", y = 50, font_color=(120, 120, 255))
    
    pygame.display.update()
    if has_colided:
        sound_death.play()
        pygame.display.update()
        
        animation_fps = 10
        player_image_object = player_object.image
        
        
        # Rotate car 3 times over the space of 2 seconds
        screen.fill((0, 0, 0))

        end_text = f"Final Score: {score}"

        if score > highscore:
            with open(HIGHSCORE_FILENAME, "w") as file:
                file.write(str(score))
                
            end_text = f"NEW HIGHSCORE: {score}"
            
        for i in range(3):
            for angle in range(0, 360, 40):
                screen.fill((0, 0, 0))
                background_object.show(screen)
                
                player_image_object = pygame.transform.rotate(player_image_object, 10)          
                screen.blit(player_image_object, (player_object.x, player_object.y))
                display_text(screen, end_text, font_color=(255, 255, 255))
                pygame.display.update()
                
                clock.tick(animation_fps)
        is_play_again = death_menu()

        if is_play_again == False:
            finished = True
        else:
            # Prepare the game to restart
            global_enemy_velocity = original_enemy_velocity
            player_object = Player("blue")
            enemy_objects.clear()
            score = 0

        continue
                
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