"""
This file contains a simple parser to run various parts of the project
Uses: argparse (from standard library)
"""
import argparse
import os
import sys
from test import *

# Creates the parser object
parser = argparse.ArgumentParser(
	prog="Universal or Not Turing Machines", 
	description="Runs Turing Machines, specified using the format of: https://turingmachinesimulator.com/",
	epilog="Authors: Kerserlis, Egeyae, Ellyna Soumelis")

# Adds the verbose argument, which if enabled, lets part of the code display more text (if implemented)
parser.add_argument("-v", "--verbose", action="store_true", help="Increase verbosity")
# Output arg allows the user to save any output to a file, instead of standard output
parser.add_argument("--out", "--output", help="If specified, will write to specified path instead of standard output")

# Creation of 2 subtrees: either we run tests, or we execute a turing machine on an input
action = parser.add_subparsers(dest="action")

# Test branch
test = action.add_parser("test", help="Execute tests (located in test.py)")
# Specification of which tests to run, all tests by default
test.add_argument("-w", "--which", choices=["all", "tm", "utm", "uctm"], help="Choose which part of the project you want to test", default="all")


# Run branch
run = action.add_parser("run", help="Executes a Turing Machine on an input")
# Input file containing the Turing Machine code
run.add_argument("file", help="File containing Turing Machine description")
# Input is either a valid path => loads the file content, or just a string
run.add_argument("input", help="Input for the TM, if it is a valid file, loads file content")
# Output format describes question 4 and 5 => only print the output + acception status or we print every configurations that lead to final result
run.add_argument("-of", "--output-format", choices=["normal", "pretty"], default="normal", help="If pretty used, prints all the TM steps, else prints the output only")


# When cli.py is run, loads all passed arguments into args
args = parser.parse_args()

# Parser logic
# If we want to save to a file, open the file and change the standard output (needs testing)
if args.out:
	new_out = open(args.out, "w")
	sys.stdout = new_out

match args.action:
	# Test branch
	case "test":
		if args.v:
			print(f"Running {args.w} tests")
		# We match which tests need to be executed
		match args.w:
			case "all":
				TestTM.runall()
				TestUniversalTM.runall()
				TestUniversalCounterTM.runall()
			case "tm":
				TestTM.runall()
			case "utm":
				TestUniversalTM.runall()
			case "uctm":
				TestUniversalCounterTM.runall()
	# Execution branch
	case "run":
		# We ensure that file arg is a valid, existing file
		assert os.path.isfile(args.file), "Invalid turing machine path specified"

		# We set the input to passed argument by default
		input_ = args.input_
		# If input is a valid file, load instead the file content
		if os.path.isfile(args.input):
			with open(args.input) as f:
				input_ = f.read()

		if args.v:
			print(f"Execution of {args.file} on {args.input} with output format = {args.of}")

		# TODO: load the TM and init Config

		match args.of:
			case "normal":
				# TODO: run the TM as question 4
				pass
			case "pretty":
				# TODO : run the TM as question 5
				pass

# If we saved results to a file, properly close the opened file at the end of execution
if args.out:
	new_out.close()