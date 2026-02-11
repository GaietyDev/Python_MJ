from math import sin
from math import radians

initial_angle = 0
target_distance_meters = 0
distance_traveled_meters = 0.0
speed = 1
gravity_meters = 9.8

while True:
    initial_angle = int(input("Enter the initial angle(1-89 degrees): "))
    print()
    
    if initial_angle <= 0:
        print("|! INITIAL ANGLE NEEDS TO BE MORE THAN 0 !|")
    elif initial_angle >= 90:
        print("|! INITIAL ANGLE CAN'T BE MORE THAN 89 !|")
    else:
        break
# End of Loop

while True:
    target_distance_meters = int(input("Enter the target distance(meters): "))
    print()

    if target_distance_meters <= 0:
        print("|! DISTANCE NEEDS TO BE MORE THAN 0 !|")
    else:
        break
# End of Loop

while True:
    distance_traveled_meters = (speed * speed) * sin(2 * radians(initial_angle))/gravity_meters
    
    if (target_distance_meters - 0.5) <= distance_traveled_meters <= (target_distance_meters + 0.5):
        print("The speed needed to land within 0.5 meters of the target is %.1f m/s" % (speed))
        break
    else:
        speed += 0.1
