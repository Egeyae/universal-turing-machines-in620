#Import of parser for function and Turing Machine for the TM class.

import parser as p
import turingmachine as TM

class TestTM:
	"""
	This class contains all the tests link to the classic Turing Machine.
	"""
	@staticmethod
	def runall():
		"""
		This function execute all test related to the class.
		"""
		print("Executing test on the Classic Turing Machine")
		TestTM.create_init_config()
		TestTM.read()
		TestTM.write()
		TestTM.move()
		TestTM.next_step()
		TestTM.run()
		TestTM.run_start()
		TestTM.run_count()
		TestTM.binary_comparison()
		TestTM.linearsearch()
		TestTM.unarymultiplication()
		print("Testing Completed on the Turing Machine.")


	@staticmethod
	def create_init_config():
		"""
		Function testing the function create_init_config() from the TM class.
		"""
		print("\tTesting creation of init config.")

		# Loading test Machines.
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		# Test with the first TM - One tape - Input '0'.
		config_init1_test = TM_test1.create_init_config('0')
		assert len(config_init1_test.before) == 1 # Check if we have one tape.
		assert len(config_init1_test.before[0]) == 0 # Check if before the reading head, the tape is empty
		assert len(config_init1_test.under) == 1 # Check if the input have been load in the tape after the reading head. 
		assert len(config_init1_test.under[0]) == 1 and config_init1_test.under[0] == ['0'] # Check if we have the input under the reading head.
		assert config_init1_test.q == TM_test1.init # Check if we are in the init stat of the machine.

		# Test with the second TM - Two tapes - Input '0'
		config_init2_test = TM_test2.create_init_config('0')

		# Same logic of checks than before, but here we have two tapes.
		assert len(config_init2_test.before) == 2
		assert len(config_init2_test.before[0]) == 0
		assert len(config_init2_test.before[1]) == 0
		assert len(config_init2_test.under) == 2
		assert len(config_init2_test.under[0]) == 1 and config_init2_test.under[0] == ['0']
		assert len(config_init2_test.under[1]) == 0
		assert config_init2_test.q == TM_test2.init

		print("\tTesting Complete.")

	@staticmethod
	def read():
		"""
		Function testing the function read() from the TM class.
		"""
		print("\tTesting Reading.")

		# Loading test Machines.
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		# Test with the first TM - One tape:
		for k in ("0","1","#","_",""): # For each case : 
			config_test = TM_test1.create_init_config(k) # We create an config.
			tuple_test = TM_test1.read(config_test) # We apply read to this config.
			if k == "": # If k == "", read replace "" by "_" so we assert this
				assert tuple_test == ('q0','_')
			else : # Else, we assert than we are indeed reading k.
				assert tuple_test == ('q0',k)
	
		# Test with the second TM - Two tapes :
		for k in ("0","1","#","_",""): # For each case, we load in the first tape k. 
			for j in ("0","1","#","_",""): # For each k, we load a j in the second tape for each case.

				# We created depending on k and j an config with k and j in the first and second tape.
				if k =="" and j =="": 
					config_test = TM.Config([[],[]],[[],[]],"q") 
				elif k =="": 
					config_test = TM.Config([[],[]],[[],[j]],"q")
				elif j =="" :
					config_test = TM.Config([[],[]],[[k],[]],"q")
				else :
					config_test = TM.Config([[],[]],[[k],[j]],"q")
				tuple_test = TM_test2.read(config_test)

				# And for each case, we check if the tuple is good on the same logic that the first machine.
				if k == "" and j == "":
					assert tuple_test == ('q','_' ,'_')
				elif k =="":
					assert tuple_test == ('q','_',j)
				elif j == "":
					assert tuple_test == ('q', k,'_')
				else :
					assert tuple_test == ('q',k,j)

		print("\tTesting Complete.")

	@staticmethod
	def write():
		"""
		Function testing the function write() from the TM class.
		"""
		print("\tTesting Writing.") 

		# Loading test Machines.
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		# Config for a machine with one tape :
		config_test = TM_test1.create_init_config("0")

		for k in ("0","1","#","_") : # For each case :
			TM_test1.write(config_test,k) # We write this symbol in the config.
			assert config_test.under[0][0] == k # And we check if under the reading head we have k.
		
		# Config for a machine with two tapes :
		config_test = TM.Config([[],[]],[["0"],["0"]],"q")
		for k in ("0","1","#","_") : # For each case.
			for j in ("0","1","#","_") : # For each case of k.
				TM_test2.write(config_test,[k,j]) # We write k and j in the config.
				# And we check on the same logic that before.
				assert config_test.under[0][0] == k
				assert config_test.under[1][0] == j

		print ("\tTesting Complete.")
	
	@staticmethod
	def move() :
		"""
		Function testing the function move() from the TM class.
		"""
		print("\tTesting Moving.") 

		# Loading test Machines.
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		# Config for a machine with one tape :
		config_test = TM_test1.create_init_config("0")
		
		# We test for each case :
			# When we move right.
		TM_test1.move(config_test,['>'])
		assert config_test.under[0][0] == '_' # Check if we have a _ under the reading head.
		assert config_test.before[0][0] == '0' # And since we move right, we check if in the before of the configuration we have '0'.
		
			# When we move left.
		TM_test1.move(config_test,['<'])
		assert config_test.under[0][0] == '0' # Check if we have now '0' under the reading head.

			# When we stay.	
		TM_test1.move(config_test,['-'])
		assert config_test.under[0][0] == '0' # Nothing change, so we suppose to still have '0' under the reading head.
		
		# Config for a machine with two tapes :
		config_test = TM.Config([[],[]],[["0"],["0"]],"q")

		# We test for each case :
			# When we move left.
		TM_test2.move(config_test,['<','<'])
		#Check if now we have '_' under each reading head.
		assert config_test.under[0][0] == '_' 
		assert config_test.under[1][0] == '_'
		# And if we have now '0' after the reading head.
		assert config_test.under[0][1] == '0'
		assert config_test.under[1][1] == '0'

			# When we move right.
		TM_test2.move(config_test,['>','>'])
		# Check if now we have '0' under each reading head.
		assert config_test.under[0][0] == '0'
		assert config_test.under[1][0] == '0'
		# And if we have now '_' before the reading head.
		assert config_test.before[0][0] == '_'
		assert config_test.before[1][0] == '_'

			# When we stay.
		# Nothing is suppose to change.
		assert config_test.under[0][0] == '0'
		assert config_test.under[1][0] == '0'
		assert config_test.before[0][0] == '_'
		assert config_test.before[1][0] == '_'

		print("\tTesting Complete.")

	@staticmethod
	def next_step():
		"""
		Function testing the function next_step() from the TM class.
		"""
		print("\tTesting Next Move.")

		# Loading test Machines.
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		# Test with the first TM - One tape - Input '000'.
		config_init1 = TM_test1.create_init_config('000') # We create an init config.
		config_init1 = TM_test1.next_step(config_init1) # And we apply next_step() on it.

		assert config_init1.q == 'q0' and config_init1.before[0][0] == '0' # We check if we are in the good state.
		assert config_init1.under[0][0] == '0' and config_init1.under[0][1] == '0' # And if have indeed moved like the transition in the machine said.

		# Test with the second TM - Two tapes - Input '000'.
		config_init2 = TM_test2.create_init_config('000') # We create an init config.
		config_init2 = TM_test2.next_step(config_init2) # And we apply next_step() on it.

		# Same logic here.
		assert config_init2.q == 'q0' and config_init2.before[1][0] == '0'
		assert config_init2.under[0][0] == '0' and config_init2.under[0][1] == '0'

		print("\tTesting Complete.")

	@staticmethod
	def run():
		"""
		Function testing the function run() from the TM class.
		"""
		print("\tTesting Run.")

		# Loading test Machines.
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		# Test with the first TM - One tape - Input '000'.
		config_init1 = TM_test1.create_init_config('000') # Creation of an init config.
		config_test1 = TM_test1.run(config_init1) # And we do a run from this init config.

		assert config_test1.q == TM_test1.accept and config_test1.under[0][0] == '_' # Check if we are in the accept state, and we have '_' under the reading head.

		# Test with the second TM - Two tapes - Input '000'.
		config_init2 = TM_test2.create_init_config('0000') # Creation of an init config.
		config_test2 = TM_test2.run(config_init2) # And we do a run from this init config.

		assert config_test2.q == TM_test2.accept and config_test2.under[0][0] == '_' and config_test2.under[1][0] == '_' # Same logic here.

		print("\tTesting Complete.")

	@staticmethod
	def run_start():
		"""
		Function testing the function run_start() from the TM class.
		"""
		print("\tTesting Run from start.")

		# Loading test Machines.
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		# Test with the first TM - One tape - Input '000'.
		config_test1 = TM_test1.run_start('000') # We run with our input.
		assert config_test1.q == TM_test1.accept and config_test1.under[0][0] == '_' # Check if we are in the final step and if '_' is under the reading head.

		# Test with the second TM - Two tapes - Input '000'.
		config_test2 = TM_test2.run_start('0000') # We run with our input.
		assert config_test2.q == TM_test2.accept and config_test2.under[0][0] == '_' and config_test2.under[1][0] == '_' # Check if we are in the final step and if '_' is under the reading head.
		
		print("\tTesting Complete.")

	@staticmethod
	def run_count():
		"""
		Function testing the function run_count() from the TM class.
		"""
		print("\tTesting Run Count.")

		# Loading test Machine.
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		
		# Test with the first TM - One tape - Input '000' and a "good" count.
		config_init1 = TM_test1.create_init_config('000') # Creation of an init config.
		config_test1,count_test1 = TM_test1.run_count(config_init1,100) # We apply run_count on the init config, and we fetch our config and our count.
		assert config_test1.q == TM_test1.accept and config_test1.under[0][0] == '_' and count_test1 > 0 # We check if we are in the same condition than run and that our counter is superior to 0.

		# Test with the first TM - One tape - Input '000' and a "bad" count.
		config_init1 = TM_test1.create_init_config('000') # Test with the first TM - One tape - Input '000' and a "good" count.
		config_test1,count_test1 = TM_test1.run_count(config_init1,1)  # We apply run_count on the init config, and we fetch our config and our count.

		assert config_test1.q == 'q0' and config_test1.under[0][0] == '0' and count_test1 == 1 # We check if we are in the same condition than run and count == 1.

		print("\tTesting Complete.")

	@staticmethod
	def binary_comparison():
		"""
		Function testing the machine for binary comparison. 
		This machine checks if x < y. If it's not the case, the machine loops infinitely.
		"""
		print("\tTesting Turing Machine Binary Comparison.")

		# Loading our machine.
		bin_compararison_TM = p.load_from_file("./files/binary_comparison.tm")

		# Testing with a good input - 100#110 - x < y.
		config_test1 = bin_compararison_TM.run_start("100#110") # We run from start with our input.
		assert config_test1.q == bin_compararison_TM.accept # And we check if our machine accept our input.

		# Testing with a bad input - 11#10 - x > y.
		config_init2 = bin_compararison_TM.create_init_config("11#10") # We create our config who will be used in run_count.
		config_test2,count = bin_compararison_TM.run_count(config_init2,50) # We run from start with our input, and using count to stop the looping.

		assert config_test2.q != bin_compararison_TM.accept and count == 50 # We check if the machine is not in the final state and if we have reached the maximum number of transitions allowed.
		
		print("\tTesting Complete.")
	
	@staticmethod
	def linearsearch():
		"""
		Function testing the machine for linear search. 
		This machine checks if x is in the list given in the inpout (input form : x#w1#w2...#wi ). If it's not the case, the machine loops infinitely.
		"""
		print("\tTesting Turing Machine Linear Search.")

		# Loading our machine.
		linearsearch_TM = p.load_from_file("./files/linearsearch.tm")

		# Testing with a good input - 10#110#10#11#00#1 - x is in the list.
		config_test1 = linearsearch_TM.run_start("10#110#10#11#00#1") # We run from start with our input.
		assert config_test1.q == linearsearch_TM.accept # And we check if our machine accept our input.

		# Testing with a bad input - 10#110#00#11#00#1 - x is not in the list.
		config_init2 = linearsearch_TM.create_init_config("10#110#00#11#00#1") # We create our config who will be used in run_count.
		config_test2,count = linearsearch_TM.run_count(config_init2,100) # We run from start with our input, and using count to stop the looping.

		assert config_test2.q != linearsearch_TM.accept and count == 100 # We check if the machine is not in the final state and if we have reached the maximum number of transitions allowed.
		
		print("\tTesting Complete.")

	@staticmethod
	def unarymultiplication():
		"""
		Function testing the machine for unary multiplication. 
		This machine calculates 1**nm with a given input in the form : 1**n#1**m.
		"""
		print("\tTesting Turing Machine Unary Multiplication.")

		# Loading our machine.
		unarymultiplication_TM = p.load_from_file("./files/unarymultiplication.tm")

		# Testing with a good input - 11#111 - expect output : 111111
		config_test1 = unarymultiplication_TM.run_start("11#111") # We run from start with our input.
		assert config_test1.q == unarymultiplication_TM.accept and config_test1.before[2].count('1') == 6 # We check if we are in the final state and if we have six 1 in the before.

		# Testing with bad input - 10#11 - expect output : None
		config_test2 = unarymultiplication_TM.run_start("10#11") # We run from start with our input, but we have not an unary number.
		assert config_test2.q ==  -1 # Check if we are not in the final state.

		print("\tTesting Complete.")



