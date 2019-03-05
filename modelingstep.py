#pendulum step 1

import math
import numpy as np

vel = [0] #this section assigns some variables that will be used later
acc = [0]
length = 1
angleNext = math.pi / 6
angle = [angleNext]
time = np.linspace(0,10,10000) #declares the timesteps used in data plotting
#anglNext = 0
#velNext = 0
#accNext = 0


def update_system(acc,angle,vel,time1,time2):
    dt = time2 - time1
    angleNext = angle + vel * dt
    velNext = vel + acc * dt
    accNext = 9.81 * (math.pi/2 - angleNext) / length
    return angleNext, velNext, accNext #above formulas manipulate variables to create new, useful variables

def print_system(time,angle,vel,acc):
    print("TIME: ", time)
    print("ANGLE: ", angle)
    print("VELOCITY: ", vel)
    print("ACCELERATION: ", acc, "\n") #this section prints the useful variables



i = 1 #the following section appends the variables per time step
while i < len(time)-1:
    angleNext, velNext, accNext = update_system(acc[i-1],angle[i-1],vel[i-1],time[i-1],time[i])
    angle.append(angleNext)
    vel.append(velNext)
    acc.append(accNext)
    if i % 100 == 0:
        print_system(time[i],angle[i],vel[i],acc[i])
    i += 1

print_system(time[0],angle[0],vel[0],acc[0])

#everything below plots the data into graphs

import matplotlib.pyplot as plt
import numpy as np

plt.subplot(3,1,1)
plt.plot(time[:-1], angle, 'ro--')

plt.xlabel('Time (seconds)')
plt.ylabel('Angle (rad)')
plt.title('Angle vs Time')
plt.xlim((0, 20))
plt.grid()


plt.subplot(3,1,2)
plt.plot(time[:-1], vel, 'ro--')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Time')
plt.xlim((0, 20))
plt.grid()


plt.subplot(3,1,3)
plt.plot(time[:-1], acc, 'ro--')
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration vs Time')
plt.xlim((0, 20))
plt.grid()
plt.tight_layout()
plt.show()