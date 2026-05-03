import os

class Config:
    def __init__(self, before: list, under: list, q: str|int):
        """
        Config class holds the current state of the machine
        Args:
            before: list of list(s) holding the content of the tapes before the reading head
            under: list of list(s) holding the content of the tapes under the reading head and after
            q: can be string or int, if string = valid state of the machine, if int should be -1 => reject state
        """   
        self.before: list = before
        self.under: list = under
        self.q: str|int = q

    def __str__(self) -> str:
        s = f"State: {self.q if type(self.q) is str else 'REJECT'}\n"

        for i in range(len(self.before)):
            s += f"[{i}]\t"+" "*(len(self.before[i]) or 1) + "v" + " "*((len(self.under[i]) - 1) > 0 or 1) + "\n"
            if len(self.before[i]) > 0:
                s += f"\t{''.join(self.before[i])}"
            else:
                s += "\t" + "_"

            if len(self.under[i]) > 1:
                s += f"{''.join(self.under[i])}\n"
            elif len(self.under[i]) == 1:
                s += f"{self.under[i][0]}" + "_" + "\n"
            else:
                s += "" + "_" + "\n"
            s += "\n"
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

    def get_nb_states(self) -> int:
        return len(self.states)

    def __str__(self) -> str:
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

    def read(self, conf: Config) -> tuple:
        """
        Reads the symbol under the read head of each tape
        Args:
            conf: current configuration of the Turing machine
        Return
            (q, a1, a2, ...):  tuple describing what is read
        """
        machine = []
        for i in range(self.nb_tapes) :
            if (len(conf.under[i]) ) > 0 : #we read the symbol under the head 
                machine.append(conf.under[i][0])
            else : 
                machine.append('_')#if the tape is empty we return a blank symbol
        return tuple([conf.q] + machine) 

    def write(self, conf: Config, symbols: list) -> None:
        """
        Writes new symbols under the head of each tape.
        Args:
            conf: current configuration of the turing machine
            symbols: symbols we write into conf
        Return
            None since it modifies the configuration
        """
        for i in range(self.nb_tapes):
            if len(conf.under[i]) > 0 :
                conf.under[i][0] = symbols[i]#overwrites the symbol currently under the head
            else : 
                #if the tape is empty we insert the symbol at position 0
                conf.under[i].insert(0, symbols[i])

    def move(self, conf: Config, movements: list) -> None:
        """
        Moves the read head of each tape according to the given directions
        Args:
            conf: current configuration of the turing machine
            movements: direction in which to move each tape of the Config
        """
        for i in range(self.nb_tapes):
            direction = movements[i]

            if direction == '>':
                #when we move to the right we pop the symbol under head into before and we then advance to the next one
                symbol = conf.under[i].pop(0) if conf.under[i] else '_'
                conf.before[i].append(symbol)
                if not conf.under[i]:#if we have reached the end we extend the tape with a blank
                    conf.under[i].append('_')  

            elif direction == '<':
                #when we move to the left we pop the last symbol of before and we insert it as a new head symbol 
                incoming = conf.before[i].pop() if conf.before[i] else '_'
                conf.under[i].insert(0, incoming)
           

    def next_step(self, conf: Config) -> Config:
        """
        Computes the next configuration of the machine from the current one following the machine rules
        Args : 
            conf : current configuration of the turing machine 
        Return : 
            updated configuration after one step 
        """
        #If we are already in accept or reject state we do not execute further
        #Reject state is represented by -1
        if conf.q == self.accept:
            return conf
        elif conf.q == -1:
            return conf

        key = self.read(conf)#we read the current state and symbols under each head 

        if key not in self.transitions:#if no transitions exists for this key, we reject 
            conf.q = -1
            return conf

        transition = self.transitions[key]#we retrieve the transition
        
        new_state   = transition[0]   #destination state 
        new_symbols = transition[1]   #symbols to write on each tape
        movements   = transition[2]   #directions to move each head

        self.write(conf, new_symbols)#we write the new symbols under each head
        self.move(conf, movements)#we move each head
        conf.q = new_state#we update the current state

        return conf 

    def run(self, conf: Config) -> Config:
        """
        Given a Config, computes all Config until end of program (q = 1) and returns the last Config
        Parameters :
            conf : A configuration of where to start the run.
        """
        while conf.q != self.accept and conf.q !=-1:
            self.next_step(conf)
        return conf

    def run_count(self,conf :Config, nb_max : int, v : bool = False) -> Config:
        """
        Given a Config, computes all Config until end of program (q = 1) or until the maximun number of transition is reached and returns the last Config
        """
        count = 0
        while (conf.q != self.accept and conf.q !=-1) and count < nb_max:
            self.next_step(conf)
            count += 1
        if count == nb_max and v :
            print("The maximun number of transition have been reach.")
        return conf,count
    
    def run_start(self, input_ : str) -> Config:
        """
        Given an input, computes all Config until end of program (q = 1) and returns the last Config
        """
        config_init = self.create_init_config(input_)
        while config_init.q != self.accept and config_init.q !=-1:
            self.next_step(config_init)
        return config_init

    def run_print_start(self, input_ : str) -> Config:
        """
        Given an input, computes all Config until end of program (q = 1) and returns the last Config
        Also prints out in a pretty manner how it works
        """
        print(f"Running with TM : {self.name}")
        conf = self.create_init_config(input_)
        step = 0
        while conf.q != self.accept and conf.q != -1:
            print(f"Step : {step}")
            print(conf)
            self.next_step(conf)
            step += 1
        print("Final Configuration :")
        print(conf)
        if conf.q == self.accept :
            print(" Accept")
        else :
            print(" Reject")
        return conf

    def run_print(self, conf: Config) -> Config:
        """
        Given a Config, computes all Config until end of program (q = 1) and returns the last Config
        Also prints out in a pretty manner how it works
        """
        print(f"Running with TM : {self.name}")
        step = 0
        while conf.q != self.accept and conf.q != -1:
            print(f"Step : {step}")
            print(conf)
            self.next_step(conf)
            step += 1
        print("Final Configuration :")
        print(conf)
        if conf.q == self.accept :
            print(" Accept")
        else :
            print(" Reject")
        return conf

    def create_init_config(self, input_: str) -> Config:
        """
        Creates a Config using the input_, and gives it the good amount of tapes
        """
        before, under = [[] for _ in range(self.nb_tapes)], [[] for _ in range(self.nb_tapes)]

        for l in input_:
            under[0].append(l)

        return Config(before,under,self.init)



if __name__ == '__main__':
    tm = TM("toto", {0, 1, 2, 3}, 0, 3, 2, dict())
    print(tm)
    print(tm.create_init_config("toto"))
