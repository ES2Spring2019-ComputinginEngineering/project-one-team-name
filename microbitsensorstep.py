import random as r
import microbit as m
filename = "pendulumdata_" + str(r.randint(1,9999))+".txt"

with open(filename, 'w') as my_file:
    start_time = m.running_time()
    while not m.button_b.is_pressed():
        m.sleep(100)
        accel_x = m.accelerometer.get_x()
        accel_y = m.accelerometer.get_y()
        accel_z = m.accelerometer.get_z()
        time = m.running_time() - start_time
        datafrom = str(accel_x) + " " + str(accel_y) + " " + str(accel_z) + " " + str(time)
        my_file.write(datafrom+'\n')
        m.sleep(50)
my_file.close
