import parser as p
import turingmachine as TM

class TestTM:
	@staticmethod
	def runall():
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


	@staticmethod
	def create_init_config():
		print("Testing creation of init config")
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		#Test with the first TM - One tape - Input '0'
		config_init1_test = TM_test1.create_init_config('0')
		assert len(config_init1_test.before) == 1
		assert len(config_init1_test.before[0]) == 0
		assert len(config_init1_test.under) == 1
		assert len(config_init1_test.under[0]) == 1 and config_init1_test.under[0] == ['0']
		assert config_init1_test.q == TM_test1.init

		#Test with the second TM - Two tapes - Input '0'
		config_init2_test = TM_test2.create_init_config('0')
		assert len(config_init2_test.before) == 2
		assert len(config_init2_test.before[0]) == 0
		assert len(config_init2_test.before[1]) == 0
		assert len(config_init2_test.under) == 2
		assert len(config_init2_test.under[0]) == 1 and config_init2_test.under[0] == ['0']
		assert len(config_init2_test.under[1]) == 0
		assert config_init2_test.q == TM_test2.init

		print("create_init_config pass all tests")

	@staticmethod
	def read():
		print("Testing Read")
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		# Test with the first TM - One tape:
		for k in ("0","1","#","_",""):
			config_test = TM_test1.create_init_config(k)
			tuple_test = TM_test1.read(config_test)
			if k == "":
				assert tuple_test == ('q0','_')
			else :
				assert tuple_test == ('q0',k)
	
		# test with the second TM - Two tapes :
		for k in ("0","1","#","_",""):
			for j in ("0","1","#","_",""):
				if k =="" and j =="":
					config_test = TM.Config([[],[]],[[],[]],"q")
				elif k =="": 
					config_test = TM.Config([[],[]],[[],[j]],"q")
				elif j =="" :
					config_test = TM.Config([[],[]],[[k],[]],"q")
				else :
					config_test = TM.Config([[],[]],[[k],[j]],"q")
				tuple_test = TM_test2.read(config_test)


				if k == "" and j == "":
					assert tuple_test == ('q','_' ,'_')
				elif k =="":
					assert tuple_test == ('q','_',j)
				elif j == "":
					assert tuple_test == ('q', k,'_')
				else :
					assert tuple_test == ('q',k,j)

		print("Testing complete")

	@staticmethod
	def write():
		print("Testing Writing") 
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		#Config for one tape :
		config_test = TM_test1.create_init_config("0")
		for k in ("0","1","#","_") :

			TM_test1.write(config_test,k)
			assert config_test.under[0][0] == k
		
		#Config for two tapes :
		config_test = TM.Config([[],[]],[["0"],["0"]],"q")
		for k in ("0","1","#","_") :
			for j in ("0","1","#","_") :
				TM_test2.write(config_test,[k,j])
				assert config_test.under[0][0] == k
				assert config_test.under[1][0] == j

		print ("Testing complete")
	
	@staticmethod
	def move() :
		print("Testing Moving") 
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		#Config for one tape :
		config_test = TM_test1.create_init_config("0")
		
		TM_test1.move(config_test,['>'])
		assert config_test.under[0][0] == '_'
		assert config_test.before[0][0] == '0'
		TM_test1.move(config_test,['<'])
		assert config_test.under[0][0] == '0'

		#Config for two tapes :
		config_test = TM.Config([[],[]],[["0"],["0"]],"q")
		TM_test2.move(config_test,['<','<'])
		assert config_test.under[0][0] == '_'
		assert config_test.under[1][0] == '_'
		TM_test2.move(config_test,['>','>'])
		assert config_test.under[0][0] == '0'
		assert config_test.under[1][0] == '0'
		assert config_test.before[0][0] == '_'
		assert config_test.before[1][0] == '_'

		print("Testing Complete")

	@staticmethod
	def next_step():
		print("Testing Next Move")
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		#Test with the first TM - One tape - Input '000'
		config_init1 = TM_test1.create_init_config('000')
		config_init1 = TM_test1.next_step(config_init1)
		assert config_init1.q == 'q0' and config_init1.before[0][0] == '0'
		assert config_init1.under[0][0] == '0' and config_init1.under[0][1] == '0'

		#Test with the first TM - One tape - Input '000'
		config_init2 = TM_test2.create_init_config('000')
		config_init2 = TM_test2.next_step(config_init2)

		assert config_init2.q == 'q0' and config_init2.before[1][0] == '0'
		assert config_init2.under[0][0] == '0' and config_init2.under[0][1] == '0'

		print("Testing Complete")

	@staticmethod
	def run():
		print("Testing Run")
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		#Test with the first TM - One tape - Input '000'
		config_init1 = TM_test1.create_init_config('000')
		config_test1 = TM_test1.run(config_init1)
		assert config_test1.q == TM_test1.accept and config_test1.under[0][0] == '_'

		#Test with the second TM - Two tapes - Input '000'
		config_init2 = TM_test2.create_init_config('0000')
		config_test2 = TM_test2.run(config_init2)
		assert config_test2.q == TM_test2.accept and config_test2.under[0][0] == '_' and config_test2.under[1][0] == '_'
		print("Testing Complete")

	@staticmethod
	def run_start():
		print("Testing Run from start")
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		#Test with the first TM - One tape - Input '000'
		config_test1 = TM_test1.run_start('000')
		assert config_test1.q == TM_test1.accept and config_test1.under[0][0] == '_'

		#Test with the second TM - Two tapes - Input '000'
		config_test2 = TM_test2.run_start('0000')
		assert config_test2.q == TM_test2.accept and config_test2.under[0][0] == '_' and config_test2.under[1][0] == '_'
		print("Testing Complete")

	@staticmethod
	def run_count():
		print("Testing Run Count")
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		
		#Test with the first TM - One tape - Input '000'
		config_init1 = TM_test1.create_init_config('000')
		config_test1,count_test1 = TM_test1.run_count(config_init1,100)
		assert config_test1.q == TM_test1.accept and config_test1.under[0][0] == '_' and count_test1 > 0

		config_init1 = TM_test1.create_init_config('000')
		config_test1,count_test1 = TM_test1.run_count(config_init1,1)

		assert config_test1.q == 'q0' and config_test1.under[0][0] == '0' and count_test1 == 1

		print("Testing Complete")

	@staticmethod
	def binary_comparison():
		print("Testing Turing Machine Binary Comparison.")
		bin_compararison_TM = p.load_from_file("./files/binary_comparison.tm")

		#Testing with a good input - 100#110
		config_test1 = bin_compararison_TM.run_start("100#110")
		print(config_test1)
		assert config_test1.q == bin_compararison_TM.accept 

		#Testing with a bad input - 11#10
		config_init2 = bin_compararison_TM.create_init_config("11#10")
		config_test2,count = bin_compararison_TM.run_count(config_init2,50)

		assert config_test2.q != bin_compararison_TM.accept and count == 50
		print("Testing Complete.")
	
	@staticmethod
	def linearsearch():
		print("Testing Turing Machine Linear Search.")
		linearsearch_TM = p.load_from_file("./files/linearsearch.tm")

		#Testing with a good input - 10#110#10#11#00#1
		config_test1 = linearsearch_TM.run_start("10#110#10#11#00#1")
		assert config_test1.q == linearsearch_TM.accept 

		#Testing with a bad input - 10#110#00#11#00#1
		config_init2 = linearsearch_TM.create_init_config("10#110#00#11#00#1")
		config_test2,count = linearsearch_TM.run_count(config_init2,100)

		assert config_test2.q != linearsearch_TM.accept and count == 100
		print("Testing Complete.")

	@staticmethod
	def unarymultiplication():
		print("Testing Turing Machine Unary Multiplication.")
		unarymultiplication_TM = p.load_from_file("./files/unarymultiplication.tm")

		#Testing with a good input - 11#111
		config_test1 = unarymultiplication_TM.run_start("11#111")
		assert config_test1.q == unarymultiplication_TM.accept and len(config_test1.before[2]) == 6 

		#Testing with bad input - 10#11
		config_test2 = unarymultiplication_TM.run_start("10#11")

		assert config_test2.q ==  -1
		print("Testing Complete.")



