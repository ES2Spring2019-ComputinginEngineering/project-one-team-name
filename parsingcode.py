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

filename = "pendulumdata_4536length.24.txt"
print(filename)
###change file name on above line to analyze other data files (DELETE ABOVE LINE IF YOU WANT USER INPUT TO DEFINE FILE NAME)

list_lines = []
t = []
accX = []
accY = []
accZ = []
angle = []
g = 9.8
#above creates lists for the individual variables
with open (filename, "r") as file:

    for line in file:
        
        line.split(" ")
        
        Zacc = float(line[3])

        Yacc = float(line[2])
        
        Xacc = float(line[1])

        time = int(line[0])

        accY.append(Yacc)
        
        accX.append(Xacc)
        
        accZ.append(Zacc)

        t.append(time)



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
print("times: ",t)
print("accX: ",accX)
print("accY: ",accY)
print("accZ: ",accZ)


t = np.asarray(t)



y_noisy_filt = sig.medfilt(accY)

y_noisy_filt_pks, _ = sig.find_peaks(y_noisy_filt)



theta = np.arcsin(y_noisy_filt / g)



plt.subplot(2, 1, 1)

plt.plot(t, y_noisy_filt,'g-', t[y_noisy_filt_pks], y_noisy_filt[y_noisy_filt_pks], 'b.')

plt.xlabel('Time (seconds)')

plt.ylabel('Y Acceleration (m/s^2)')

plt.title('Y Acceleration vs Time Filtered')

plt.grid()



plt.subplot(2, 1, 2)

plt.plot(t, theta,'b-', t[y_noisy_filt_pks], theta[y_noisy_filt_pks], 'g.')

plt.title('Noisy Median Filtered')

plt.xlabel('Time (seconds)')

plt.ylabel('Theta(radians)')

plt.title('Theta vs Time Filtered')

plt.grid()



plt.tight_layout()

plt.show()



peaks = t[y_noisy_filt_pks]

time_difference = np.diff(peaks)

period = str(np.sum(time_difference)/len(time_difference))

print("Period: " + period + "seconds")