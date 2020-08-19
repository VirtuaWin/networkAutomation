# Open a file called myswitches which contains the IP addresses of the SWs we are going to configure
file = open('myswitches')

for IP in file:
    print('Configuring SW ' + IP)
# At each cycle, the variable IP takes the value of each IP (of each line) that's in the file
