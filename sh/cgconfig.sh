#Create the group to be added in cggroups.
GROUP = "group limited {
	memory {
		memory.limit_in_bytes = 75M;
  	}
}"

#Add the group to config file
#This creates files at /sys/fs/cgroup/memory/limited
sudo $GROUP >> /etc/cgconfig.conf

#Restart the cgconfig service
sudo restart cgconfig

#Change ownership for directory

sudo chown -R $(whoami) /sys/fs/cgroup/memory/limited

#Now you can exec your files with the restriction using a command such as 
#cgexec -g memory:limited command

