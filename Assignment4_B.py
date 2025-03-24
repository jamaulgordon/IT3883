# Program Name: Assignment4_Program B
# Course: IT3883/W02
# Student Name: Jamaul Gordon
# Assignment Number: Assignment4
# Due Date:3/24/25
# Purpose: This program sends a message to the server and prints back the response.
# Resources Used: Just my class notes and Python socket examples.

import socket

# Setup IP and port to listen on
host = '127.0.0.1'
port = 40001

# Create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind it to IP and port
s.bind((host, port))

# Start listening
s.listen(1)
print("Waiting for a connection...")

# Accept a connection
conn, addr = s.accept()
print("Connected to", addr)

# Receive message
data = conn.recv(1024).decode()
print("Got message:", data)

# Convert to uppercase
new_msg = data.upper()

# Send it back
conn.send(new_msg.encode())

# Close everything
conn.close()