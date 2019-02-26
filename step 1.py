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

import matplotlib.pyplot as plt
import numpy as np

# regular python lists
x_list = [1, 2, 3, 4, 5] 
y_list = [1, 4, 9, 16, 25]

print('Indexing in Python List:', x_list[1])

# convert to numpy arrays
x_numpy = np.array(x_list)
y_numpy = np.array(y_list)


print('Indexing in Numpy Array:', x_numpy[1])

# Adding Python Lists
z_list = [] 
for i in range(0, len(x_list)):
  z_list.append(x_list[i] + y_list[i])
  
print('Adding in Python List:', z_list)

# Adding Numpy Arrays
z_numpy = x_numpy + y_numpy
# Multiplication 
y2_numpy = 2 * x_numpy

print('Adding in Numpy Array:', z_numpy)

plt.figure(1)
plt.plot(x_numpy, y_numpy, 'ro--', x_numpy, y2_numpy, 'kd-.') 
#Y is red dashed line with circles
#Y2 is black dot-dash line with diamonds
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Y vs X')
plt.legend(('Y', 'Y2'))
plt.xlim((-1, 8)) # set x range to -1 to 8
plt.grid()
plt.show()