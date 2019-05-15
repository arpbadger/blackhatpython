# tcpclient-badger-gui
# developed by arpbadger with assistance from Justic Seitz, "Black Hat Python"

# The GUI version of tcpclient-badger
from Tkinter import *
import socket


target_host = ""
target_port = 0

# Pring title page
def title_sequence():

	print ('''
     __     _                      _        ___           _
  /\ \ \___| |___      _____  _ __| | __   / __\ __ _  __| | __ _  ___ _ __
 /  \/ / _ \ __\ \ /\ / / _ \| '__| |/ /  /__\/// _` |/ _` |/ _` |/ _ \ '__|
/ /\  /  __/ |_ \ V  V / (_) | |  |   <  / \/  \ (_| | (_| | (_| |  __/ |
\_\ \/ \___|\__| \_/\_/ \___/|_|  |_|\_\ \_____/\__,_|\__,_|\__, |\___|_|
                                                            |___/
                                             ''')
	return

# get domain or targer IP and port from the user
def add_target():
    global target_host
    target_host = e.get()

def add_port():
    global target_port
    target_port = e1.get()
    target_port = int(target_port)

def get_target():
	return target_host,target_port

# Request http connection
def connect(target_host,target_port):

	#edit target_host variable. I.E cut of www
	ftarget_host = target_host[2:]

	#create a socket object
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#connect the client
	client.connect((target_host,target_port))

	#send some data
	client.send("GET / HTTP/1.1\r\nHost: "+ftarget_host+"\r\n\r\n")

	#receive some data
	response = client.recv(4096)

	print response

# Main sequence
def main():
	title_sequence()
	get_target()
	connect(target_host,target_port)

# Create GUI Interface
root = Tk()

root.title('TCPClient Badger')

# Create target entry feild
e = Entry(root)
e.pack()
e.focus_set()

# Create 'add target' button
b = Button(root,text='Add target',command = add_target)
b.pack()

# Create port entry feild
e1 = Entry(root)
e1.pack()
e1.focus_set()

# Create 'add port' button
c = Button(root,text='Add Port', command = add_port)
c.pack()

d = Button(root,text='Run Badger', command = main)
d.pack(side='bottom')

# run gui interface
root.mainloop()
