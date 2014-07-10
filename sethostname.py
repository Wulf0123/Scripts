#!/usr/bin/env python

"""
Author: Bradley M Richards
Date Created: 06/25/2014
Last Modified: 06/26/2014
Description: 
	With no/or invalid arguments it displays the current hostname
	Given a hostname it updates the hostname of a Linux based system
"""

import sys, os, socket

def main(host):
	if userIsAdmin():
		oldHost = getHostname()
		updateNetworkFile(oldHost, host)
		updateHostsFile(oldHost, host)
		os.system("reboot")
	else:
		print 'Hostname Not Changed: Please rerun with Administrative rights'
		print getHostname()
		
def userIsAdmin():
	Files = '/etc/sysconfig/network', '/etc/hostname', '/etc/HOSTNAME', '/etc/hosts'
	for file in Files:
		if os.path.isfile(file):
			if not os.access(file, os.W_OK) or not os.access(file, os.R_OK):
				return False
	return True

def getHostname():
	if socket.gethostname().find('.') >= 0:
		return socket.gethostbyaddr(socket.gethostname())[0]
	else:
		return socket.gethostname()
	
def updateNetworkFile(oldhostname, newhostname):
	NetworkFiles = ['/etc/sysconfig/network', '/etc/hostname', '/etc/HOSTNAME']
	
	for NetworkFile in NetworkFiles:
		if os.path.isfile(NetworkFile):
			network = open(NetworkFile, 'r')
			lines = network.readlines()
			network.close()
			network = open(NetworkFile, 'w')
			output = ''
			for line in lines:
				if not line.isspace():
					line = line.replace(oldhostname, newhostname)
					output += line
			network.write(output)
			network.close()
		
def updateHostsFile(oldhostname, newhostname):
	hostsfile = '/etc/hosts'
	if os.path.isfile('/etc/hosts'):
		network = open('/etc/hosts', 'r')
		lines = network.readlines()
		network.close()
		network = open('/etc/hosts', 'w')
		output = ''
		for line in lines:
			if not line.isspace():
				if 'localhost' in line and oldhostname not in line:
					line = line.replace('localhost', newhostname)
				else:
					line = line.replace(oldhostname, newhostname)
				if ('127.0.0.1' in line or '::1' in line) and 'localhost' not in line:
					line = line.rstrip() + '\tlocalhost\n'
				output = output + line
		network.write(output)
		network.close()		

if __name__ == "__main__":
	if len(sys.argv) == 2:
		main(sys.argv[1])
	else:
		print getHostname()

