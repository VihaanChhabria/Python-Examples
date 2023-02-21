# H-Drive Autonomous Test Code
# FTC-14133 : VIHAAN CHHABRIA

import math

#Uncomment 2 lines below for no user input from cmd
#distanceInput = 13 # Can be any distance
#angleInput = 45 # Can be any angle

distanceInput = input("Distance Traveling? : ") # How much the user wants to go
angleInput = input("Angle (In Degrees) Traveling? : ") # Angle of which the user wants to go

distanceFloat = float(distanceInput) #Converting distance and angle to floats
angleFloat = float(angleInput)

angleRadians = angleFloat*(math.pi/180) # Converting angle(s) to radiant(s)

strafeDistance = distanceFloat*math.cos(angleRadians) # How long the strafe motor(s) needs to travel
fbDistance = distanceFloat*math.sin(angleRadians) # How long the forward/backward motor(s) needs to travel

# Print Information

print("\nDistance Input : {}".format(distanceInput))
print("Angle Input (In Radians) : {}\n".format(angleInput))
print("Forward/Backwards Distance : {}".format(fbDistance))
print("Strafe Distance : {}\n".format(strafeDistance))