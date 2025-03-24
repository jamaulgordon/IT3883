# Program Name: Assignment4_Program A
# Course: IT3883/W02
# Student Name: Jamaul Gordon
# Assignment Number: Assignment4
# Due Date:3/24/25
# Purpose: This program sends a message to the server and prints back the response.
# Resources Used: Just my class notes and Python socket examples.

import socket

# Set up the server details
server_ip = '127.0.0.1'  # Local machine
port = 40001             # Random unused port

# Create a socket to connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, port))

# Ask the user to type something
msg = input("Type something to send: ")

# Send the message
s.send(msg.encode())

# Wait for reply from server
reply = s.recv(1024)

# Show what the server sent back
print("Server replied:", reply.decode())

# Done
s.close()
