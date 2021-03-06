import random as r
import microbit as m
filename = "pendulumdata_" + str(r.randint(1,9999))+"length5.txt" #sets file name that microbit will write data onto

with open(filename, 'w') as my_file:
    start_time = m.running_time()
    while not m.button_b.is_pressed(): #following lines gather microbit data
        m.sleep(100)
        accX = m.accelerometer.get_x()
        accY = m.accelerometer.get_y()
        accZ = m.accelerometer.get_z()
        time = m.running_time() - start_time
        datafrom = str(time) + "," + str(accX) + "," + str(accY) + "," + str(accZ)
        my_file.write(datafrom+' \n') #writes microbit data onto a txt file
        m.sleep(50)
my_file.close