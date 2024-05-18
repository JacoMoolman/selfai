# Setup variables and client
first_requirement = """
Please write a script to train an ML model in Python. This can use any model you think is best for the task. 

There is files in E:\\Projects\\SELFAI\\KagglespaceTitanic (this is windows to you need the //)
They are:
test.csv and train.csv

=====
In this competition your task is to predict whether a passenger was transported to an alternate dimension during the Spaceship Titanic's collision with the spacetime anomaly. To help you make these predictions, you're given a set of personal records recovered from the ship's damaged computer system.

File and Data Field Descriptions
train.csv - Personal records for about two-thirds (~8700) of the passengers, to be used as training data.
PassengerId - A unique Id for each passenger. Each Id takes the form gggg_pp where gggg indicates a group the passenger is travelling with and pp is their number within the group. People in a group are often family members, but not always.
HomePlanet - The planet the passenger departed from, typically their planet of permanent residence.
CryoSleep - Indicates whether the passenger elected to be put into suspended animation for the duration of the voyage. Passengers in cryosleep are confined to their cabins.
Cabin - The cabin number where the passenger is staying. Takes the form deck/num/side, where side can be either P for Port or S for Starboard.
Destination - The planet the passenger will be debarking to.
Age - The age of the passenger.
VIP - Whether the passenger has paid for special VIP service during the voyage.
RoomService, FoodCourt, ShoppingMall, Spa, VRDeck - Amount the passenger has billed at each of the Spaceship Titanic's many luxury amenities.
Name - The first and last names of the passenger.
Transported - Whether the passenger was transported to another dimension. This is the target, the column you are trying to predict.
test.csv - Personal records for the remaining one-third (~4300) of the passengers, to be used as test data. Your task is to predict the value of Transported for the passengers in this set.
space_submission.csv - A submission file in the correct format.
PassengerId - Id for each passenger in the test set.
Transported - The target. For each passenger, predict either True or False.

===

Sample of the test file is:
PassengerId,HomePlanet,CryoSleep,Cabin,Destination,Age,VIP,RoomService,FoodCourt,ShoppingMall,Spa,VRDeck,Name
0013_01,Earth,True,G/3/S,TRAPPIST-1e,27.0,False,0.0,0.0,0.0,0.0,0.0,Nelly Carsoning
0018_01,Earth,False,F/4/S,TRAPPIST-1e,19.0,False,0.0,9.0,0.0,2823.0,0.0,Lerome Peckers
0019_01,Europa,True,C/0/S,55 Cancri e,31.0,False,0.0,0.0,0.0,0.0,0.0,Sabih Unhearfus

Sample of the train file is:
PassengerId,HomePlanet,CryoSleep,Cabin,Destination,Age,VIP,RoomService,FoodCourt,ShoppingMall,Spa,VRDeck,Name,Transported
0001_01,Europa,False,B/0/P,TRAPPIST-1e,39.0,False,0.0,0.0,0.0,0.0,0.0,Maham Ofracculy,False
0002_01,Earth,False,F/0/S,TRAPPIST-1e,24.0,False,109.0,9.0,25.0,549.0,44.0,Juanna Vines,True
0003_01,Europa,False,A/0/S,TRAPPIST-1e,58.0,True,43.0,3576.0,0.0,6715.0,49.0,Altark Susent,False

I want the script to produce a file in the same location as the train and test files with the output of the ML model
The output file must be called space_sub.csv and MUST have the following layout as example below:
PassengerId,Transported
0013_01,False
0018_01,False
"""

outcome = """
Outcome:
On the screen the F1 score of the model must be printed in the following manner:
F1 SCORE :XXX Indicating how good the model has performed. 
"""

first_instructions = """
Instructions:
I want you to return the following in the following manner:
1. A paragraph of your reasoning. As in why did generate the code that you did, and if it's to fix an error what changed you made to fix the error
2. The actual python code
2.1 This must be encapsulated in three X'es (X) as in XXX before the start of the script and 
    at the end of the script.
    This part of your output will be extracted and run and must be pure python code. NOTHING ELSE
3. DO NOT add "```" (tripple qutoes) anywhere!!!!
4. Remember you are returning CODE, so the indentations must also be correct!
"""

def get_input_text():
    return(first_requirement,outcome,first_instructions)