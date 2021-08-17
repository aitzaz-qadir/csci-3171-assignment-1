# CSCI–3171 Assignment #1

- Name   : Aitzaz Qadir Khowaja
- Dal-ID : B00–853169
- E-mail : at382154@dal.ca / aitzazqadir@dal.ca

# Description :

I chose to do 'Option-2' with the 'Python' programming language. I wrote my program
to be the client-side of the provided code. First I imported the socket and time to 
setup a time-out after 1 second. For Part-A the program was a simple loop which would
ping the server 10 times and print out the sequence no. and response of the server. I
used a try statement to catch the timeout exception and return an error. At first I 
used socket.timeout but I realised that timeout worked fine. I also used time.time() 
which returns epoch time in seconds to calculate the round trip time. For Part-B, I used
multiple counters to sum up the round trip time and count lost packets. I used those to
calculate the averages and packet loss rate.

# Running the Program :

I tested the program on Windows 10 with Ubuntu 20.04 LTS. To test run 'serv.py' first so
that it starts listening for connections. Then execute 'client.py', it will send a total
of 10 pings of which some will fail and produce a time out. The sequence, response of the
server and RTT will be printed on the terminal for evaluation. At the end, the additional
calculations will also be printed.

# References :

- Socket settimeout() method : https://docs.python.org/3/library/socket.html#socket.socket.settimeout
- Socket timeout exception   : https://docs.python.org/3/library/socket.html#socket.timeout
- Time time() method for RTT : https://www.tutorialspoint.com/python/time_time.htm
- Catching timeout exception : https://www.kite.com/python/answers/how-to-catch-a-socket-timeout-exception-in-python
- Implementation UDP Client  : https://tutorialedge.net/python/udp-client-server-python/
