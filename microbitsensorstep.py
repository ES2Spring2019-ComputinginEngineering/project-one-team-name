import random
import microbit as m
import step 1 as stp
filename = "pendulumdata_" + str(r.randint(1,9999))+".csv"

with open(filename, 'w') as my_file:
    start_time = m.running_time()
    while not m.button_b is_pressed:
        m.sleep(200)
        accel_x = accelerometer.get_x()
        accel_y = accelerometer.get_y()
        accel_z = accelerometer.get_z()
        time = microbit.running_time() - start_time

########################################################################################################
###parsing
########################################################################################################

fin = open("whatever.txt") #whatever.txt is the file the microbit will write

list_lines = []
time = []
accX = []
accY = []
accZ = []
angle = []

for line in fin:
    time.append(int(line.split("\t")[0]))
    accX.append(int(line.split("\t")[1]))
    accY.append(int(line.split("\t")[2]))
    accZ.append(int(line.split("\t")[3]))
    angle.append(math.atan2(-1*int(line.split("\t")[1]))/ int(line.split("\t")[2]))