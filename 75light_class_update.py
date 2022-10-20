# class Regulator():
#     """
#     Once we have finalized understanding what our MODEL is and what we want our system to do we will start working 
#     on an implementatio of this class

#     The goal of this class will be to have control over our entire system without needing human interaction

#     The parameters will be set, the regulator will be launched with an initial state for our model, and then it 
#     will run by itself and will be making modifications by itself on the system.
#     """
#     def __init__():
#         return 

#     def Digital_Twins():
#         """
#         Run the overall system status at time "t+1" to predict the future state and modify current state to maintain
#         the goal we want
#         """
#         return

#     def Analyze_DT():
#         """
#         Analyze the results given following the Digital Twins function
#         """
#         return 

#     def Modify_System():
#         """
#         Given the results of the analysis of the Digital Twins, the regulator will have the role to modify the state
#         of the system all while respecting the desired model
#         """
#         return

class Block():
    """
    This class will be used to define each individual item within the system (globally it can be a phone, dryer...)
    in our case we are working with 'blinky blocks'.

    Each block will be able to evaluate itself and will be able to get information from it's neighbors
    This will be able to add a way to have aggregate programming, the communication amongst the blocks
    """

    def __init__(self, right, left, battery, light, sound, sens_light, sens_sound, HS):
        """
        Initialization of the block
        INPUT:
            right: another instance of Block
            left: another instance of Block
            battery: integer corresponding to battery percentage
            light: integer corresponding to quantity of light emitted by the block
            sound: integer corresponding to the quantity of sound emitted by the block
            HS: boolean corresponding to whether or not the block is still functionning

        Addition of exterior environmental elements
            sens_light: integer corresponding to how much exterior light is sensed by the block
            sens_sound: integer corresponding to how much exterior sound is sensed by the block
        """
        self. right = right
        self.left = left
        self.battery = battery
        self.light = light
        self.sound = sound
        self.sens_light = sens_light
        self.sens_sound = sens_sound
        self.HS = HS

    def battery_consumption(self):
        """
        Based on the quantity of light/sound emmited the battery decreases proportionally (i.e. if light emits 100 lux
        then it looses 0.1% and if it emits 200% then it looses 0.2%)
        """
        return

    def neigh_info(self, neigh: list, n: int):
        """
        Given n neighbors, the block can evaluate it's current state and compare it to theirs
        """
        return

    
class System():
    """
    This class will be used to evaluate the overall status of our blocks put all together, it is supposed to
    represent the model we want to have.

    !!! THE IDEA OF HAVING A SET MODEL HAS TO IMPLEMENTED CORRECTLY !!!
    """

    def __init__(self, blocks, status, size):
        """
        Initialize the system as a whole
        Input: 
        blocks: a matrix consisting of Block objects
        status: a boolean value telling us whether or not the system is running correctly with respect to the desired model
        size: number of blocks in the system
        """
        self.blocks = blocks
        self.status = status
        self.size = len(self.blocks) * len(self.blocks[0])

    def battery(self, param):
        """
        Based on the parameter that will be given, this function will return various results using functions
        from the battery class 
        """
        if isinstance (param, Block):
            return
        else:
            return  

    def evaluate_overall_system(self, param):
        """
        Check the overall status of the system, that means look at the different parts of the system and notice if
        there are any anomalies (such as too much sun on one part of the system, we should just have to modify 
        that area not the whole system)

        Given a certain parameter it will evaluate the status of the system and return the result for the specific
        parameter (i.e. light, or sound)
        """
        return

    def modify_status(self, param):
        """
        This function can be used to modify the behavior of the system given a certain parameter

        param: could be the amount of light received, or sound ...
        """

        # BASED ON PARAMETER GIVEN 
            # Do modify system

class Battery():
    """
    THe use of this class will be to store various different functions that will be able to analyze the battery of 
    the system, either as a whole or individual blocks
    """

    def __init__(self, battery):
        """
        Initialize the battery instance

        INPUT:
        battery: this variable can be of various types, it can be an instance of a block, or a row of the instance
        System, or a column...

        This allows for different parameters to be analyzed
        """
        self.battery = battery

    def battery_neighs(self, battery, n):
        """
        Return the battery of the neighbors of the block

        battery: instance of block
        n: integer saying how many neighbors to get
        """
        return

    def battery_l_c(self, battert, val):
        """
        Return the battery of an entire row or column

        val: parameter that defines row or column or other
        """
        return 

def main(init, obj):
    """
    Given an initial status for the system and an objective to keep, we let the system run and live by itself
    """
    return

"""
INITIAL STATE OF MODEL:

    We have a matrix of blocks  of size (Y x Z), each block is initialize to be functionning correctly (as well
    as all of it's neighbors). They all have a full charge and their lights and speakers are working at maximum
    power.

    Objective:
        We want the system to be able to run for as long as possible

    How do we achieve this:
        - Establish communication amongst the blocks
        - If one block shuts down, have a reaction from the other blocks to complement the failure

"""
