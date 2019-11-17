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
# Description: Monu's first program :-)

print("Hello User")
print("Welcome to my program")
print("Have lots of fun")
print("This program is for addition and multiplication of numbers because it is the first time I am programming")
print("Please choose the operation you'd like to do today:\n(a) Addition (b) Multiplication")
choice = input("Please type 'a' or 'b': ")
if choice == "a" or choice == "A":
	print("Give me any number of numbers to add:")
	numbers = input().split()
	sum_numbers = 0
	for number in numbers:
	   sum_numbers = sum_numbers + int(number)
	print("Answer is " + str(sum_numbers))
elif choice == "b" or choice == "B":
	print("Give me any number of numbers to multiply:")
	numbers = input().split()
	prod_numbers = 1
	for number in numbers:
	   prod_numbers = prod_numbers * int(number)
	print("Answer is " + str(prod_numbers))
else:
	print("[ERROR] Invalid choice. Please select 'a' or 'b' only.\n")
