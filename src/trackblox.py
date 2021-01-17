#!/usr/bin/python3
# Copyright 2020 Suyash Raghavendra and Aryash Raghavendra
# All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import requests
from datetime import datetime
import time
import random
import sys
import os
import json
import sqlite3
from termcolor import colored

# Properties of TrackBlox daemon
LOG = ".herobrine.db"

# Init function
def setup(LOG):
	print(colored("[INFO]", 'white', attrs=['reverse', 'blink', 'bold']) + " Starting TrackBlox...")
	procs = os.popen("ps -e | grep " + __file__.split('/')[-1] + "| grep -v grep | awk '{print $1}'").read().split()
	pid = os.getpid()
	for proc in procs:
		if proc != str(pid):
			print(colored("[ERROR]", 'red', attrs=['reverse', 'bold', 'blink']) + colored(" TrackBlox already running with PID ", 'red') + colored(str(proc), 'red', attrs=['bold', 'underline']) + colored(". Shutting down.", 'red'))
			sys.exit()
	if not(os.path.isfile(LOG)):
		print(colored("[ERROR]", 'red', attrs=['reverse', 'bold', 'blink']) + colored(" Log DB file not found.", 'red'))
		sys.exit()

# Extract all roblox IDs to be tracked
def getIDs(LOG):
	rids =[]
	conn = sqlite3.connect(LOG)
	c = conn.cursor()
	uids = c.execute("SELECT userid from roblox")
	for uid in uids:
		rids.append(int(uid[0]))
	conn.close()
	return rids

# Extract authentication secrets
def getAuth(LOG):
	conn = sqlite3.connect(LOG)
	c = conn.cursor()
	rows = c.execute("SELECT userid, username, rbxid, roblosecurity FROM roblox WHERE rbxid IS NOT NULL LIMIT 1")
	for row in rows:
		auth = row
	conn.close()
	return auth

# Daemon monitoring Roblox activity
def trackDaemon(LOG):
	IDs = {}
	auth = []
	location = {0: 'MobileWebsite', 1: 'MobileInGame', 2: 'Website', 3: 'Studio', 4: 'InGame', 5: 'XBoxApp', 6: 'TeamCreate'}
	presence = {0: 'Offline', 1: 'InStudio', 2: 'InGame', 3:'Online'}
	URL = "http://api.roblox.com/"
	ts = ''
	started = False
	while True:
		try:
# Live update tracked IDs and authentication info required
			for uid in getIDs(LOG):
				if int(uid) not in IDs.keys():
					IDs[uid] = [0, '']
			if auth == []:
				auth = getAuth(LOG)

# For each tracking ID track the status of the users
			for rid in IDs.keys():
				js = requests.get(URL + "users/" + str(rid) + "/onlinestatus", cookies={".RBXID": auth[2], ".ROBLOSECURITY": auth[3]}).json()

# Case-1: User had just come online from being offline
				if (js['IsOnline'] or js['PresenceType'] != 0 or js['GameId'] is not None) and IDs[rid][0] == 0:
					if js['PresenceType'] != 0:
						IDs[rid][0] = js['PresenceType']
					else:
						IDs[rid][0] = 2
					IDs[rid][1] = js['GameId']
					user = requests.get(URL + "users/" + str(rid) + "/").json()
					ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
					conn = sqlite3.connect(LOG)
					c = conn.cursor()
					result = c.execute("INSERT INTO logblox VALUES('" + str(rid) + "', '" + user['Username'] + "', '" + str(js['GameId']) + "', '" + str(js['LastLocation'].replace("Playing", "").strip()) + "', '" + ts + "', 'Online', '0', '" + str(location[int(js['LocationType'])]) + "', '" + str(js['PlaceId']) + "', '" + str(presence[int(js['PresenceType'])]) + "')")
					conn.commit()
					conn.close()
				
# Case-2: User has switced between Roblox games
				elif (js['IsOnline'] or js['PresenceType'] != 0 or js['GameId'] is not None) and IDs[rid][0] != 0 and IDs[rid][1] != js['GameId']:
					user = requests.get(URL + "users/" + str(rid) + "/").json()
					ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
					conn = sqlite3.connect(LOG)
					c = conn.cursor()
					result = c.execute("UPDATE logblox SET endtime = '" + ts + "' WHERE userid = '" + str(rid) + "' and gameid = '" + str(IDs[rid][1]) + "' and endtime = 'Online'")
					result = c.execute("UPDATE logblox SET time =  strftime('%s', endtime) - strftime('%s', starttime) WHERE userid = '" + str(rid) + "' and gameid = '" + str(IDs[rid][1]) + "' and time = 0")
					result = c.execute("INSERT INTO logblox VALUES('" + str(rid) + "', '" + user['Username'] + "', '" + str(js['GameId']) + "', '" + str(js['LastLocation'].replace("Playing", "").strip()) + "', '" + ts + "', 'Online', '0', '" + str(location[int(js['LocationType'])]) + "', '" + str(js['PlaceId']) + "', '" + str(presence[int(js['PresenceType'])]) + "')")
					IDs[rid][1] = js['GameId']
					conn.commit()
					conn.close()
				
# Case-3: User has gone offline from being online
				elif IDs[rid][0] != 0 and not(js['IsOnline']) and js['PresenceType'] == 0 and js['GameId'] is None:
					user = requests.get(URL + "users/" + str(rid) + "/").json()
					ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
					conn = sqlite3.connect(LOG)
					c = conn.cursor()
					result = c.execute("UPDATE logblox SET endtime = '" + ts + "' WHERE userid = '" + str(rid) + "' and gameid = '" + str(IDs[rid][1]) + "' and endtime = 'Online'")
					result = c.execute("UPDATE logblox SET time =  strftime('%s', endtime) - strftime('%s', starttime) WHERE userid = '" + str(rid) + "' and gameid = '" + str(IDs[rid][1]) + "' and time = 0")
					IDs[rid][0] = 0
					IDs[rid][1] = ''
					conn.commit()
					conn.close()
				
# Case-4: Nothig interesting to report
				else:
					if not(started):
						print(colored("[INFO]", 'white', attrs=['reverse', 'bold','blink']) + " TrackBlox started succesfully.")
						started = True
					time.sleep(1)
		
# Initial exception triggers exit, else it resumes tracking
		except:
			if not(started):
				print(colored("[ERROR]", 'red', attrs=['reverse', 'bold', 'blink']) + colored(" TrackBlox startup failed.", 'red'))
				sys.exit()
			else:
				continue

# Main script
setup(LOG)
trackDaemon(LOG)
