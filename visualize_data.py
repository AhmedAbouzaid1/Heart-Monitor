import string
import sys
import os
import serial
import pickle
import heartpy as hp
from time import sleep
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading

arr = []

# def printit():
#   threading.Timer(5.0, printit).start()
#   global arr
#   with open('data.txt', 'w') as outfile:
#       outfile.write("\n".join(arr))
#
# printit()

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
ser = serial.Serial()
ser.port = 'COM8'
ser.baudrate = 9600
# ser.port = sys.argv[1]
# ser.baudrate = sys.argv[2]
ser.bytesize = serial.EIGHTBITS
ser.partiy = serial.PARITY_NONE
ser.timeout = 2
ser.open()
count = 0

def get_read():
    a = ''
    while(1):
        read_str = ser.read().decode("utf-8")
        if(read_str == '\r'):
            filter_str = filter(str.isdigit, a)
            str_converted = "".join(filter_str)
            return int(str_converted)

        elif (len(read_str) == 1):
             a = (str(a) + str(read_str))



def animate(i, xs, ys):
    global count
    read = get_read()
    arr.append(read)
    count = count + 1


    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(read)

    # Limit x and y lists to 20 items
    xs = xs[-50:]
    ys = ys[-50:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Heart Monitor')
    plt.ylabel('Heart sensor data')

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1)

plt.show()