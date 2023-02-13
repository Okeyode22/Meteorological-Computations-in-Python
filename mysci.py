# Initialize data variable
data = []

# Read the data file
filename = "data/wxobs20170821.txt"

with open(filename,'r') as datafile:
    for _ in range(3):
        datafile.readline()
        print(_)
    for line in datafile:
        datum = line.split()
        data.append(datum)

