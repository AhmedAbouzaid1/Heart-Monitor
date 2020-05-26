from tkinter import *
from tkinter.ttk import *
import sys
import os

def clicked():
  os.system('"python visualize_data.py" %s %s' % (port_chosen, rate_chosen))

window = Tk()
window.title("Heart Monitor Project")
window.geometry('500x500')

lbl = Label(window, text="Select the Port Number")
lbl.grid(column=0, row=0)

port = Combobox(window)
port['values']= ('COM6', 'COM7', 'COM8')
port.grid(column=0, row=2)
port.current(1) #set the selected item
port_chosen = port.get()
print(port_chosen)


lbl = Label(window, text="Select the Baudrate")
lbl.grid(column=4, row=0)

rate = Combobox(window)
rate['values']= (110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 38400, 57600, 115200, 230400, 460800, 921600)
rate.current(1) #set the selected item
rate.grid(column=4, row=2)
rate_chosen = rate.get()

btn = Button(window, text="Start", command=clicked)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
window.mainloop()




