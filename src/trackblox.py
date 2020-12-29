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

print("[INFO] Starting TrackBlox...")
LOG = ".herobrine.db"
if not(os.path.isfile(LOG)):
	print("[ERROR] Log DB file not found.")
	sys.exit()
IDs = {}
conn = sqlite3.connect(LOG)
c = conn.cursor()
for row in c.execute("SELECT userid from roblox"):
	IDs[int(row[0])] = False
conn.close()

URL = "http://api.roblox.com/"
ts = ''
started = False

while True:
	try:
		for rid in IDs.keys():
			json = requests.get(URL + "users/" + str(rid) + "/onlinestatus").json()
			if json['IsOnline'] and not(IDs[rid]):
				IDs[rid] = True
				user = requests.get(URL + "users/" + str(rid) + "/").json()
				ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				conn = sqlite3.connect(LOG)
				c = conn.cursor()
				result = c.execute("INSERT INTO diary VALUES('" + str(random.randint(0,1000000000)) + "', '" + ts + "', '" + str(user['Username']) + " LOGGED IN', 'User ID: " + str(rid) + "', 'Roblox')")
				conn.commit()
				conn.close()
			elif IDs[rid] and not(json['IsOnline']):
				IDs[rid] = False
				user = requests.get(URL + "users/" + str(rid) + "/").json()
				ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				conn = sqlite3.connect(LOG)
				c = conn.cursor()
				result = c.execute("INSERT INTO diary VALUES('" + str(random.randint(0,1000000000)) + "', '" + ts + "', '" + str(user['Username']) + " LOGGED OUT', 'User ID: " + str(rid) + "', 'Roblox')")
				conn.commit()
				conn.close()
			else:
				if not(started):
					print("[INFO] TrackBlox started succesfully.")
					started = True
				time.sleep(1)
	except:
		if not(started):
			print("[ERROR] TrackBlox startup failed.")
			sys.exit()
		else:
			continue
