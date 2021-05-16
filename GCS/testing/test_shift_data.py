
import numpy as np

data = np.arange(10).astype(float)
data = np.array([0,0,0,0,0])

def update_data(num):
    global data
    data[:-1] = data[1:]
    data[-1] = num

print(data)
update_data(4)
print(data)
update_data(4)
print(data)

"""
list of data arrays:
containervoltagedata
containertempdata
containeraltitudedata
p1tempdata
p1altitudedata
p1rpmdata
p2tempdata
p2altitudedata
p2rpmdata
"""