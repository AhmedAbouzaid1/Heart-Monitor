# Heart-Monitor
Heart monitoring using STM32F103C8Tx and AD8232

This application provides a python UI to select the baud rate and the port number which is connected to the microcontroller and
the heart sensor. 

# For building and running the program:

clone/download the files from master branch

Run "start_ui.py"

Choose the baud rate and click "select" to save your choice
choose the port number and click "select" to save your choice

Click "Start" to open the graph viewer and dispaly the heart sensor data. 

# Dependencies: (Libraries)

import sys

import os

import serial

import pickle

import heartpy as hp

from time import sleep

import datetime as dt

import matplotlib.pyplot as plt

import matplotlib.animation as animation


