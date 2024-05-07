import pygame
import random
import time


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


DINO_GAME_BACKGROUND_COLOR = (247, 247, 247)
DINO_GAME_CACTUS_COLOR = (83, 83, 83)


GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

spawn_cactus_delay = 10
global_cactus_y = 415

DISPLAY_SIZE = [1000, 600]

pygame.init()
pygame.mixer.init()

score = 0
death_sound = pygame.mixer.Sound("audio/death.mp3")

music_tracks = ["audio/music.mp3", "audio/music1.mp3"]
track = random.choice(music_tracks)
bg_music = pygame.mixer.Sound(track)

bg_music.play(2)

screen = pygame.display.set_mode(DISPLAY_SIZE)

llama = pygame.image.load("images/Llama.png").convert_alpha()
llama = pygame.transform.scale(llama, (50, 50))

ground = pygame.image.load("images/ground.png").convert_alpha()
ground = pygame.transform.scale(ground, (1000, 200))

cactus = pygame.image.load("images/cactus.png").convert_alpha()
cactus = pygame.transform.scale(cactus, (50, 50))

font = pygame.font.Font('freesansbold.ttf', 32)

display_text = "Score: "

pygame.display.set_caption('Llama game')

global_gravity = 2
cactus_move_amount = 12
fps = 60

""" The ratio of fps that the cactus uses as its random timings eg at 60fps and a ratio of 1
the minimum frame delay between the previous cactus is 60 frames (1 second)

if the ratio of fps is 0.5 then the minmum delay between a cactus spawning moves to """
if fps > 30:
    ratio_of_fps_min = 0.8
else:
    ratio_of_fps_min = 0.75

ratio_of_fps_max = lambda: ratio_of_fps_min * 2 # Calculated value

def calculate_cactus_delay():
    return random.randint(round(ratio_of_fps_min * fps), round(ratio_of_fps_max() * fps))


# A list for all cacutus being spawned on screen. Cactus will be removed when offscreen
all_cactus = []


class Llama_object:
    def __init__(self):
        self.x = 100
        self.y = 400
        self.width = 50
        self.height = 50
        self.velocity = 0
        # self.gravity = 5

    def is_onground(self):
        if self.y == 400:
            return True
        
        return False

    def jump(self):
        """Make llama jump"""
        if self.is_onground():
            self.velocity = -26
        else:
            self.velocity += 20


    def move(self):
        self.velocity += global_gravity
        self.y += self.velocity

        # Make llama stop at the y of 400
        if self.y > 400:
            self.y = 400
            self.velocity = 0

    def draw(self):
        screen.blit(llama, (self.x, self.y))




def change_cactus_delay():
    global spawn_cactus_delay
    """Defines the amount of delay in frames that the next cactus will spawn in"""
    delay = calculate_cactus_delay()
    spawn_cactus_delay = delay
    return delay # If needed


def update_llama():
    """Render llama on screen"""
    llama_obj.move()
    llama_obj.draw()


def render_ground():
    """Render ground on screen"""
    screen.blit(ground, (0, 330))


def get_highscore():
    """Get the highscore from a file"""
    import os

    if os.path.exists("highscore.txt") is False:
        with open("highscore.txt", "w") as file:
            file.write("0")
    else:
        
        with open("highscore.txt", "r") as file:
            return file.read()

import pygame.font

def spawn_cactus():
    """Create new cactus"""
    all_cactus.append((1100, "normal"))


def render_text():
    display_text = "Score: " + str(score)  # Update display_text to include the score value
    text = font.render(display_text, True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = (DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] / 4)
    screen.blit(text, text_rect)


def add_watermark():
    """Add a fun watermark to the screen"""
    watermark = pygame.image.load("images/watermark.png").convert_alpha()
    watermark = pygame.transform.scale(watermark, (200, 50))
    screen.blit(watermark, (800, 550))


def update_and_render_cactus(cactus_delay):
    """A general function to update and render all the cactus stuff"""

    def render_cactus():
        """Render cactus on screen"""
        for index, (cactus_x, cactus_type) in enumerate(all_cactus):
            # Cactus type may be implemented later giving taller cactus's
            screen.blit(cactus, (cactus_x, global_cactus_y))
            # print(f"Rendered cactus ")
        

    def move_cactus():
        """Move cactus left slowly"""
        global all_cactus

        all_cactus_modified = [(cactus_x - cactus_move_amount, cactus_type) 
                               for cactus_x, cactus_type in all_cactus 
                               if cactus_x > -200 # Removes all offscreen cactus's
                               ]
        all_cactus = all_cactus_modified


    if cactus_delay > 0:
        # print(f"Checking delay (its at {cactus_delay})")
        cactus_delay -= 1
    else:
        print("Spawning cactus :!")
        spawn_cactus()
        cactus_delay = change_cactus_delay()

    
    move_cactus()
    render_cactus()


    return cactus_delay



def llama_death():
    pygame.mixer.stop()
    screen.fill(BLACK)
    death_sound.play()

    time.sleep(2)
    pygame.quit()


def background():
    """Render background on screen"""
    screen.fill(WHITE)

def check_collision(llama_object: Llama_object):
    """Check if llama collides with cactus - To be implemented later"""
    # If the 108-140 x (players zone)
    # 417 y (max height of the cactus)

    for cactus_x, cactus_type in all_cactus:
        if cactus_x > 108 and cactus_x < 140:
            print(f"The x is in the players zone! {cactus_x}")
            print(f"The player y {llama_object.y}")
            # The cactus is in the players zone
            if llama_object.y > 370:
                # and there is a collision
                llama_death()




def make_harder():
    global ratio_of_fps_min
    global fps
    fps += 0.01 # Makes the games pace go faster
    ratio_of_fps_min -= 0.00015 # Makes the cactus's spawn more frequently 
    # Every hundred fps the fps increases by one


# Main routine
llama_obj = Llama_object()
clock = pygame.time.Clock()

game_finished = False



while game_finished is not True:
    background()
    
    score += 1
    render_ground()
    update_llama()
    render_text()
    check_collision(llama_obj)
    make_harder()
    spawn_cactus_delay = update_and_render_cactus(spawn_cactus_delay)
    

    pygame.display.update()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN or event.type == pygame.K_UP:
            if event.key == pygame.K_SPACE:
                llama_obj.jump()
        elif event.type == pygame.MOUSEMOTION:
            print(event.dict["pos"])
        
        