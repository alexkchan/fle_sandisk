import subprocess	#To call temrinal commands
import re			#Regular expression syntax formats

from googleSheet import get_spreadsheet_id_row_mapping

def get_server_id_list():
	#scan for wifi
	proc = subprocess.Popen('iwlist wlan0 scan 2>/dev/null', shell=True, stdout=subprocess.PIPE,)
	#displays outputs of list
	stdout_str = proc.communicate()[0]
	#parse the outputs
	stdout_list = stdout_str.split('\n')
	#empty array to save the parsed outputs
	server_ids=[]
	#search for wifi server_ids that match SanDisk Media
	for line in stdout_list:
		line=line.strip()
		match=re.search('SanDisk Media (\w\w\w\w)', line)
		if match:
			server_ids.append(match.group(1))
	#make it look pretty
	server_ids = list(set(server_ids))
	return server_ids

server_ids = get_server_id_list()

print(server_ids)

server_id_row_map = get_spreadsheet_id_row_mapping()

print(server_id_row_map)

#Add empty dictionary to keep track active threads, in case server dies partway through
	# Mapping of server_ids to thread

#Add a dictionary of wifi dongles 

#Mutex threading to control what task the wifi dongles are on
# for server_id in server_ids:
# 	if server_id not in server_dictionary:
		#Method: Look at available WiFi dongles, configure the server on one
		#Check to see if partway through configuration
		#Add new row to spreadsheet		

#choose server/SSID that is not being configured, assign to WiFi dongle