class TestUniversalTM:
	"""
	This class contains all the tests link to the Universal Turing Machine.
	"""
	@staticmethod
	def runall():
		"""
		This function execute all test related to the class.
		"""
		print("Running all tests related to the Universal Turing Machine.")
		TestUniversalTM.encode_transition()
		TestUniversalTM.encode_binary()
		TestUniversalTM.Universal_Machine()
		print("Testing Completed on the Universal Machine.")

	@staticmethod
	def encode_transition():
		"""
		Function testing the function encode_transition() from the parser file.
		"""
		print("\tTesting Encode Transition.")

		# Loading the test machine.
		TM_test1 = p.load_from_file("./files/test_1tape.tm") 

		# We create the expect binary and the binary from the function.
		correct_binary1 = "0000|01|0000|01|>|0000|00|0000|00|>|0000|11|0001|11|-"
		test_binary1 = p.encode_transitions(TM_test1)

		assert correct_binary1 == test_binary1 # And we check if they are the same.

		print("\tTesting Complete.")

	@staticmethod
	def encode_binary():
		"""
		Function testing the function encode_binary() from the parser file.
		"""
		print("\tTesting Encode Binary.")

		# Test with the first machine with one tape.
		correct_binary1 = "1000001000001110000000000001100001100011101" # Our correct binary.
		test_binary1,test_int1 = p.encode_binary("./files/test_1tape.tm") # And getting the one frome the function with the associated integer.

		assert correct_binary1 == test_binary1 and int(correct_binary1,2) == test_int1 # Check if both binary are the same and both integer are the same.

		print("\tTesting Complete.")

	@staticmethod
	def Universal_Machine():
		"""
		Function testing the simulation of the universal machine on a basic one tape machine.
		"""
		print("\tTesting correct simulation with the Universal machine.")

		# Testing with the machine one tape bis who transform 0 in 1 and 1 in 0.

		test_1tape_binary = p.encode_binary("./files/test_1tape_bis.tm")[0] # We get the binary code for the machine.
		UM = p.load_from_file("./files/utm_states4_alpha2.utm") # We load the machine on a UM class.

		# We simulate our machine and also executing the normal turing machine to compare.
		config_test1 = UM.run_code(test_1tape_binary,'000000')
		TM_test1 = p.load_from_file("./files/test_1tape_bis.tm")
		config1 = TM_test1.run_start("000")

		# Each join is for fetching the content of the concerne tape.
			# First, we check if the binary code for the machine has not changed.
		assert "".join([config_test1.before[0][i] for i in range(len(config_test1.before[0])) if config_test1.before[0][i] != '_'])+"".join([config_test1.under[0][i] for i in range(len(config_test1.under[0])) if config_test1.under[0][i] != '_']) ==  test_1tape_binary[1:] 
			# Second, we check that we are in the final state and we have '_' under the reading head.
		assert "".join([config_test1.under[1][i] for i in range(1,5)]) == '0001' and "".join([config_test1.under[1][i] for i in range(5,7)]) == p.symbol_to_bin(config1.under[0][0])
			# And finaly we check if we have the expected output : 01010111(11 -> '_').
		assert "".join([config_test1.before[2][i] for i in range(len(config_test1.before[2])) if config_test1.before[2][i] != '_'])+"".join([config_test1.under[2][i] for i in range(len(config_test1.under[2])) if config_test1.under[2][i] != '_']) == "".join([p.symbol_to_bin(config1.before[0][i]) for i in range(len(config1.before[0])) if config1.before[0][i] != '_'])+"".join(p.symbol_to_bin('_'))
		
		print("\tTesting complete.")


