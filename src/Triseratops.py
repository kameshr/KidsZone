#!/usr/bin/python3

# Copyright 2019 Aryash Raghavendra
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

# File: Raptarosorous
# Description: Monu's second program :-)

print("Hello User!")
print("Welcome to my second program.")
print("This is for Division and Subtraction of only two number.")
print("Have lots of fun.")
print("Please choose the operation you'd like to do today:\n(a) Subtraction (b) Divsion")
choice = input("Please type 'a' or 'b': ")
if choice == "a" or choice == "A":
	print("Give me any two numbers to subtract:")
	numbers = input().split()
	print("Answer is " + str(float(numbers[0]) - float(numbers[1])))
elif choice == "b" or choice == "B":
	print("Give me any two numbers to divide:")
	numbers = input().split()
	print("Answer is " + str(float(numbers[0]) / float(numbers[1])))
else:
	print("[ERROR] Invalid choice. Please select 'a' or 'b' only.\n")
