# Copyright 2020 Aryash Raghavendra and Suyash Raghavendra
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

# File: divisibility.py
# Description: Divisibility test for natural numbers

import sympy
import numpy

NUMCOLOR = "\033[1;90;40m"
PRIMECOLOR = "\033[1;94;40m"
POWERCOLOR = "\033[1;92;40m"
POWERSYM = "\033[1;33;40m"
LOSECOLOR = "\033[0m"
ERRORCOLOR = "\033[1;31;40m"


# Divisibility test for the natural number passed across a list of numbers
# The funtion returns a list of divisors, test result and description
# explaining the divisibility results
def divTest(num):
	if not(isinstance(num, int)) or num < 1:
		return dict({-1: "[ERROR] Invalid number passed."})

	num = int(num)
	if num == 1:
		return dict({1: [True, num, "The given number is 1."]})

	divResults =dict()
	divResults[1] = [True, num, "The given number is " + str(num) + "."]

	divResults[2] = div2Test(num)
	print(divResults)

# Divisibility test for divisor 2
def div2Test(num):
	numArray = list(map(int, str(num)))
	if numArray[-1] % 2 == 0:
		return [True, int(num/2), "The last digit of " + str(num) + " is the even number " + str(numArray[-1]) + "."]
	else:
		return [False, -1, "Not divisible by " + str(2) + "."]

divTest(12)
