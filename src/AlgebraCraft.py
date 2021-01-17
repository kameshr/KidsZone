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
import math
import cmath
import sympy

superscript = str.maketrans("0123456789", "\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079")

# Function to unwind and exit
def exitCraft():
	print(colored("Thank you for using AlgebraCraft.", 'cyan', attrs=['bold']))
	sys.exit()

# Print basic help message
def printhelp():
	print(colored("[INFO]", 'yellow', attrs=['reverse', 'bold', 'blink']) + colored(" Commands: qs <three co-efficients of quadratic equation to solve>, binom <two numbers> <positive integer power>, sumsq <two numbers>, subsq <two numbers>, sumcb <two numbers>, subcb <two numbers>, exit", 'yellow'))

# Function to verify command prompt argument numbers
def checknum(cmd_args):
	chk_args = []
	try:
		chk_args[0] = int(cmd_args[1])
		chk_args[1] = int(cmd_args[2])
		if len(cmd_args) == 4:
			chk_args[2] = int(cmd_args[3])
	except:
		try:
			chk_args[0] = float(cmd_args[1])
			chk_args[1] = float(cmd_args[2])
			if len(cmd_args) == 4:
				chk_args[2] = float(cmd_args[3])
		except:
			try:
				chk_args[0] = Fraction(cmd_args[1])
				chk_args[1] = Fraction(cmd_args[2])
				if len(cmd_args) == 4:
					chk_args[2] = Fraction(cmd_args[3])
			except:
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
	print("(a + b)2 value is ".translate(superscript) + str(ans1))
	print("a2 + ".translate(superscript) + "2*a*b + " + "b2 value is ".translate(superscript) + str(ans2))
	return 0

# Function to calculate square of sum of two numbers
def subsq(cmd_args):
	chk_args = checknum(cmd_args)
	if chk_args[0] == "ERROR":
		return 0
	ans1 = pow(chk_args[0] - chk_args[1], 2)
	ans2 = pow(chk_args[0], 2) - 2*chk_args[0]*chk_args[1] + pow(chk_args[1], 2)
	print("(a - b)2 value is ".translate(superscript) + str(ans1))
	print("a2 - ".translate(superscript) + "2*a*b + " + "b2 value is ".translate(superscript) + str(ans2))
	return 0

# Function to calculate cube of sum of two numbers
def sumcb(cmd_args):
	chk_args = checknum(cmd_args)
	if chk_args[0] == "ERROR":
		return 0
	ans1 = pow(chk_args[0] + chk_args[1], 3)
	ans2 = pow(chk_args[0], 3) + 3*pow(chk_args[0], 2)*chk_args[1] + 3*chk_args[0]*pow(chk_args[1], 2) +  pow(chk_args[1], 3)
	print("(a + b)3 value is ".translate(superscript) + str(ans1))
	print("a3 + ".translate(superscript) + "3*" + "a2*b + ".translate(superscript) + "3*a*" + "b2 + b3 value is ".translate(superscript) + str(ans2))
	return 0

# Function to calculate cube of difference of two numbers
def subcb(cmd_args):
	chk_args = checknum(cmd_args)
	if chk_args[0] == "ERROR":
		return 0
	ans1 = pow(chk_args[0] - chk_args[1], 3)
	ans2 = pow(chk_args[0], 3) - 3*pow(chk_args[0], 2)*chk_args[1] + 3*chk_args[0]*pow(chk_args[1], 2) -  pow(chk_args[1], 3)
	print("(a - b)3 value is ".translate(superscript) + str(ans1))
	print("a3 - ".translate(superscript) + "3*" + "a2*b + ".translate(superscript) + "3*a*" + "b2 - b3 value is ".translate(superscript) + str(ans2))
	return 0

# Function to calculate binomial expansion
def binom(cmd_args):
	chk_args = checknum(cmd_args)
	if chk_args[0] == "ERROR":
		return 0
	power = 0
	try:
		power = int(cmd_args[3])
	except:
		print(colored("[ERROR]", 'red', attrs=['reverse', 'blink']) + colored(" Power should be a positive integer.", 'red', attrs=['bold']))
		printhelp()
		return -1
	
	if power <= 0:
		print(colored("[ERROR]", 'red', attrs=['reverse', 'blink']) + colored(" Power should be a positive integer.", 'red', attrs=['bold']))
		printhelp()
		return -1
	
	var_color = 'magenta'
	pow_color = 'green'
	op_color = 'yellow'
	coeff_color = 'white'
	value_color = 'white'
	
	coeff = int(1)
	formula = colored("a", var_color) + colored(str(power).translate(superscript), pow_color)
	value = pow(chk_args[0], power)

	for i in range(power - 1, -1, -1):
		coeff = int(coeff*(i + 1)/(power - i))

		formula = formula + colored(" + ", op_color)
		if coeff != 1:
			formula = formula + colored(str(coeff), coeff_color)
		
		if i == 1:
			formula = formula + colored("a", var_color)
		elif i > 1:
			formula = formula + colored("a", var_color) + colored(str(i).translate(superscript), pow_color)
		
		if power - i == 1:
			formula = formula + colored("b", var_color)
		elif power - i > 1:
			formula = formula + colored("b", var_color) + colored(str(power - i).translate(superscript), pow_color)

		value = value + coeff*pow(chk_args[0], i)*pow(chk_args[1], power - i)
	print(colored("(", op_color) + colored("a", var_color) + colored(" + ", op_color) + colored("b", var_color) + colored(")", op_color) + colored(str(power).translate(superscript), pow_color) + colored(" = ", op_color) + formula)
	print(colored("Therefore, (", op_color) + colored(str(chk_args[0]), var_color) + colored(" + ", op_color) + colored(str(chk_args[1]), var_color) + colored(")", op_color) + colored(str(power).translate(superscript), pow_color) + colored(" = ", op_color) + colored(str(value), value_color))

