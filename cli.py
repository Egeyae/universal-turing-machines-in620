"""
This file contains a simple parser to run various parts of the project
Uses: argparse (from standard library)
"""
import argparse
import os
import sys
from test import *
from parser import load_from_file, encode_binary
from universalturingmachine import convert_input_to_binary

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
test.add_argument("-w", "--which", choices=["all", "tm", "utm", "uctm", "2", "3", "4", "5", "6", "7", "8", "9", "10"], help="Choose which part of the project you want to test", default="all")


# Run branch
run = action.add_parser("run", help="Executes a Turing Machine on an input")
# Input file containing the Turing Machine code
run.add_argument("file", help="File containing Turing Machine description")
# Input is either a valid path => loads the file content, or just a string
run.add_argument("input", help="Input for the TM, if it is a valid file, loads file content")
# Output format describes question 4 and 5 => only print the output + acception status or we print every configurations that lead to final result
run.add_argument("-of", "--output-format", choices=["normal", "pretty"], default="normal", help="If pretty used, prints all the TM steps, else prints the output only")
# 
run.add_argument("-b", "--bin", action="store_true", help="If set true, simulates the provided binary file using appropriate Universal Turing Machine and converts input to the right format. Crashes if not .utm.bin file is given as <file>.")

run.add_argument("-c", "--counter", type=int, default=-1, help="If counter > 0 and bin is True, then uses a Universal Counter Turing Machine instead of Universal Turing Machine. This machine is limited to <counter> steps.")

to_bin = action.add_parser("bin", help="Converts a standard Turing Machine file to a binary file")
to_bin.add_argument("file", help="File containing Turing Machine description")
to_bin.add_argument("-sb", "--states_bits", choices=[4], default=4, type=int, help="Number of bits used to compile T.M. states in binary (at 4, 2**4=16 max number of states)")
to_bin.add_argument("-ab", "--alpha_bits", choices=[2], default=2, type=int, help="Number of bits used to compile T.M. alphabet. In this project we only support the following alphabet: {0, 1, _, #} but it can be extended")

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
		if args.verbose:
			print(f"Running {args.which} tests")
		# We match which tests need to be executed
		match args.which:
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

			case "2":
				TM_test = load_from_file("./files/test_1tape.tm")
				print(TM_test)
				TestTM.create_init_config()

			case "3":
				TestTM.read()
				TestTM.write()
				TestTM.move()
				TestTM.next_step()

			case "4":
				TestTM.run()
				TestTM.run_start()
				TestTM.run_count()

			case "5":
				print("Testing full prints of ./files/test_1tape.tm on 01011101")
				TM_test = load_from_file("./files/test_1tape.tm")

				TM_test.run_print_start("01011101")


				print("Testing full prints of ./files/test_1tape.tm on 01011101")
				TM_test.run_print_start("01011101")

			case "6":
				TestTM.binary_comparison()
				TestTM.linearsearch()
				TestTM.unarymultiplication()

			case "7":
				TestUniversalTM.encode_transition()

			case "8":
				TestUniversalTM.encode_binary()

			case "9":
				TestUniversalTM.Universal_Machine()

			case "10":
				TestUniversalCounterTM.Universal_Machine_Counter()

	# Execution branch
	case "run":
		# We ensure that file arg is a valid, existing file
		assert os.path.isfile(args.file), "Invalid turing machine path specified"

		# We set the input to passed argument by default
		input_ = args.input
		# If input is a valid file, load instead the file content
		if os.path.isfile(args.input):
			with open(args.input) as f:
				input_ = f.read()

		if args.verbose:
			print(f"Execution of {args.file} on {args.input} with output format = {args.output_format}")

		if args.bin:
			with open(args.file) as f:
				states, alpha = map(int, f.readline().strip().split("|"))
			if args.counter > 0:
				name = f"./files/uctm_states{states}_alpha{alpha}.utm"
				in_ = convert_input_to_binary(args.input, alphabet_bits=alpha)+'#'+'1'*args.counter

				print(f"Running {name} with {in_}")

				universal_machine = load_from_file(name, states_size=states, alpha_size=alpha)

				universal_machine.load_and_run_binary(args.file, in_, verbose=args.output_format == "pretty", in_bin=True)
			else:
				name = f"./files/utm_states{states}_alpha{alpha}.utm"
				in_ = args.input

				print(f"Running {name} with {in_}")

				universal_machine = load_from_file(name, states_size=states, alpha_size=alpha)

				universal_machine.load_and_run_binary(args.file, in_, verbose=args.output_format == "pretty")
		else:
			machine = load_from_file(args.file)


			match args.output_format:
				case "normal":
					print(machine.run_start(args.input))
				case "pretty":
					machine.run_print_start(args.input)

	case "bin":
		assert os.path.isfile(args.file), "Invalid turing machine path specified"

		print(f"Generated: {encode_binary(args.file, args.states_bits, args.alpha_bits)[1]}")

# If we saved results to a file, properly close the opened file at the end of execution
if args.out:
	new_out.close()