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

import sqlite3
import sys
import os
import random
import pandas
from datetime import datetime
from termcolor import colored

def searchnote(cmd_args, user):
	if len(cmd_args) == 1:
		print(colored("[COMMAND INCOMPLETE]", 'red', attrs=['reverse', 'blink']) + colored("Use date <diary note date> or search subject <diary note subject>.", 'red'))
		return -1
	elif cmd_args[1] == "date":
		if len(cmd_args) == 2:
			print(colored("[COMMAND INCOMPLETE]", 'red', attrs=['reverse', 'blink']) + colored("Specify the Diary Note date in the format YYYY-MM-DD.", 'red'))
			return -1
		else:
			conn = sqlite3.connect(".herobrine.db")
			print(pandas.read_sql_query("SELECT * from diary WHERE AUTHOR = '" + user + "' AND DATE like '" + cmd_args[2] + "%'", conn))
			conn.close()
			return 0
	elif cmd_args[1] == "subject" or cmd_args[1] == "user":
		if len(cmd_args) == 2:
			print(colored("[COMMAND INCOMPLETE]", 'red', attrs=['reverse', 'blink']) + colored("Specify the Diary Note subject.", 'red'))
			return -1
		else:
			conn = sqlite3.connect(".herobrine.db")
			print(pandas.read_sql_query("SELECT * from diary WHERE AUTHOR = '" + user + "' AND SUBJECT like '%" + cmd_args[2] + "%'", conn))
			conn.close()
			return 0
	else:
		print(colored("[COMMAND INCOMPLETE]", 'red', attrs=['reverse', 'blink']) + colored("Use search date <diary note date> or subject <diary note subject>.", 'red'))
		return -1

def newnote(cmd_args, user):
	subject = input(colored("Please type the subject name of the new note: ", 'yellow', attrs=['reverse', 'bold']))
	note = input(colored("Please type the new note: ", 'yellow', attrs=['reverse', 'bold']))
	now = datetime.now()
	d_string = now.strftime("%Y-%m-%d %H:%M:%S")
	conn = sqlite3.connect(".herobrine.db")
	c = conn.cursor()
	result = c.execute("INSERT INTO diary VALUES('" + str(random.randint(0,1000000000)) + "', '" + d_string + "', '" + subject + "', '" + note + "', '" + user + "')")
	conn.commit()
	conn.close()
	print(colored("[INFO]", 'yellow', attrs=['reverse', 'bold']) + colored("Note saved successfully. Thank you.", 'yellow'))

# Function to delete note
def deletenote(cmd_args, user):
	if len(cmd_args) == 1:
		print(colored("[COMMAND INCOMPLETE]", 'red', attrs=['reverse', 'blink']) + colored("Please use delete date <diary note date> or delete subject <diary note subject>.", 'red'))
		return -1	
	elif cmd_args[1] == "date":
		if len(cmd_args) == 2:
			print(colored("[COMMAND INCOMPLETE]", 'red', attrs=['reverse', 'blink']) + colored("Please specify the Diary Note date in the format YYYY-MM-DD.", 'red'))
			return -1
		else:
			searchnote(cmd_args, user)
			notenum = input(colored("Please type the Note ID of the Note to be deleted: ", 'yellow', attrs=['reverse', 'bold']))
			conn = sqlite3.connect(".herobrine.db")
			c = conn.cursor()
			result = c.execute("DELETE FROM diary WHERE AUTHOR = '" + user + "' AND ID = '" + notenum + "'")
			conn.commit()
			conn.close()
			print(colored("[INFO]", 'yellow', attrs=['reverse', 'bold']) + colored(" Note deleted successfully.", 'yellow'))
			return 0
	elif cmd_args[1] == "subject":
		if len(cmd_args) == 2:
			print(colored("[COMMAND INCOMPLETE]", 'red', attrs=['reverse', 'blink']) + colored("Please specify the Diary Note subject to search.", 'red'))
			return -1
		else:
			searchnote(cmd_args, user)
			notenum = input(colored("Please type the Note ID of the Note to be deleted: ", 'yellow', attrs=['reverse', 'bold']))
			conn = sqlite3.connect(".herobrine.db")
			c = conn.cursor()
			result = c.execute("DELETE FROM diary WHERE AUTHOR = '" + user + "' AND ID = '" + notenum + "'")
			conn.commit()
			conn.close()
			print(colored("[INFO]", 'yellow', attrs=['reverse', 'bold']) + colored("Note deleted successfully.", 'yellow'))
			return 0

# Help message
def helpmesg(user):
	if user == 'Roblox':
		print(colored("Commands help:\n1) search date <log date in YYYY-MM-DD> | user <username>\n2) exit", 'yellow'))
	else:
		print(colored("Commands help:\n1) search date <note date in YYYY-MM-DD> | subject <note subject>\n2) newnote\n3) deletenote date <note date in YYYY-MM-DD> | subject <note subject>\n4) exit", 'yellow'))

# Command prompt function
def cmd_prompt():
	os.system("clear")
# Program startup message
	print(colored("Welcome to Eternal Diary!", 'cyan', attrs=['bold']))

# User name needed for securing access to database
	user = input(colored("Username:", 'cyan', attrs=['reverse']) + " ")
	if user == "Roblox":
		print(colored("[INFO]", 'yellow', attrs=['reverse', 'blink', 'bold']) + colored("Today's LogBlox entries:", 'yellow', attrs=['bold']))
		searchnote(['search', 'date', datetime.now().strftime("%Y-%m-%d")], user)
		print(colored("=================================", 'yellow'))
	helpmesg(user)

# Main command prompt for the program
	while True:
		try:
			cmd_args = input(colored(">> ", 'cyan', attrs=['bold'])).split()
		except:
			print(colored("Thank you for using Eternal Diary.", 'yellow'))
			conn.close()
			sys.exit()
		
		if len(cmd_args) == 0:
			continue

		elif cmd_args[0] == "search":
			searchnote(cmd_args, user)
			continue

		elif cmd_args[0] == "newnote":
			newnote(cmd_args, user)
			continue

		elif cmd_args[0] == "exit":
			print(colored("Thank you for using Eternal Diary.", 'cyan', attrs=['bold']))
			sys.exit()

		elif cmd_args[0] == "deletenote":
			deletenote(cmd_args, user)
			continue

		else:
			helpmesg()
			continue

# Main program
cmd_prompt()
