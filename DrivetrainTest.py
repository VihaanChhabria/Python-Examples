import math

print("Input the angle of the direction the robot should travel")
angle = float(input())
rf = (math.sin(math.radians(angle) + (1 * math.pi/4)))
lf = (math.sin(math.radians(angle) + (7 * math.pi/4)))
lb = (math.sin(math.radians(angle) + (5 * math.pi/4)))
rb = (math.sin(math.radians(angle) + (3 * math.pi/4)))
print("rf:")
print(rf)
print("lf:")
print(lf)
print("lb:")
print(lb)
print("rb:")
print(rb)

#Angle test
print(math.degrees(math.atan2(1,1))+90)
