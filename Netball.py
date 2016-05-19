# Name: Netball.py
# Description: Output the names + avg scores of netball players in alphabetic order. Then suggest the top 3 scorers.

# Functions Definitions --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def hasNumbers(inputString): # Checks if a string has any numbers in it
    return any(char.isdigit() for char in inputString)

def GetPlayer(): # Get player in own function as input checking will be
                # performed before getting information about the player.
    ValidPlayer = ""
    while True:
        try:
            print("")
            print("Please enter First Name and " + str(NumScores) + " goal scores (" + str(MinScore) + " to " + str(MaxScore) + ")")
            IsValid = True
            numPlayers = len(Players) + 1
            _input = input("Player " + str(numPlayers) + ": ") # Display the current number of valid players so the user can keep track

            if _input.lower() == "q": # The user wants to quit, no need to validate just stop here.
                ValidPlayer = "Quit"
                break
            if _input == "": # If the user enters nothing, handle it
                print("Error: Input should be in the form of Name then " + str(NumScores) + " goal scores")
                raise Warning()
    
            _player = _input.split()
            _scores = [] + _player
            _scores.pop(0)
            _name = _player[0]

             
            if len(_player) != (NumScores + 1): # If the user has not entered a Name + NumScores of Scores, handle it
                print("Error: You must enter a players First Name then " + str(NumScores) + " goal scores (" + str(MinScore) + " to " + str(MaxScore) + ")")
                raise Warning()
            
            for i in _scores:
                
                if not i.isdigit(): # If the user has entered a score that contains a character, handle it
                    print("Error: You must only enter integers for scores")
                    raise Warning()
                
                if (int(i) < MinScore) or (int(i) > MaxScore): # If the user has entered a goal score outside the allowed range, tell them.
                    print("Error: You must only enter scores from MinScore to MaxScore")
                    raise Warning()
            
            if hasNumbers(_name):
                print("Error: The players name cannot contain numbers")
                raise Warning()

            # If the program has reached this point, It means that the entered player + scores is certainly valid,
            # therefore break out of while loop and return the ValidPlayer
            ValidPlayer = _player
            break
        
        except Warning:
            print("For example: Emma 3 6 17 9 20")
            
    return ValidPlayer

def AveragePlayer(player): # Average player in own function as finding the average
                           # of the player's scores will be done many times.
    _name = player[0]
    player.pop(0)
    _scores = player
    
    _total = 0
    _average = 0
    
    for iScore in _scores:
        _total = _total + int(iScore) 

    if _total != 0:
        _average = _total/NumScores # We know that we have received a valid player, therefore divide by NumScores there should be rather than find how long the scores list is for this player.
    
    return [_name] + [_average]

# Main -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NumScores = 5 # Variable to allow configuration of program
MinScore = 0 # Variable to allow configuration of program
MaxScore = 50 # Variable to allow configuration of program

Players = list() # This list will contain all valid players

# Instruct the user how to use the program
print("Instructions: Please enter each individual Netball players First Name and all Goal Scores separated by Spaces\n")
print("An example input is as follows")
print("Example: Emma 3 6 17 9 20")
print("When you are finished, enter Q and press enter")

while True:
    thePlayer = GetPlayer()
    if thePlayer == "Quit": # If the user has chosen to quit, end the while loop and output the averages and suggestions.
        break

    averagedPlayer = AveragePlayer(thePlayer)
    Players.append(averagedPlayer)

print("\nAll Players names and their average scores: \n")
Players.sort()
for player in Players:
    print(player[0] + " has an average of " + str(player[1]))

print("\nSuggest any of these for Goal Shoot and Goal Attack\n")
Players = sorted(Players, key = lambda item: item[1], reverse = True)

for i in range (3):
    try:
        print(str(i+1) + " " + Players[i][0] + " with an average of " + str(Players[i][1]))
    except IndexError:
        print("Only " + str(len(Players)) + " players were entered.")
        # If an IndexError occurs, it means that the user has not entered at least 3 players.
        # This is okay so the exception can be ignored.

# Due to the nature of the program it is likely the program will be used once at a time.
# Therefore the program simply exits.
# End --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