class TestUniversalTM:
	# TODO: test the Universal Turing Machine class
	@staticmethod
	def runall():
		# TODO: executes all tests of this class
		TestUniversalTM.encode_transition()
		TestUniversalTM.encode_binary()
		TestUniversalTM.Universal_Machine()

	@staticmethod
	def encode_transition():
		print("Testing Encode Transition.")
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		correct_binary1 = "0000|01|0000|01|>|0000|00|0000|00|>|0000|11|0001|11|-"
		test_binary1 = p.encode_transitions(TM_test1)

		assert correct_binary1 == test_binary1
		print("Testing Complete")

	@staticmethod
	def encode_binary():
		print("Testing Encode Binary")

		# Test with the first machine with one tape.
		correct_binary1 = "1000001000001110000000000001100001100011101"
		test_binary1,test_int1 = p.encode_binary("./files/test_1tape.tm")

		assert correct_binary1 == test_binary1 and int(correct_binary1,2) == test_int1
		print("Testing Complete")

	@staticmethod
	def Universal_Machine():
		print("Testing correct simulation with the Universal machine.")
		# Testing with the machine one tape bis who transform 0 in 1 and 1 in 0.

		test_1tape_binary = p.encode_binary("./files/test_1tape_bis.tm")[0]
		UM = p.load_from_file("./files/utm_states4_alpha2.utm")
		config_test1 = UM.run_code(test_1tape_binary,'000000')
		TM_test1 = p.load_from_file("./files/test_1tape_bis.tm")
		config1 = TM_test1.run_start("000")

		assert "".join([config_test1.before[0][i] for i in range(len(config_test1.before[0])) if config_test1.before[0][i] != '_'])+"".join([config_test1.under[0][i] for i in range(len(config_test1.under[0])) if config_test1.under[0][i] != '_']) ==  test_1tape_binary[1:] 
		assert "".join([config_test1.under[1][i] for i in range(1,5)]) == '0001' and "".join([config_test1.under[1][i] for i in range(5,7)]) == p.symbol_to_bin(config1.under[0][0])
		assert "".join([config_test1.before[2][i] for i in range(len(config_test1.before[2])-2) if config_test1.before[2][i] != '_'])+"".join([config_test1.under[2][i] for i in range(len(config_test1.under[2])) if config_test1.under[2][i] != '_']) == "".join([p.symbol_to_bin(config1.before[0][i]) for i in range(len(config1.before[0])) if config1.before[0][i] != '_'])
		print("Testing complete.")


