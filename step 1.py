#pendulum step 1

import math
import numpy as np

vel = [0]
acc = [0]
length = 1
angleNext = math.pi / 6
angle = [angleNext]
time = np.linspace(0,10,10000)
#anglNext = 0
#velNext = 0
#accNext = 0


def update_system(acc,angle,vel,time1,time2):
    dt = time2 - time1
    angleNext = angle + vel * dt
    velNext = vel + acc * dt
    accNext = 9.81 * (math.pi/2 - angleNext) / length
    return angleNext, velNext, accNext

def print_system(time,angle,vel,acc):
    print("TIME: ", time)
    print("ANGLE: ", angle)
    print("VELOCITY: ", vel)
    print("ACCELERATION: ", acc, "\n")



i = 1
while i < len(time)-1:
    angleNext, velNext, accNext = update_system(acc[i-1],angle[i-1],vel[i-1],time[i-1],time[i])
    angle.append(angleNext)
    vel.append(velNext)
    acc.append(accNext)
    if i % 100 == 0:
        print_system(time[i],angle[i],vel[i],acc[i])
    i += 1

print_system(time[0],angle[0],vel[0],acc[0])