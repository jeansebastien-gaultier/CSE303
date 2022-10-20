import random
import math

# Try to work with a Distributed Control Type of work
# class Regulator():
#     def __init__(self):
#         return

class Block:
    def __init__(self, charge = 100, light = 1, speaker = 1):
        self.charge = charge
        self.light = light
        self.speaker = speaker

    def light_status(self):
        return self.light

    def speaker_status(self):
        return self.speaker

    def what_charge(self):
        return self.charge

    def change_charge_per_moment(self):
        self.charge = self.charge - (random.randint(1,3))

class System:
    """
    We say that the system will be represented by blocks stacked on blocks (like the flag representation)
    We can assume that
    """
    def __init__(self, blocks, status = 1, min_charge = 35):
        """
        Input: 
        blocks: a matrix consisting of Block objects
        status: a boolean value telling us when 75% of blocks have enough charge
        min_charge: value at which a block doesn't have enough charge
        size: number of blocks in the system
        """
        self.blocks = blocks
        self.status = status
        self.min_charge = min_charge
        self.size = len(self.blocks) * len(self.blocks[0])

    def system_battery(self):
        """
        Find the overall system battery by averaging the battery of each block in the system
        """
        battery = 0
        for line in self.blocks:
            for blk in line:
                battery += blk.what_charge()
        perc = battery / self.size
        return perc
        
    def check_status(self):
        """
        Function that checks the status of our system every 'instant'
        Returns True if enough battery
        """
        over = 0
        for line in self.blocks:
            for blk in line:
                charge = blk.what_charge()
                if charge >= self.min_charge:
                    over += 1
        perc = over / self.size
        if perc >= 0.75:
            return True
        else:
            return False

    def turn_off_20(self):
        """
        Given a certain parameter, the 20% of blocks in each line with the lowest battery will turn off their speaker
        """
        for line in self.blocks:
            blk_bat = []
            for blk in line:
                blk_bat.append(blk.charge)
            x = sorted(blk_bat)
            val_20 = x[math.ceil(0.2*len(x))]
            for i in range(len(blk_bat)):
                if blk_bat[i] <= val_20:
                    line[i].speaker = 0
    
    def reduce_battery(self):
        for line in self.blocks:
            for blk in line:
                blk.change_charge_per_moment()
        
            



def main():
    """
    Build a program that will initialize a matrix of blocks of shape AxA
    Every "instant" the battery of the block will reduce and lose between (1%-3%)
    We check every "instant" the status of our system
    """
    matrix = [[Block() for _ in range (10)] for _ in range (10)]
    system = System(matrix)
    num_of_loops = 0
    bat = system.system_battery()
    while bat >= 20:
        if system.check_status() == False:
            system.turn_off_20()
        system.reduce_battery()
        bat = system.system_battery()
        num_of_loops +=1
    return num_of_loops

print(main())

# Limitations for the program:
    # We do not know which speakers should be turned off
    # What is the status of the system before we start
    # We do not know what it means: "blocks have enough battery"

# Freedoms we took:
    # Blocks with the lowest battery will have their speakers turned off
    # We initialize each block to start with lights on and speakers on with battery at 100%
    # We assume blocks under 35% do not have enough battery

# Personal Problem:
    # Time management - How do we implement the idea that there will only be 5 minutes left...

# Ideas:
    # Try to give an overall battery to the system