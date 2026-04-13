import re
from turingmachine import TM
import os


# Valid chars used to name a state
STATE_R = r"[a-zA-Z0-9]+"
# The alphabet is all printable ASCII chars except space and del (cf: https://en.wikipedia.org/wiki/ASCII)
ALPHA_R = r"[\x21-\x7E]+"

# For the name of the Turing Machine, we allow spaces
NAME_R = r"^name: ([\x20-\x7E]+)$"

INIT_R = rf"^init: ({STATE_R})$"
ACCEPT_R = rf"^accept: ({STATE_R})$"

# Finds every groups of read + transition
BLOCK_R = rf"^({STATE_R}),((?:{ALPHA_R})+)\n({STATE_R}),((?:{ALPHA_R})+)$"

def load_from_file(filepath: str) -> TM:
	if not (os.path.isfile(filepath) and os.path.splitext(filepath)[-1] in (".tm", ".utm")):
		raise ValueError(f"{filepath} is not a valid path or is not a recognized extension")

	with open(filepath, 'r') as f:
		content = f.read()

	name = re.search(NAME_R, content, re.MULTILINE)
	name = name.group(1) if name else "N/A"

	init = re.search(INIT_R, content, re.MULTILINE)
	accept = re.search(ACCEPT_R, content, re.MULTILINE)

	if not init or not accept:
		raise ValueError("Provided file is invalid, does not contain init and/or accept states description")

	init = init.group(1)
	accept = accept.group(1)

	blocks = re.findall(BLOCK_R, content, re.MULTILINE)

	# the 2nd group of the first match defines the number of tapes for the rest of the load
	number_tapes = len(blocks[0][1].split(",")) 

	# defines a lambda to check quickly if any block is invalid
	_check_block = lambda b: True if (len(b[1].split(","))==number_tapes and len(b[3].split(","))==2*number_tapes) else False

	states = set()
	transitions = dict()
	for block in blocks:
		if not _check_block(block):
			raise ValueError(f"Number of tapes is not consistent ! ({ block = })")

		states.add(block[0])
		states.add(block[2])
		read = tuple([block[0],] + block[1].split(","))
		write = tuple([block[2],] + [block[3].split(",")[:number_tapes],] + [block[3].split(",")[number_tapes:]])
		
		transitions[read] = write

	return TM(name,states,init,accept,number_tapes,transitions)


if __name__ == '__main__':
	x=load_from_file("./files/test_2tapes.tm")
	print(x)

	c = x.create_init_config("1001010100")
	print(x.next_step(c))
