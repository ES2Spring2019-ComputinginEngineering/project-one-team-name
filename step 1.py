#pendulum step 1

import math
import numpy as np

def update_system(acc,pos,vel,time1,time2):
    dt = time2-time1
    posNext = #eq for position of a pendulum
    velNext = #eq for velocity of a pendulum
    return posNext, velNext

def print_system(time,pos,vel):
    print("TIME: ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel, "\n")

pos = [0]
vel [0]
acc = #initial conditions of acceleration for a pendulum
time = np.linspace#()
print_system(time[0],pos[0],vel[0])

i = 1
while i < len(time):
    posNext, velNext = update_system(acc[i],pos[i-1],vel[i-1],time[i]) #not sure if this line is right
    pos.append(posNext)
    vel.append(velNext)
    print_system(time[i],pos[i],vel[i])
    i += 1