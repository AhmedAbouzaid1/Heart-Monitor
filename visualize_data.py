import string
import sys
import os
import serial
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
ser = serial.Serial()
print(sys.argv[1])
ser.port = 'COM8'
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS
ser.partiy = serial.PARITY_NONE
ser.timeout = 2
ser.open()
count = 1
def get_read():
    return ser.read(size=3)

def animate(i, xs, ys):

    read = get_read()
    read_str = read.decode("utf-8")
    #print(read_str)

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(read_str)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Heart Monitor')
    plt.ylabel('Heart sensor data')
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=300)

plt.show()