class TestUniversalCounterTM:
	# TODO: test the Universal + Counter Turing Machine class
	@staticmethod
	def runall():
		TestUniversalCounterTM.Universal_Machine_Counter()

	@staticmethod
	def Universal_Machine_Counter():
		print("Testing correct simulation with the Universal Machine Counter.")
		
		# Testing with the machine one tape bis who transform 0 in 1 and 1 in 0.

		#We try with a "good" n, who will be enough. N is in unary
		test_1tape_binary = p.encode_binary("./files/test_1tape_bis.tm")[0]
		UMC = p.load_from_file("./files/uctm_states4_alpha2.utm")
		config_test1 = UMC.run_code(test_1tape_binary,'010001#111111')
		TM_test1 = p.load_from_file("./files/test_1tape_bis.tm")
		config1 = TM_test1.run_start("101")

		assert "".join([config_test1.before[0][i] for i in range(len(config_test1.before[0])) if config_test1.before[0][i] != '_'])+"".join([config_test1.under[0][i] for i in range(len(config_test1.under[0])) if config_test1.under[0][i] != '_']) ==  test_1tape_binary[1:] 
		assert "".join([config_test1.under[1][i] for i in range(1,5)]) == '0001' and "".join([config_test1.under[1][i] for i in range(5,7)]) == p.symbol_to_bin(config1.under[0][0])
		assert "".join([config_test1.before[2][i] for i in range(len(config_test1.before[2])) if config_test1.before[2][i] != '_'])+"".join([config_test1.under[2][i] for i in range(len(config_test1.under[2])) if config_test1.under[2][i] != '_']) == "".join([p.symbol_to_bin(config1.before[0][i]) for i in range(len(config1.before[0])) if config1.before[0][i] != '_'])+"".join(p.symbol_to_bin('_'))
		assert config_test1.before[3].count('1')+config_test1.under[3].count('1') == 3

		test_1tape_binary = p.encode_binary("./files/test_1tape_bis.tm")[0]
		UMC = p.load_from_file("./files/uctm_states4_alpha2.utm")
		config_test2 = UMC.run_code(test_1tape_binary,'010001#1')
		TM_test1 = p.load_from_file("./files/test_1tape_bis.tm")

		assert config_test2.before[3].count('1')+config_test2.under[3].count('1') == 0
		assert config_test2.q == -1
		
if __name__ == '__main__':
	TestTM.runall()
	#tm_test = p.load_from_file("./files/linearsearch.tm")
	#tm_test.run_print_start('1#01#10#00#1')
	TestUniversalTM.runall()
	TestUniversalCounterTM.runall()