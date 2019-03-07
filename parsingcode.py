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

import scipy.signal as sig



filename = "pendulumdata_4536length.24.txt"

print(filename)

fin = open(filename)

###change file name on above line to analyze other data files (DELETE ABOVE LINE IF YOU WANT USER INPUT TO DEFINE FILE NAME)



list_lines = []

t = []

accX = []

accY = []

accZ = []

theta = []

g = 9.8

#above creates lists for the individual variables

for line in fin:

    t.append(float(line.split(",")[0]))

    accX.append(int(line.split(",")[1]))
    
    accY.append(int(line.split(",")[2]))

    accZ.append(int(line.split(",")[3].strip()))

    theta.append(math.atan2(-1*int(line.split(",")[1]),int(line.split(",")[2])))



t = np.asarray(t)

theta = np.asarray(theta)

#above splits the values in the .txt file into individual variables which are entered into arrays/lists from lines 17-21

print("times: ",t)

print("accX: ",accX)

print("accY: ",accY)

print("accZ: ",accZ)

###above is just to check that values are OK at this step



t = np.asarray(t)/1000 

#above converts the list to np.array



y_noisy_filt = sig.medfilt(theta,9)

y_noisy_filt_pks, _ = sig.find_peaks(y_noisy_filt)

#above applies filters



#theta = np.arcsin(y_noisy_filt / g)

#theta_peaks, _ = sig.find_peaks(theta)

#above calculates theta from accY







plt.figure()

plt.plot(t, y_noisy_filt,'g-', t[y_noisy_filt_pks], y_noisy_filt[y_noisy_filt_pks], 'b.')

plt.xlabel('Time (seconds)')

plt.ylabel('Y Acceleration (m/s^2)')

plt.title('Y Acceleration vs Time Filtered')

plt.grid()

plt.show()

#above chunk is for plotting accY v.s. time







plt.figure()

plt.plot(t, theta,'b-', t[y_noisy_filt_pks], theta[y_noisy_filt_pks], 'g.')

plt.title('Noisy Median Filtered')

plt.xlabel('Time (seconds)')

plt.ylabel('Theta(radians)')

plt.title('Theta vs Time Filtered')

plt.grid()

plt.show()

#above chunk plots angle v.s. time





peaks = t[y_noisy_filt_pks]

time_difference = np.diff(peaks)

period = str(np.sum(time_difference)/len(time_difference))

print("Period: " + period + "seconds")

#above chunk plots period by averaging time between peaks







#Note: Input numbers here to graph in the plot

#Length_of_Pendulum= [0.18,0.24,0.40,0.42,0.48] 

#Period_of_Pendulum= [,,,,]





#plt.plot(Length_of_Pendulum, Period_of_Pendulum)

#plt.xlabel('Log(Pendulum Length)')

#plt.ylabel('Log(Pendulum Period)')

#plt.yscale('log')

#plt.xscale('log')

#plt.title('Pendulum Length and Period') #Note: change title as needed

#plt.grid(True)