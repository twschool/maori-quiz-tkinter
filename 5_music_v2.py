"""
v2 of the simple music module
It now plays the music on a loop as long as the game is open
A stop music function was also added for when the player died and we want to stop all sounds 
"""

import pygame


DISPLAY_SIZE = [800, 700]
    

pygame.mixer.init()

# Initialize pygame and set the display caption
pygame.init()
pygame.display.set_caption('Test sprites!')
screen = pygame.display.set_mode(DISPLAY_SIZE)

def play_music():
    """Play music in the background"""
    pygame.mixer.music.load("other assets/racing_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    
    return pygame.mixer.music.get_busy()


def stop_music():
    """Stop all music playing"""
    pygame.mixer.music.stop()
    
    
# Main routine

finished = False
clock = pygame.time.Clock()

play_music()
# Main loop
while not finished:
    
    
    screen.fill((255, 120, 0))
    
    pygame.display.update()
    clock.tick(10)
    
    # Event handling
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            finished = True
        # For debugging purposes
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Stopping music")
            stop_music()