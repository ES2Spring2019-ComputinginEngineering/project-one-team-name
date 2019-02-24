#pendulum step 1

import math
import numpy as np

angle = [0]
vel = [0]
acc = [#]
length = #.25
angleNext = math.pi / 6
time = np.linspace(0,10,10)


def update_system(acc,angle,vel,time1,time2):
    dt = time2 - time1
    angleNext = #eq for angle of a pendulum #angle + vel * dt
    velNext = #eq for velocity of a pendulum #vel + acc * dt
    accNext = #(-9.81 * math.sin(angleNext)) / length
    return angleNext, velNext, accNext

def print_system(time,angle,vel,acc):
    print("TIME: ", time)
    print("ANGLE: ", angle)
    print("VELOCITY: ", vel)
    print("ACCELERATION: ", acc, "\n")


print_system(time[0],angle[0],vel[0])

i = 1
while i < len(time)-1:
    angleNext, velNext, accNext = update_system(acc[i],angle[i-1],vel[i-1],time[i-1],time[i])
    angle.append(angleNext)
    vel.append(velNext)
    acc.append(accNext)
    print_system(time[i],angle[i],vel[i],acc[i])
    i += 1