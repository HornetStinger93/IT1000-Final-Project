print( "Welcome to my ICBM Position Calculator: sponsored by the US Government")
print( "This program is made possible by the tax paying public and users like you: Thank You!")
initial_position_of_missile = float(input("Enter the missile's initial position in meters: "))
initial_velocity_of_missile = float(input("Enter the missile's initial velocity in meters per second: "))
acceleration_of_missile = float(input("Enter the missile's accleration in meters per second squared: "))
flight_time = float(input("Enter the missile's estimated total flight time in seconds: "))
Missile_Final_Position = (initial_position_of_missile + initial_velocity_of_missile * flight_time + 0.5 * acceleration_of_missile * flight_time * flight_time) 
print ("Calculating...")
import time
time.sleep (3)
print ("Calculating...")
time.sleep (7)
if initial_position_of_missile == 0 or initial_velocity_of_missile == 0 or acceleration_of_missile == 0 or flight_time == 0 :
    print ("error")
else:
    print("The Missile's Final Position is:")
    time.sleep(1)
    print(str(Missile_Final_Position) + 'm')
    time.sleep(1)
    print("Hopefully you understand what this means in relation to your current position!")
    print( "Stay safe out there!")
    time.sleep(1)
    print("Product of The United States Government ©2020")
    

Exit = input("Press ENTER to exit the program.")
