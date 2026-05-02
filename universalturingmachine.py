# Here ALPHABET, binary_conversion and convert_input_to_binary are duplicate of parser.py functions, this is temporary to avoid circular imports

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
    def __init__(self, machine, states_bits=4, alpha_bits=2):
        self.name = machine.name

        self.states_bits = states_bits
        self.alpha_bits = alpha_bits

        self.machine = machine

    def run_code(self, code, input_):
        return self.machine.run_start(f"{code}#{input_}")

    def run_code_print(self, code, input_):
        return self.machine.run_print_start(f"{code}#{input_}")


    def load_and_run_binary(self, filepath, input_, verbose=False, in_bin=False):
    	if not in_bin:
    		input_ = convert_input_to_binary(input_, alphabet_bits=self.alpha_bits)
    	with open(filepath, 'r') as f:
    		f.readline()
    		code = f.read().strip()

    	if verbose:
    		self.run_code_print(code, input_)
    	else:
    		print(self.run_code(code, input_))