########################################################################################################
###parsing
########################################################################################################
a =input("What is your File Name?")
if ".txt" in a:
    filename = a
else:
    filename = a + ".txt"
print(filename) #above ensures proper file is opened for parsing

fin = open(filename)

list_lines = []
time = []
accX = []
accY = []
accZ = []
angle = []
#above creates lists for the individual variables
for line in fin:
    time.append(int(line.split("\t")[0]))
    accX.append(int(line.split("\t")[1]))
    accY.append(int(line.split("\t")[2]))
    accZ.append(int(line.split("\t")[3]))
    angle.append(math.atan2(-1*int(line.split("\t")[1]))/ int(line.split("\t")[2]))