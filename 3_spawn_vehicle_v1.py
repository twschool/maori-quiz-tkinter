"""
v2 of the move sprites module
A Simple module to move the sprites around the screen.
This module changes the movement to be hold not press
"""

import pygame

DISPLAY_SIZE = [800, 700]
PLAYER_PREFIX = "cars/player/player-"
IMAGE_SUFFIX = ".png"


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def format(self):
        """Returns the players formatted coordinates (x, y) as a tuple"""
        return (self.x, self.y)

class Player(Coordinate):
    def __init__(self, color):
        # Initiate the coordinate class
        super().__init__(100, 500)
        

        self.color = color
        image = pygame.image.load(get_player_filename(color))
        
        # Scale the player 
        scale = 1.25

        self.image = pygame.transform.scale(image, (int(image.get_width() * scale)
                                                         , int(image.get_height() * scale)))

    def get_player_filename(self):
        return PLAYER_PREFIX + self.color + IMAGE_SUFFIX

    def get_coords(self):
        """Return the x, y coords as a tuple (x, y)"""
        return self.format()

def make_background_object() -> pygame.Surface:
    # Define all background related variables
    background_image = pygame.image.load("background.png")
    background_scale_x =  DISPLAY_SIZE[0] / background_image.get_width()
    background_scale_y =  (DISPLAY_SIZE[1] * 2) / background_image.get_height()
    new_background_image = pygame.transform.scale(background_image, (int(background_image.get_width() * background_scale_x)
                                                            , int(background_image.get_height() * background_scale_y)))
    return new_background_image



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
        
        
        if background_coords[0].y >= y_lower_bound:
            background_coords[0].y = y_upper_bound
        
        if background_coords[1].y >= y_lower_bound:
            background_coords[1].y = y_upper_bound

    
    move_background()
    
    screen.blit(background_image, background_coords[0].format())
    screen.blit(background_image, background_coords[1].format())
    

def update_player(player_object: Player):
    """Draw the player image on the screen"""
    
    screen.blit(player_object.image, player_object.get_coords())


# Initialize pygame and set the display caption
pygame.init()
pygame.display.set_caption('Test sprites!')
screen = pygame.display.set_mode(DISPLAY_SIZE)


player_coords = Coordinate(100, 100)

background_coords: list[Coordinate] = [Coordinate(0, 0), Coordinate(0, -700)]

background_image = make_background_object()
new_background_image_height = background_image.get_height()
fps = 60


# Defines the y upper and lower bound to give the illusion of screen wrapping for the background
y_upper_bound = -new_background_image_height
y_lower_bound = DISPLAY_SIZE[1]

# Get the players sprite based on the color given
player_images = ["black", "blue", "red", "white"]
get_player_filename = lambda player_color: PLAYER_PREFIX + player_color + IMAGE_SUFFIX

player_image_global = pygame.image.load( get_player_filename("red") )





# Main routine

finished = False
player_object = Player("blue")

# Main loop
while not finished:

    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))
    background()
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
                
        
        # For debugging purposes
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.dict["pos"])

        

def prank():
    # Force the user to open up a rickroll in their browser open it in both edge and their default browser
    import webbrowser
    
    for i in range(10):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        # time.sleep(5)
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        # time.sleep(5)
