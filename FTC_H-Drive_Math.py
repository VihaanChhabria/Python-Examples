# H-Drive Autonomous Test Code
# FTC-14133 : VIHAAN CHHABRIA

import math

countsperrev = 28; # Counts per rev of the motor
wheelD = 96.0/25.4; # Diameter of the wheel (in inches)
gearratio = (76.0/21.0)*(68.0/13.0); # Ratio of the entire drivetrain from the motor to the wheel
countsperin = countsperrev*(gearratio)*(1/(math.pi*wheelD)) # Counts per Inch

#Uncomment 3 lines below for no user input from cmd
#distanceInput = 13 # Can be any distance
#angleInput = 45 # Can be any angle
#powerInput = 1

distanceInput = input("Distance Traveling (In Inches)? : ") # How much the user wants to go
angleInput = input("Angle (In Degrees) Traveling? : ") # Angle of which the user wants to go
powerInput = input("Power (-1 <= power => 1) : ")

distanceFloat = float(distanceInput) #Converting distance and angle to floats
angleFloat = float(angleInput)
powerFloat = float(powerInput)

angleRadians = angleFloat*(math.pi/180) # Converting angle(s) to radiant(s)

strafeDistance = distanceFloat*math.cos(angleRadians) # How long the strafe motor(s) needs to travel
fbDistance = distanceFloat*math.sin(angleRadians) # How long the forward/backward motor(s) needs to travel

# Converting the distance (in inches) to counts for the motors
fbCountsDistance = fbDistance*countsperin
strafeCountDistance = strafeDistance*countsperin

# Power Distribution

if strafeDistance > fbDistance:
    strafePower = (powerFloat)/(strafeDistance/fbDistance) # Allows the distance to be stretched along the whole time compared with the other motor(s)
    fbPower = powerFloat # Full Power
else:
    fbPower = (powerFloat)/(fbDistance/strafeDistance) # Allows the distance to be stretched along the whole time compared with the other motor(s)
    strafePower = powerFloat # Full Power

# Print Information

print("\nPower Input : {}".format(powerInput))
print("Distance Input : {}".format(distanceInput))
print("Angle Input (In Radians) : {}\n".format(angleInput))


print("Forward/Backwards Distance (In Inches) : {}".format(fbDistance))
print("Forward/Backwards Distance (In Counts) : {}".format(fbCountsDistance))

print("Strafe Distance (In Inches) : {}\n".format(strafeDistance))
print("Strafe Distance (In Counts) : {}\n".format(strafeCountDistance))


print("Forward/Backwards Power : {}".format(fbPower))
print("Strafe Power : {}".format(strafePower))