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