########################################################################################################
###parsing
########################################################################################################
#a =input("What is your File Name?")
#if ".txt" in a:
    #filename = a
#else:
    #filename = a + ".txt"
#print(filename)
#above ensures proper file is opened for parsing (keep as comment)
########INCLUDE ABOVE IF YOU WANT USER INPUT TO DEFINE THE FILE NAME INSTEAD OF MANUAL ENTRY

import math
import matplotlib.pyplot as plt
import numpy as np

filename = "pendulumdata_4536length1.txt"
print(filename)
###change file name on above line to analyze other data files (DELETE ABOVE LINE IF YOU WANT USER INPUT TO DEFINE FILE NAME)

list_lines = []
time = []
accX = []
accY = []
accZ = []
angle = []
#above creates lists for the individual variables
with open (filename, "r") as file:

    for line in file:

        line = line.rstrip().split(" ")

        Yacc = float(line[2])
        
        Xacc = float(line[1])

        t = int(line[0])

        accY.append(Yacc)

        time.append(t)



t = np.asarray(t)

#with open (filename, "r") as file:
 #   for line in file:
  #      time.append(int(line.split(" ")[0]))
   #     accX.append(float(line.split(" ")[1]))
    #    accY.append(float(line.split(" ")[2]))
     #   accZ.append(float(line.split(" ")[3]))
        #i = 0
        #while i <= len(accX):
         #   angle.append(math.atan(-1* accX[i] / accY[i] * 100))
          #  i = i + 1
#above splits the values in the .txt file into individual variables which are entered into arrays from lines 17-21
print("times: ",time)
print("accX: ",accX)
print("accY: ",accY)
print("accZ: ",accZ)

#plt.subplot(3,1,1)
#plt.plot(time[:-1], angle, 'ro--')

#plt.xlabel('Time (seconds)')
#plt.ylabel('Angle (rad)')
#plt.title('Angle vs Time')
#plt.xlim((0, 20))
#plt.grid()