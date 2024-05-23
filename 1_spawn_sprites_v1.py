"""v1 of the spawn sprites module
A Simple module to spawn a sprite on the screen"""

import pygame

pygame.init()



DISPLAY_SIZE = [1000, 600]


PLAYER_PREFIX = "cars/player/player-"
IMAGE_SUFFIX = ".png"
PLAYER_IMAGES = ["black", "blue", "red", "white"]


# Get the players sprite based on the color given
get_player_filename = lambda player_color: PLAYER_PREFIX + player_color + IMAGE_SUFFIX

# Get blue car sprite
player_image_blue = get_player_filename("blue")




# Hardcoded sprite values
player_image = ["cars/player/player-black.png", "cars/player/player-blue.png", 
                "cars/player/player-red.png", "cars/player/player-white.png"]


# Get blue car sprite the hardcoded way
player_image_blue = player_image[1]



screen = pygame.display.set_mode(DISPLAY_SIZE)


image = pygame.image.load( get_player_filename("red") )

pygame.display.set_caption('Test sprites!')



test_coords = [100, 100]
finished = False

while not finished:

    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    screen.blit(image, test_coords)
    pygame.display.update()
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN or event.type == pygame.K_UP:
            if event.key == pygame.K_UP:
                test_coords[0] += 20
                
        elif event.type == pygame.MOUSEMOTION:
            print(event.dict["pos"])


