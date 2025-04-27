#Importing Libraries

import random
import time
from collections import deque


#Queues
landing_queue = deque()
takeoff_queue = deque()
emergency_landing_queue = deque()


#Landing Requests
def request_landing(flight_number):
    print(f"Flight {flight_number} requests landing")
    landing_queue.append(flight_number)




#Takeoff Requests
def request_takeoff(flight_number):
    print(f"Flight {flight_number} requests takeoff")
    takeoff_queue.append(flight_number)


#Emergency Landing
def request_emergency_landing(flight_number):
    print(f"Flight {flight_number} requests EMERGENCY landing")
    emergency_landing_queue.appendleft(flight_number)  


#Flight Control
def control():
    if emergency_landing_queue:  #Emergency landing is prioritised
        flight_number = emergency_landing_queue.popleft()
        print(f"CONTROL: {flight_number} land (EMERGENCY)")
        
    elif landing_queue:
        flight_number = landing_queue.popleft()
        print(f"CONTROL: {flight_number} land")

    elif takeoff_queue:
        flight_number = takeoff_queue.popleft()
        print(f"CONTROL: {flight_number} takeoff")

    else:
        print("CONTROL: No action (no planes waiting)")


#Stimulate the airport
def simulate_airport(steps=20, delay=0.5):
    for _ in range(steps):
        action = random.choice(["landing", "takeoff", "emergency"]) #Generate a random action
        flight_number = random.randint(100, 999) #Generate a random flight number

        if action == "landing":
            request_landing(flight_number)

        elif action == "takeoff":
            request_takeoff(flight_number)

        elif action == "emergency":
            request_emergency_landing(flight_number)


        control()

        time.sleep(delay)  #Pause for readable output

if __name__ == "__main__":
    simulate_airport()
