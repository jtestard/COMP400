#!/bin/sh

#I have special configurations but other users may not.
#This file is meant to be called from the project root dir

if [ "$(whoami)"=="jtestard" ]; then 
	sudo cgexec -g memory:limited /home/jtestard/epd-7.3-2-rh5-x86/bin/python python/python_start.py
else
	cgexec -g memory:limited python python/python_start.py
fi
