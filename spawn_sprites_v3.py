"""
v3 of the spawn sprites module
A Simple module to spawn the player on the screen 
using arrow keys to move the player rotation has been removed.

A Looping background has been added to the screen to give the illusion of movement."""

import pygame

DISPLAY_SIZE = [800, 700]
PLAYER_PREFIX = "cars/player/player-"
IMAGE_SUFFIX = ".png"


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def format(self):
        return (self.x, self.y)


class Player:
    def __init__(self, color):
        self.color = color
        self.image = pygame.image.load(get_player_filename(color))

    def get_player_filename(self):
        return PLAYER_PREFIX + self.color + IMAGE_SUFFIX


def background():
    """Draw the background image which slowly scrolls down the screen with seamless looping"""
    
    def move_background():
        """Move the background down the screen with the second background image 
        following the first to wrap around to create a seamless transition"""
            
        # How this will work
        # 1. Move the background down the screen
        # 2. Have two images working in parallel to create a seamless transition
        # NOTE: There will only be two images in the background_coords list so we can hardcode stuff
        
        background_coords[0].y += 5
        background_coords[1].y += 5
        
        
        if background_coords[0].y >= 700:
            background_coords[0].y = -700
            background_coords[1].y = 0
        
        if background_coords[1].y >= 700:
            background_coords[1].y = -700
            background_coords[0].y = 0
    
    move_background()
    
    screen.blit(background_image, background_coords[0].format())
    screen.blit(background_image, background_coords[1].format())
    

def player():
    """Draw the player image on the screen"""
    
    screen.blit(player_image_global, player_coords.format())


# Initialize pygame and set the display caption
pygame.init()
pygame.display.set_caption('Test sprites!')
screen = pygame.display.set_mode(DISPLAY_SIZE)

# Define all constants and variables
player_velocity = 0
velocity = Coordinate(0, 0) # Store the players velocity as a coordinate x,y
player_coords = Coordinate(100, 100)
background_coords: list[Coordinate] = [Coordinate(0, 0), Coordinate(0, -700)]


# Get the players sprite based on the color given
player_images = ["black", "blue", "red", "white"]
get_player_filename = lambda player_color: PLAYER_PREFIX + player_color + IMAGE_SUFFIX

player_image_global = pygame.image.load( get_player_filename("red") )
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, DISPLAY_SIZE)

fps = 60


# Main routine

finished = False

# Main loop
while not finished:

    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))
    background()
    player()
    
    pygame.display.update()
    clock.tick(fps)


    # Event handling
    for event in pygame.event.get():
        print(event.dict)
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            # Player movement (horizontal only for now)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_coords.x -= 20
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_coords.x += 20

            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.dict["pos"])
