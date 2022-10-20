import random
import math
from operator import itemgetter


# Basic Implementation - Imp 1
# imp = 1
# def emit_light(charge: list, min_charge: int):
#     """
#     The idea of this function is to check the charge of all the blocks
#     If 75% of blocks have enough charge then, we do nothing.

#     INPUT:
#     charge: list of charge for each block
#     min_charge: the minimum charge a block needs to emit enough light
#     """
#     over_75 = 0
#     for block in charge:
#         if block >= min_charge:
#             over_75 +=1
#     result = over_75 / len(charge)
#     if result>=0.75:
#         return "Blocks have enough battery to emit light with out turning off the speakers"
#     else:
#         return "We need to turn off charge for 20% of the speakers"

# Implementation 2 - Imp 2
imp = 2
def use_speakers(charge: list, min_charge: int):
    """
    The idea this time is to check the charge of each block
    Then based on the result we turn off the speaker for 20% of the blocks

    INPUT:
    charge: [(charge of block, bool: is light on?, bool: is speaker on?)]
    min_charge: minimal charge required for block to work
    """
    over_75 = 0
    for block_status in charge:
        #if block_status[1] == True:
        if block_status[0] >= min_charge:
            over_75 +=1
    result = over_75 / len(charge)


    if result>=0.75:
        return "The blocks can continue emitting light"
    else:
        block_status_lth = (sorted(charge, key=itemgetter(0)))
        p20 = math.ceil(0.2*len(charge))
        for i in range(p20):
            block_status_lth[i][2] = False
        return "20% of the block speakers have been turned off"

def main(imp: int):
    num_blocks = int(input('How many blocks are in the system'))
    if imp == 1:
        charge = random.sample(range(0, 100), num_blocks)
        min_charge = random.randint(0,100)

        print(emit_light(charge, min_charge))

    elif imp == 2:
        charge = [[random.randint(0,100), random.choice([True, False]), random.choice([True, False])] for _ in range(num_blocks)]
        min_charge = random.randint(0,100)

        print(use_speakers(charge, min_charge))

main(imp)

