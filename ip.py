#!/usr/bin/env python

"""
Author: Bradley M Richards
Date Created: 07/10/2014
Last Modified: 07/11/2014
Description: 
	Displays the valid ips of the device
"""

import sys, subprocess

def main(commands):
	for command in commands:
		if command == '-a':		#Prints address info
			print "\n".join(addressInfo())
		elif command == '-i':	#Prints all the valid IPs
			print "\n".join((str(ip[0]) + ' ' + str(ip[1]) + ' ' + str(ip[2])) for ip in validIPs())
		elif command == '-i4':	#Prints all valid IPv4 IPs
			print "\n".join((str(ip[0]) + ' ' + str(ip[1])) for ip in validIPs() if ip[2] == 'IPv4')
		elif command == '-i6':	#Prints all valid IPv6 IPs
			print "\n".join((str(ip[0]) + ' ' + str(ip[1])) for ip in validIPs() if ip[2] == 'IPv6')
	
def addressInfo():
	ipInfo = []
	for line in subprocess.Popen(['ip', 'addr', 'show'], stdout=subprocess.PIPE).stdout:
		if not line.isspace():
			ipInfo.append(line.rstrip())
	return ipInfo
	
def validIPs():
	ips = []
	ipInfo = addressInfo()
	name = ''
	count = 1
	v4 = 'inet '
	v6 = 'inet6 '
	for line in ipInfo:
		nthIP = str(count) + ': '
		if nthIP in line:
			count += 1
			begin = line.find(': ') + 2
			end = line.find(': ', begin+1)
			if(begin == -1 or end == -1): break
			name = line[begin:end]
		if v4 in line:
			begin = line.find(v4) + 5
			end = line.find('/', begin+1)
			if(begin == -1 or end == -1): break
			ip = line[begin:end]
			ips.append((name, ip, 'IPv4'))
		elif v6 in line:
			begin = line.find(v6) + 6
			end = line.find('/', begin+1)
			if(begin == -1 or end == -1): break
			ip = line[begin:end]
			ips.append((name, ip, 'IPv6'))
	return ips
	
def IP():
	valid_ips = []
	ips = validIPs()
	for ip in ips:
		if ip[0] != 'lo' and ip[2] == 'IPv4':
			valid_ips.append(ip[1])
	return valid_ips
	
if __name__ == "__main__":
	if len(sys.argv) > 1:
		main(sys.argv)
	else:
		print "\n".join(IP())
