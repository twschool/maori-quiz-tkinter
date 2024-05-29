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
lane1_x = 190
lane2_x = 310
lane3_x = 430
lane4_x = 550

class EnemyVehicle:
    def __init__(self, prefix, images, suffix):
        self.prefix = prefix
        self.images = images
        self.suffix = suffix
        self.scale = 1.25
    
    def get_random_vehicle(self):
        return self.prefix + random.choice(self.images) + self.suffix
    

class NPCVehicle(EnemyVehicle):
    def __init__(self):
        super().__init__(NPC_PREFIX, npc_images, IMAGE_SUFFIX)


class SpecialVehicle(EnemyVehicle):
    def __init__(self):
        super().__init__(SPECIAL_VECHICLE_PREFIX, special_images, IMAGE_SUFFIX)
        self.scale = 1


class TruckVehicle(EnemyVehicle):
    def __init__(self):
        super().__init__(TRUCK_PREFIX, truck_images, IMAGE_SUFFIX)


class EnemyLanes:
    """A class to store the enemy lanes x coords"""

    
    def __init__(self):
        """Initialize the enemy lanes x coords
        This part of the function is unlikely to be used in the final version"""
        self.y_range = (-30, -50)

        self.lane1_x = 190
        self.lane2_x = 310
        self.lane3_x = 430
        self.lane4_x = 550
    
    @staticmethod
    def pick_random_lane():
        """Return a random lane x coordinate"""
        return random.choice (
            [(1, lane1_x), (2, lane2_x), (3, lane3_x), (4, lane4_x)])

    @staticmethod
    def lane_x_to_lane_number():
        """Return the lane number based on the x coordinate"""
        return {lane1_x: 1, lane2_x: 2, lane3_x: 3, lane4_x: 4}

    

        
