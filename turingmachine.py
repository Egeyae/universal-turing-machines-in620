class Config:
    def __init__(self, before, under, q):   
        self.before = before
        self.under = under
        self.q = q

    def __str__(self):
        s= f"Before : \n"
        for i in range(len(self.before)):
            s += f"\t - {i} tape : \n"
            for j in range(len(self.before[i])):
                s+= f"\t \t - {self.before[i][j]} \n"
        s+= f"After : \n"
        for i in range(len(self.under)):
            s += f"\t - {i} tape : \n"
            for j in range(len(self.under[i])):
                s+= f"\t \t - {self.under[i][j]} \n"
        s+= f"State : {self.q}"
        return s

class TM:
    """
    TM for Turing Machine represents a Turing Machine code
    Computes for a given configuration the next step.s
    """
    def __init__(self, name: str, states: set, init: str, accept: str, nb_tapes: int, transitions: dict):
        self.name = name
        self.states = states
        self.nb_tapes = nb_tapes
        self.transitions = transitions

        if not (init in states and accept in states):
            raise ValueError("Init and Accept states have to be valid states")
        self.init = init
        self.accept = accept

    def get_nb_states(self):
        return len(self.states)

    def __str__(self):
        s =f"Name : {self.name} \n"
        s += f"Number of states : {self.get_nb_states()} \n"
        for state in self.states:
            s += f"\t - {state}"
            if state == self.init:
                s += " (init)"
            if state == self.accept:
                s += " (accept)"
            s += "\n"
        s += f"Number of tape.s : {self.nb_tapes} \n"
        for k,v in self.transitions.items():
            s+= f"\t - {k} -> {v} \n"
        return s

    def read(self, conf):
        """
        Args:
            conf: Config
        Return
            (q, a1, a2, ...):  tuple describing what is read
        """
        machine = []
        for i in range(self.nb_tape) :
            if (len(conf.under[i]) ) > 0 : 
                machine.append(conf.under[i][0])
            else : 
                machine.append('_')
        return tuple([conf.q] + machine) 

    def write(self, conf, symbols):
        """
        Args:
            conf: Config
            symbols: symbols to write into conf
        Return
            None since it modifies the configuration
        """
        for i in range(self.nb_tapes):
            if len(conf.under[i]) > 0 :
                conf.under[i][0] = symbols[i]
            else : 
                conf.under[i].insert(0, symbols[i])

    def move(self, conf, movements):
        """
        Args:
            conf: Config
            movements: direction in which to move each tape of the Config
        """
        for i in range(self.nb_tapes):
            direction = movements[i]

            if direction == '>':
                symbol = conf.under[i].pop(0) if conf.under[i] else '_'
                conf.before[i].append(symbol)
                if not conf.under[i]:
                    conf.under[i].append('_')  

            elif direction == '<':
                incoming = conf.before[i].pop() if conf.before[i] else '_'
                conf.under[i].insert(0, incoming)
        
        

    def next_step(self, conf):
        """
        Given a Config, returns the new Config following the machine rules
        """
        if conf.q == self.accept:
            return conf

        key = self.read(conf)

        if key not in self.transitions:
            raise ValueError(f"Pas de transition pour {key}")

        transition = self.transitions[key]
        new_state = transition[0]
        rest = transition[1:]

        new_symbols = list(rest[:self.nb_tapes])
        movements   = list(rest[self.nb_tapes:])
        self.write(conf, new_symbols)
        self.move(conf, movements)
        conf.q = new_state

        return conf


        

    def run(self, conf):
        """
        Given a Config, computes all Config until end of program (q = 1) and returns the last Config
        """
        pass

    def run_print(self, conf):
        """
        Given a Config, computes all Config until end of program (q = 1) and returns the last Config
        Also prints out in a pretty manner how it works
        """
        pass

    def create_init_config(self, input_):
        """
        Creates a Config using the input_, and gives it the good amount of tapes
        """
        pass


if __name__ == '__main__':
    tm = TM("toto", [0], 3, [])
    print(tm)