import random
import microbit as m
import step 1 as stp
filename = "pendulumdata_" + str(r.randint(1,9999))+".txt"

with open(filename, 'w') as my_file:
    start_time = m.running_time()
    while not m.button_b.is_pressed():
        m.sleep(100)
        accel_x = accelerometer.get_x()
        accel_y = accelerometer.get_y()
        accel_z = accelerometer.get_z()
        time = microbit.running_time() - start_time
        my_file.write()
