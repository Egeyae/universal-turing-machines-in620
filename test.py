import parser as p
import turingmachine as TM

class TestTM:
	# TODO: test the Turing Machine class
	@staticmethod
	def runall():
		print("Executing test on the Classic Turing Machine")
		# TODO: executes all tests of this class
		TestTM.create_init_config()
		TestTM.read()
		TestTM.write()
		TestTM.move()
		TestTM.next_step()
		TestTM.run()


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



class TestUniversalTM:
	# TODO: test the Universal Turing Machine class
	@staticmethod
	def runall():
		# TODO: executes all tests of this class
		pass

class TestUniversalCounterTM:
	# TODO: test the Universal + Counter Turing Machine class
	@staticmethod
	def runall():
		# TODO: executes all tests of this class
		pass

TestTM.runall()