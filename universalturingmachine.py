# WARNING ! _ should always be 3 !!!
ALPHABET = {'0' :0, '1' : 1, '_' : 3, '#' : 2}

MOVEMENTS = {'<' : 0, '-' : 1, '>':3 }

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

def rename_states(machine, nb_bits = 4) :
	"""Renames all the states with a binary number instead
	We force the naming of the initial state and the accept state to 0 and 1 each
	Parameters : machine which represents the turing machine we want to convert
	"""
	max_states = 2**nb_bits
	if len(machine.states) > max_states :
		raise ValueError(f"Too many states ({len(machine.states)}) for {nb_bits} bits (max {max_states})")
	
	dico_states = {}
	dico_states[machine.init] = binary_conversion(0, nb_bits)
	dico_states[machine.accept] = binary_conversion(1, nb_bits)

	counter = 2

	for state in machine.states :
		if state not in dico_states:
			dico_states[state] = binary_conversion(counter, nb_bits)
			counter+=1
	
	return(dico_states)

def symbol_to_bin(symbol, nb_bits = 2):
	if symbol not in ALPHABET : 
		raise ValueError(f"Symbol {symbol} not in fixed alphabet {set(ALPHABET.keys())}")
	return binary_conversion(ALPHABET[symbol], nb_bits)

def encode_alphabet(machine, nb_bits = 2):
	alphabet = set()

	for key,value in machine.transitions.items():
		alphabet.add(key[1])
		alphabet.add(value[1][0])

	max_symbols = 2**nb_bits
	if len(alphabet)>max_symbols : 
		raise ValueError(f"Too many symbols ({len(alphabet)} for {nb_bits} bits (max {max_symbols}))")
	
	alphabet_bis = {}

	for symbol in alphabet :
		alphabet_bis[symbol] = symbol_to_bin(symbol, nb_bits)
	return alphabet_bis

def encode_movement(movement, nb_bits = 2):
	if movement not in MOVEMENTS:
		raise ValueError(f"Unknown movement :{movement}")
	return binary_conversion(MOVEMENTS[movement], nb_bits)


def encode_transitions(machine, state_bits = 4, alphabet_bits = 2):
	"""Transforms the syntax of the MT transitions into the syntax wanted
	Parameter : MT"""

	states = rename_states(machine, state_bits)
	alphabet_machine = encode_alphabet(machine, alphabet_bits)
	t_transitions = []
	
	for key,value in machine.transitions.items() :
		current_state = states[key[0]]
		symbol_read = alphabet_machine[key[1]]
		new_state = states[value[0]]
		symbol_written = alphabet_machine[value[1][0]]
		movement = value[2][0]

		t_transitions.append(current_state + "|" + symbol_read + "|" + new_state + "|" + symbol_written + "|" + movement)

	return "|".join(t_transitions)

def universal_machine(filepath, state_bits = 8, alphabet_bits = 2):
	"""Final function to determine a universal machine 
	Parameter : filepath"""

	machine = load_from_file(filepath)
	machine_final = encode_transitions(machine, state_bits, alphabet_bits)
	
	return machine_final


def encode_binary(filepath, state_bits= 8, alpha_bits = 2):
	"""Function that produces the binary coding of the mt simulator file 
	Parameter : filepath"""
	machine_final = universal_machine(filepath, state_bits, alphabet_bits )

	elements = machine_final.split("|")

	encoding =[]
	for element in elements : 
		if element in MOVEMENTS : 
			encoding.append(encode_movement(element, alphabet_bits))
		else: 
			encoding.append(element)
			
	encoding = "1" + "".join(encoding)
	integer = int(encoding, 2)

	utm_path = filepath.replace('.tm', '.utm.bin')
	with open(utm_path, 'w') as f: 
		f.write(f"{state_bits}|{alphabet_bits}\n")
		f.write(encoding)

	return encoding, integer

def convert_input_to_binary(input_, alphabet_bits=2):
	return "".join([binary_conversion(x, alphabet_bits) for x in input_])

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

    def convert_to_binary(self, other_tm_filepath):
    	return encode_binary(other_tm_filepath, state_bits=self.states_bits, alphabet_bits=self.alpha_bits)[0]

    def load_and_run_binary(self, filepath, input_, verbose=False, in_bin=False):
    	if not in_bin:
    		input_ = convert_input_to_binary(input_, alpha_bits=self.alpha_bits)
    	with open(filepath, 'r') as f:
    		f.readline()
    		code = f.read().strip()

    	if verbose:
    		self.run_code_print(code, input_)
    	else:
    		self.run_code(code, input_)