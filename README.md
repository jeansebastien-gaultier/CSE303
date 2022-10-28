# CSE303_Project
Aggregate measures for control and coordination of IoT systems


**The main goal of this project is to propose specification mechanisms for the coordination and control based on aggregate measures, such as the percentage of entities in a given state, e.g. if less than 75% of system blocks have enough charge to emit light for 5 minutes, then 20% of these blocks shall switch off their speakers (thus allowing these blocks to continue emitting light for a longer period).**


*Goal:*  

Create specific mechanisms for the coordination and control based on aggregate 		measures of Internet of Things Systems 

 

Important terms to understand: 

Coordination: The idea of planning together to reach solutions 

Control: 

R. Scattolini, “Architectures for distributed and hierarchical model predictive control — a review”, in Journal of process control, 19(5), 723-731, 2009. [PDF] 

Model Predictive Control: Different type of algorithms implemented to manage systems. (Idea: run a prediction of the program, to see in the “future” what the system will look like and try then make decisions on how to continue running the system) 

Types of Hierarchy in systems: 

Aggregate measures: 

J. Beal, D. Pianini and M. Viroli, “Aggregate Programming for the Internet of Things,” in Computer, vol. 48, no. 9, pp. 22-30, Sept. 2015, DOI: 10.1109/MC.2015.261. [PDF] 

 

 

Internet of Things:  

https://www.zdnet.com/article/what-is-the-internet-of-things-everything-you-need-to-know-about-the-iot-right-now/ 

Physical devices connected amongst each other through the bias of the internet (ex: smart homes). They enable us to control them from afar. 

 

Objective: 

	Write a report explaining the different specifications that can be implemented to help with the control and coordination of IoT systems. Explain the thought process, how we reached these ideas and show how they work. (Use the example of the mini system to then move forward) 

 

Research Plan: 

	The idea is to find specific mechanisms to help with the control and coordination of Internet of Things systems.  

	First, we build a smaller model, to understand what we are looking for and understand how systems work. 

	Then take all these ideas and transfer them to bigger applications (IoT). 

 

Miniature (Test) Model: (Light and Sound Emitting blocks) 

	Base Question: “if less than 75% of system blocks have enough charge to emit light for 5 minutes, then 20% of these blocks shall switch off their speakers” 

	Implementations: 

Naïve: All the blocks run independently, we check the battery percentage of each and if a certain amount does not have the correct right percentage, we shut off the speakers. 

Benefit:  It works the speakers turn off, and battery is saved 

Limitations: Each block has no intel on what the other blocks are up to, we want to find a way to link these blocks together 

 

System: The idea now is to have all the blocks running on one system; hence all the blocks are connected amongst each other, and we can run global functions that will give us information about the global system and not just the individual blocks 

Benefit: We now have minimal working coordination 

Limitations: We are missing the control aspect of the system. The system has no real use, it just runs without having any understanding of what to do it just follows basic rules of implementation 

Additional Question: Do we want to shut off the completely the speaker or do we just want to reduce? Does the system evolve based on the environment it is in (if its dark outside or day...)? What happens if a block is out of service and completely shuts down? 

  

Current SYSTEM: 

What we have tried to implement: 

Blocks: 

Associate the battery percentage to how much light/sound is actually emitted (each “x lux” consumes “y battery %”) 

Node system (have each block associated to it’s neighbor) 

System: 

Additional functions are added to have a better global understanding of the system (battery percentage of the rows...) 

Add additional parameters to each function (this will help with the control of the model) 

What we want to implement: 

Potentially have a way to visualize the functioning of the system (python packages, matplotlib...) 

Have an attempt at aggregate programming, hence that would mean more communication amongst the blocks. 

 

NECESSARY: 

Correctly define the model. Make sure we understand what we are looking for, what the goal is, how do we reach said goal... 

 

CURRENT MODEL DEFINITION:  

 

Regulator: The addition of the regulator would then enable us to start working with the idea of MPC 

LATER IMPLEMENTATION 

Try to run the regulator using a “Digital Twins” ALGORITHM: 

https://dl.acm.org/doi/abs/10.1145/2968456.2974007 

 

 

 

IMPORTANT TO UNDERSTAND: 

The concept of “battery” of the blocks, or “speakers” or “light” is just a concept that is not the important aspect of the project (it helps for understanding but not the main point) 

Questions we have to ask ourselves: 

  What is the result that is expected from the system? 

  How do we reach said goal? 

  Modify whole system? 

  Change some elements of system? 

 

Overall Summary: 

	Following the overview of the two research papers on aggregate programming and hierarchical models, we started working on our own implementation of a miniature system to better understand how systems work and then be able to convert our miniature test into a more generalized version. We understand that the important part is not the individual elements of the system but more generally understanding the system as a whole, and then going into the details of how the smaller elements of the system can be taken care of. WE must go from the bigger picture to then focus on the smaller details. 

	 

 

 ### Summary Meeting (20/10):
 
 - Implementation is a good idea, but making the implementation too complex is not the objective of the project
 - Understanding how the implementation works is important, it gives a solid base for the rest of the project
 
 - Now work on more of a research aspect of the question we want to answer
 - Take everything in a more abstract manner (example of units for sound and light for BBlocks)
 - Focus on trying to understand how the blocks communicate amongst each other and see how the status of one in relevance to the other affects the system
 - Try to use graphs to visualize the communication of of the graphs amongst each other
 - CONCLUSION: specify how the data for each block is collected to then understand how this data can be shared amongst the blocks (work on the idea that we have a whole system composed of multiple blocks, so we can have look at certain neighborhoods rather than whole systems)
 
 IDEAS:
  - Focus on BBlocks and their neighborhoods (try to have a 3D) graph where we can study for example the one central node and we see how powerful the emission of light is around that block. (If we have one side of the graph with too much light emitted, maybe turn some off and emit more light on the other side).
  
  ### Summary Meeting (28/10):
  
  - Idea of visualization graph was not a bad idea, but a misunderstanding of graphs, put it aside for now, not the most important aspect (STAR WARS: *insert quote)
  
  - Better plan COMMUNICATION/CONNECTIVITY GRAPHS (little balls associated in space)
 
 FUTURE WORK:
 - Get the idea of how the systems are connected in space amongst each other
 - LOok at Graph Query Language to have an idea on how to have communication and control of the system
 - Associate it to IOT (make the project global, BBlocks is a good start but small applications)
 - With the query ideas many possibilities:
 	- info => path 
	- path => info
	- the notion of priority of one parameter over another
