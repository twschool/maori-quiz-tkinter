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


class Vehicle:
    def __init__(self, prefix, images, suffix):
        self.prefix = prefix
        self.images = images
        self.suffix = suffix
    
    def get_random_vehicle(self):
        return self.prefix + random.choice(self.images) + self.suffix
    

class NPCVehicle(Vehicle):
    def __init__(self):
        super().__init__(NPC_PREFIX, npc_images, IMAGE_SUFFIX)

class SpecialVehicle(Vehicle):
    def __init__(self):
        super().__init__(SPECIAL_VECHICLE_PREFIX, special_images, IMAGE_SUFFIX)

class TruckVehicle(Vehicle):
    def __init__(self):
        super().__init__(TRUCK_PREFIX, truck_images, IMAGE_SUFFIX)
        
