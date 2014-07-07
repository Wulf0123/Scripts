Scripts
=======
sethostname.py: Used to change the hostname on a given Linux machine
 - In your .bashrc for the root user add alias sethostname=path/sethostname.py to run sethostname directly from terminal
 - Can be run with no arguements, in which case it displays the current hostname
 - When run with 1 arguement it updates the hostname and restarts the machine to commit the changes
 - When run with any other number of arguements it defaults to displaying the current hostname
