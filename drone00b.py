from codrone_edu.drone import *

# Initialize and pair with the drone
drone = Drone()
drone.pair()

# Step 1: Takeoff
drone.takeoff()
drone.hover(2)            # Hover to stabilize at flight height

# Step 2: Fly forward
drone.set_pitch(30)      
drone.move(5)            

# Step 3: Stop & turn 180 degrees
drone.set_pitch(0)        # Reset pitch so it doesn't drift forward while turning
drone.hover(1)            # Pause to kill momentum
drone.turn_degree(180)    # Execute turn
drone.hover(1)

# Step 4: Fly back
drone.set_pitch(30)
drone.move(5)

# Step 5: Stop & turn 180 degrees
drone.set_pitch(0)
drone.hover(1)
drone.turn_right(180)
drone.hover(2)            # Must hover motionless before flipping

# Step 6: Perform the Backflip
drone.flip("back")        # Explicitly triggers a backflip
drone.hover(2)            # Recover altitude and stability


drone.turn_right(360)
drone.hover(2)

drone.flip("left")
drone.hover(2)
# Step 7: Land cleanly
drone.land()             
drone.close()