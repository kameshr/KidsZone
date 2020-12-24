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

import sys
from termcolor import colored
import os
from fractions import Fraction

# Function to unwind and exit
def exitCraft():
	print(colored("Thank you for using AlgebraCraft.", 'cyan', attrs=['bold']))
	sys.exit()

# Print basic help message
def printhelp():
	print(colored("[INFO]", 'yellow', attrs=['reverse', 'bold']) + colored("Commands: sumsq <two numbers>, subsq <two numbers>, sumcb <two numbers>, subcb <two numbers>, exit", 'yellow'))

# Function to verify command prompt argument numbers
def checknum(cmd_args):
	chk_args = ['', '']
	try:
		chk_args[0] = int(cmd_args[1])
		chk_args[1] = int(cmd_args[2])
	except:
		try:
			chk_args[0] = float(cmd_args[1])
			chk_args[1] = float(cmd_args[2])
		except:
			try:
				chk_args[0] = Fraction(cmd_args[1])
				chk_args[1] = Fraction(cmd_args[2])
			except:
				print(chk_args)
				print(colored("[ERROR", 'red', attrs=['reverse', 'bold']) + colored(" Only integer, decimal and fraction numbers allowed.", 'red', attrs=['bold']))
				printhelp()
				return ["ERROR", "ERROR"]
	return chk_args

# Function to calculate square of sum of two numbers
def sumsq(cmd_args):
	chk_args = checknum(cmd_args)
	if chk_args[0] == "ERROR":
		return 0
	ans1 = pow((chk_args[0] + chk_args[1]), 2)
	ans2 = pow(chk_args[0], 2) + 2*chk_args[0]*chk_args[1] + pow(chk_args[1], 2)
	print("(a + b)ˆ2 value is " + str(ans1))
	print("aˆ2 + 2*a*b + bˆ2 value is " + str(ans2))
	return 0

# Function to calculate square of sum of two numbers
def subsq(cmd_args):
	chk_args = checknum(cmd_args)
	if chk_args[0] == "ERROR":
		return 0
	ans1 = pow(chk_args[0] - chk_args[1], 2)
	ans2 = pow(chk_args[0], 2) - 2*chk_args[0]*chk_args[1] + pow(chk_args[1], 2)
	print("(a - b)ˆ2 value is " + str(ans1))
	print("aˆ2 - 2*a*b + bˆ2 value is " + str(ans2))
	return 0

# Function to calculate cube of sum of two numbers
def sumcb(cmd_args):
	chk_args = checknum(cmd_args)
	if chk_args[0] == "ERROR":
		return 0
	ans1 = pow(chk_args[0] + chk_args[1], 3)
	ans2 = pow(chk_args[0], 3) + 3*pow(chk_args[0], 2)*chk_args[1] + 3*chk_args[0]*pow(chk_args[1], 2) +  pow(chk_args[1], 3)
	print("(a + b)ˆ3 value is " + str(ans1))
	print("aˆ3 + 3*aˆ2*b + 3*a*bˆ2 + bˆ3 value is " + str(ans2))
	return 0

# Function to calculate cube of difference of two numbers
def subcb(cmd_args):
	chk_args = checknum(cmd_args)
	if chk_args[0] == "ERROR":
		return 0
	ans1 = pow(chk_args[0] - chk_args[1], 3)
	ans2 = pow(chk_args[0], 3) - 3*pow(chk_args[0], 2)*chk_args[1] + 3*chk_args[0]*pow(chk_args[1], 2) -  pow(chk_args[1], 3)
	print("(a - b)ˆ3 value is " + str(ans1))
	print("aˆ3 - 3*aˆ2*b + 3*a*bˆ2 - bˆ3 value is " + str(ans2))
	return 0

# Function implementing the command prompt
def cmdprompt():
	os.system("clear")
	print(colored("Welcome to AlgebraCraft!", 'cyan', attrs=['bold']))
	printhelp()
	while True:
		try:
			cmd_args = input(colored(">> ", 'cyan', attrs=['bold'])).split()
		except:
			exitCraft()
		
		if len(cmd_args) == 0:
			continue

		elif cmd_args[0] == "exit":
			exitCraft()

		elif cmd_args[0] == "sumsq":
			sumsq(cmd_args)
			continue

		elif cmd_args[0] == "subsq":
			subsq(cmd_args)
			continue

		elif cmd_args[0] == "sumcb":
			sumcb(cmd_args)
			continue

		elif cmd_args[0] == "subcb":
			subcb(cmd_args)
			continue

		else:
			printhelp()
			continue
