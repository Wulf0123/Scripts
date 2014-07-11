Scripts
=======
sethostname.py: Used to change the hostname on a given Linux machine
 - In your .bashrc for the root user add alias sethostname=path/sethostname.py to run sethostname directly from terminal
 - Can be run with no arguements, in which case it displays the current hostname
 - When run with 1 arguement it updates the hostname and restarts the machine to commit the changes
 - When run with any other number of arguements it defaults to displaying the current hostname

ip.py: Used to find the IPs of a local machine
 - addressInfo() or command -a: Prints the output of the unix command ip addr show
 - validIPs() or command -i: Prints all the valid IPs of the system
 - command -i4: Prints all valid IPv4 IPs of the system
 - command -i6: Prints all valid IPv6 IPs of the system
 - IP prints the current valid IPv4 IPs. Goal is to be the IP that you would want in all circumstances (i.e. IP that external sources can access you by)
