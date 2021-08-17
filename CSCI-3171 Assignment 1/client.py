# Aitzaz Qadir Khowaja – B00853169
# CSCI–3171 Assignment #1 UDP Pinger Client
# Importing time and socket.
import time
from socket import *

# Creating a UDP socket.
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Setting socket to timout after 1 sec.
clientSocket.settimeout(1.0)
print()

# Part-A Pinging the server 10 times.
# Initializing some variables for calculation.
count = 1
minRTT= 1
maxRTT= 0
totalRTT = 0
packetLost = 0
# Starting a loop which will run 10 times.
while count <= 10 :
	# Sending a ping test message to the server (formatted as asked in pdf).
	message = "Ping "+str(count)+" "+str(time.time())
	# Storing current time for later use in calculating RTT.
	initial  = time.time()
	clientSocket.sendto(message.encode(),('',12000))
	# Using a try statement to catch timeout exception.
	try:
		# Recieving response from the server.
		recieved, addr = clientSocket.recvfrom(100)
		# Calculating RTT, updating min & max RTT.
		roundTripTime = time.time() - initial
		if roundTripTime < minRTT : minRTT = roundTripTime
		if roundTripTime > maxRTT : maxRTT = roundTripTime
		# Summing up all RTTs for later use in calculating average RTT.
		totalRTT = totalRTT + roundTripTime
		print("Count is : "+str(count))
		print("Response : "+str(recieved.decode()))
		print("Round-Trip-Time is : " + str(roundTripTime) + " seconds")
	except timeout:
		# Printing error when socket times out.
		print("Count is : "+str(count))
		print("Request Timed Out.")
		# Counting packets lost for use in calculating packet loss rate.
		packetLost = packetLost + 1

	# Updating counter.
	count = count + 1
	print()

# Printing all additional information required in Part-B.
print("Minimum Round-Trip-Time was "+str(minRTT)+" seconds.")
print("Maximum Round-Trip-Time was "+str(maxRTT)+" seconds.")
print("Average Round-Trip-Time was "+str(totalRTT/10)+" seconds.")
print()
print("Packet-Loss-Rate is "+str((packetLost/10)*100)+"%")
print()
# Closing the connections.
clientSocket.close()
