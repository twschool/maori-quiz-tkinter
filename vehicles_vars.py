"""A Module to store the vehicle variables"""

import random

PLAYER_PREFIX = "cars/player/player-"
NPC_PREFIX = "cars/npc/npc-"
SPECIAL_VECHICLE_PREFIX = "cars/special/"
TRUCK_PREFIX = "cars/truck/truck-"
IMAGE_SUFFIX = ".png"

npc_images = ["black", "red", "white", "yellow"]
special_images = ["firetruck", "limo-black", "limo-white"]
truck_images = ["1", "2", "3", "4"]


class EnemyVehicle:
    def __init__(self, prefix, images, suffix):
        self.prefix = prefix
        self.images = images
        self.suffix = suffix
    
    def get_random_vehicle(self):
        return self.prefix + random.choice(self.images) + self.suffix
    

class NPCVehicle(EnemyVehicle):
    def __init__(self):
        super().__init__(NPC_PREFIX, npc_images, IMAGE_SUFFIX)


class SpecialVehicle(EnemyVehicle):
    def __init__(self):
        super().__init__(SPECIAL_VECHICLE_PREFIX, special_images, IMAGE_SUFFIX)


class TruckVehicle(EnemyVehicle):
    def __init__(self):
        super().__init__(TRUCK_PREFIX, truck_images, IMAGE_SUFFIX)


class EnemyLanes:
    """A class to store the enemy lanes x coords"""
    def __init__(self):
        self.y_range = (-30, -50)

        self.lane1_x = 190
        self.lane2_x = 310
        self.lane3_x = 430
        self.lane4_x = 550
    
    def pick_random_lane():
        lane1_x = 190
        lane2_x = 310
        lane3_x = 430
        lane4_x = 550
        """Return a random lane x coordinate"""
        return random.choice([lane1_x, lane2_x, 
                              lane3_x, lane4_x])

        