# Qudratic equation solution
def quadsolve(cmd_args):
	chk_args = [Fraction(), Fraction(), Fraction()]
	try:
		chk_args[0] = Fraction(cmd_args[1])
		chk_args[1] = Fraction(cmd_args[2])
		chk_args[2] = Fraction(cmd_args[3])
	except:
		print(colored("[ERROR]",'red',attrs=['bold', 'blink', 'reverse']) + colored(" Quadratic equation co-efficients 'a', 'b' and 'c' need to be integers, decimals or fractions only.", 'red'))
		return 0
	
	var_color = 'blue'
	pow_color = 'green'
	op_color = 'yellow'
	coeff_color = 'white'
	value_color = 'white'

	if chk_args[0] == 0:
		print(colored("[ERROR]", 'red', attrs=['bold', 'blink', 'reverse']) + colored(" Not a quadratic equation.", 'red', attrs=['bold']))
		return 0
	
	delta = pow(chk_args[1], 2) - 4*chk_args[0]*chk_args[2]
	root1 = root2 = "Undefined"
	equation = ''

	if chk_args[0] < 0:
		equation = colored("-", op_color) + colored(str(abs(chk_args[0])), coeff_color) + colored("x", var_color) + colored(str("2").translate(superscript), pow_color)
	elif chk_args[0] == 1:
		equation = colored("x", var_color) + colored(str("2").translate(superscript), pow_color)
	else:
		equation = colored(str(abs(chk_args[0])), coeff_color) + colored("x", var_color) + colored(str("2").translate(superscript), pow_color)
	
	if chk_args[1] < 0:
		equation = equation + colored(" - ", op_color) + colored(str(abs(chk_args[1])), coeff_color) + colored("x", var_color)
	elif chk_args[1] == 1:
		equation = equation + colored(" + ", op_color) + colored("x", var_color)
	elif chk_args[1] > 0:
		equation = equation + colored(" + ", op_color) + colored(str(abs(chk_args[1])), coeff_color) + colored("x", var_color)

	if chk_args[2] < 0:
		equation = equation + colored(" - ", op_color) + colored(str(abs(chk_args[2])), coeff_color)
	elif chk_args[2] > 0:
		equation = equation + colored(" + ", op_color) + colored(str(abs(chk_args[2])), coeff_color)
	
	equation = equation + colored(" = ", op_color) + colored("0", coeff_color)

	if delta < 0:
		print(colored("[INFO]", 'yellow', attrs=['bold', 'blink', 'reverse']) + colored(" Roots are complex.", 'yellow'))
		root1 = colored(str((-chk_args[1] + cmath.sqrt(delta))/(2*chk_args[0])), value_color, attrs=['bold', 'underline'])
		root2 = colored(str(((-chk_args[1]) - cmath.sqrt(delta))/(2*chk_args[0])), value_color, attrs=['bold', 'underline'])
	elif (math.sqrt(delta) - math.floor(math.sqrt(delta)) == 0): 
		print(colored("[INFO]", 'yellow', attrs=['bold', 'blink', 'reverse']) + colored(" Roots are rational.", 'yellow'))
		root1 = colored(str(Fraction((-chk_args[1] + math.sqrt(delta))/(2*chk_args[0]))), value_color, attrs=['bold', 'underline'])
		root2 = colored(str(Fraction((-chk_args[1] - math.sqrt(delta))/(2*chk_args[0]))), value_color, attrs=['bold', 'underline'])
	else:
		print(colored("[INFO]", 'yellow', attrs=['bold', 'blink', 'reverse']) + colored(" Roots are irrational.", 'yellow'))
		root1 = colored(str((-chk_args[1] + sympy.sqrt(delta))/(2*chk_args[0])), value_color, attrs=['bold', 'underline'])
		root2 = colored(str((-sympy.sqrt(delta) - chk_args[1])/(2*chk_args[0])), value_color, attrs=['bold', 'underline'])
	
	print("Solutions to the equation " + equation + " are " + root1 + " and " + root2 + ".")

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

		elif cmd_args[0] == "binom":
			binom(cmd_args)
			continue

		elif cmd_args[0] == "qs":
			quadsolve(cmd_args)
			continue

		else:
			printhelp()
			continue
