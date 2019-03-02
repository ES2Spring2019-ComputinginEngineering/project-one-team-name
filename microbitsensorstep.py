import random
import microbit as m
filename = "pendulumdata_" + str(r.randint(1,9999))+".csv"

with open(filename, 'w') as my_file:
    start_time = m.running_time()
    while not m.button_b is_pressed:
        m.sleep(200)
        accel_x = accelerometer.get_x()
        accel_y = accelerometer.get_y()
        accel_z = accelerometer.get_z()
        time = microbit.running_time() - start_time