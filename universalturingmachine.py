# Here ALPHABET, binary_conversion and convert_input_to_binary are duplicate of parser.py functions, this is temporary to avoid circular imports
# We should use a util.py script or similar that implements such functions. It would avoid circular imports
ALPHABET = {'0' :0, '1' : 1, '_' : 3, '#' : 2}


def binary_conversion(number, nb_bits):
	"""Function that converts decimal numbers in binary numbers
	Parameters : 
		number: represents the decimal number
		nb_bits: number of bits the number should take as bin
	"""
	
	binary = bin(number)[2:]
	if len(binary) > nb_bits : 
		raise ValueError(f"{number} cannot fit in {nb_bits} bits")
	return binary.zfill(nb_bits)

def convert_input_to_binary(input_, alphabet_bits=2):
	return "".join([binary_conversion(ALPHABET[x], alphabet_bits) for x in input_])

class UTM:
	"""
	UTM for Universal Turing Machine is a class used to hold a Universal Machine defined using Online Machine Turing Simulator syntax and then simulate any other machine compiled as binary using the UTM
	"""
	def __init__(self, machine, states_bits=4, alpha_bits=2):
		self.name = machine.name

		self.states_bits = states_bits
		self.alpha_bits = alpha_bits

		self.machine = machine

	def run_code(self, code, input_):
		"""
		This function runs the UTM on a code and an input_, only returns the result and no prints are produced.
		Asssumes that code and input_ are correctly encoded as binary
		"""
		return self.machine.run_start(f"{code}#{input_}")

	def run_code_print(self, code, input_):
		"""
		This function runs the UTM on a code and an input_, prints throughout the execution process and then returns the result
		Asssumes that code and input_ are correctly encoded as binary
		"""
		return self.machine.run_print_start(f"{code}#{input_}")


	def load_and_run_binary(self, filepath, input_, verbose=False, in_bin=False):
		"""
		This function wraps the work of this class and print the result of the simulation
		Args:
			filepath: path to a .utm.bin file, containing the binary of the simulated machine
			input_: input for the machine
			verbose: optional, if set True prints the results throughout the execution, else only print the end result
			in_bin: optional, if set True do not compile to binary the input, else does it.
		"""
		if not in_bin:
			input_ = convert_input_to_binary(input_, alphabet_bits=self.alpha_bits)

		with open(filepath, 'r') as f:
			f.readline()
			code = f.read().strip()

		if verbose:
			self.run_code_print(code, input_)
		else:
			print(self.run_code(code, input_))