class TestUniversalCounterTM:
	"""
	This class contains all the tests link to the Universal Counter Turing Machine.
	"""
	@staticmethod
	def runall():
		"""
		This function execute all test related to the class.
		"""
		print("Running all test related to the Universal Machine Counter.")
		TestUniversalCounterTM.Universal_Machine_Counter()
		print("Testing Completed on the Universal Machine Counter.")

	@staticmethod
	def Universal_Machine_Counter():
		"""
		Function testing the simulation of the universal machine counter on a basic one tape machine.
		"""
		print("\tTesting correct simulation with the Universal Machine Counter.")
		
		# Testing with the machine one tape bis who transform 0 in 1 and 1 in 0.

		# We try with a "good" n, who will be enough. N is in unary.
		test_1tape_binary = p.encode_binary("./files/test_1tape_bis.tm")[0] # We get the binary code for the machine.
		UMC = p.load_from_file("./files/uctm_states4_alpha2.utm") # We load the machine on a UM class.

		# We simulate our machine and also executing the normal turing machine to compare.
		config_test1 = UMC.run_code(test_1tape_binary,'010001#111111')
		TM_test1 = p.load_from_file("./files/test_1tape_bis.tm")
		config1 = TM_test1.run_start("101")

		# Each join is for fetching the content of the concerned tape.
			# First, we check if the binary code for the machine has not changed.
		assert "".join([config_test1.before[0][i] for i in range(len(config_test1.before[0])) if config_test1.before[0][i] != '_'])+"".join([config_test1.under[0][i] for i in range(len(config_test1.under[0])) if config_test1.under[0][i] != '_']) ==  test_1tape_binary[1:] 
			# Second, we check that we are in the final state and we have '_' under the reading head.
		assert "".join([config_test1.under[1][i] for i in range(1,5)]) == '0001' and "".join([config_test1.under[1][i] for i in range(5,7)]) == p.symbol_to_bin(config1.under[0][0])
			# Third we check if we have the expected output : 00010011(11 -> '_').
		assert "".join([config_test1.before[2][i] for i in range(len(config_test1.before[2])) if config_test1.before[2][i] != '_'])+"".join([config_test1.under[2][i] for i in range(len(config_test1.under[2])) if config_test1.under[2][i] != '_']) == "".join([p.symbol_to_bin(config1.before[0][i]) for i in range(len(config1.before[0])) if config1.before[0][i] != '_'])+"".join(p.symbol_to_bin('_'))
			# And finally, we check we have the expected n number -> 3.
		assert config_test1.before[3].count('1')+config_test1.under[3].count('1') == 3

		# We try with a "bad" n, who will not be enough. N is in unary and we simulate our machine.
		config_test2 = UMC.run_code(test_1tape_binary,'010001#1')

		assert config_test2.before[3].count('1')+config_test2.under[3].count('1') == 0 # We check if we have no n "left".
		assert config_test2.q == -1 # And that we are not in the final state.

		print("\tTesting complete.")
		
if __name__ == '__main__':
	TestTM.runall()
	TestUniversalTM.runall()
	TestUniversalCounterTM.runall()