class Config:
    def __init__(self, before: list, under: list, q: str|int) -> Config:
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
            s += f"[{i}]\t"+" "*(len(self.before[i]) or 3) + "v" + " "*((len(self.under[i]) - 1) > 0 or 3) + "\n"
            if len(self.before[i]) > 0:
                s += f"\t{''.join(self.before[i])}"
            else:
                s += "\t" + "_" * 3

            if len(self.under[i]) > 1:
                s += f"{''.join(self.under[i])}\n"
            elif len(self.under[i]) == 1:
                s += f"{self.under[i][0]}" + "_" * 3 + "\n"
            else:
                s += "" + "_" * 3 + "\n"
            s += "\n"
        return s

class TM:
    """
    TM for Turing Machine represents a Turing Machine code
    Computes for a given configuration the next step.s
    """
    def __init__(self, name: str, states: set, init: str, accept: str, nb_tapes: int, transitions: dict) -> TM:
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
        Args:
            conf: Config
        Return
            (q, a1, a2, ...):  tuple describing what is read
        """
        machine = []
        for i in range(self.nb_tapes) :
            if (len(conf.under[i]) ) > 0 : 
                machine.append(conf.under[i][0])
            else : 
                machine.append('_')
        return tuple([conf.q] + machine) 

    def write(self, conf: Config, symbols: list) -> None:
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

    def move(self, conf: Config, movements: list) -> None:
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
           

    def next_step(self, conf: Config) -> Config:
        """
        Given a Config, returns the new Config following the machine rules
        """
        #si on arrive dans un état accept ou reject on execute pas le prochain état 
        #pour représenter un état reject on choisit -1 

        if conf.q == self.accept:
            return conf
        elif conf.q == -1:
            return conf

        key = self.read(conf)

        if key not in self.transitions:
            conf.q = -1
            return conf

        transition = self.transitions[key]
        
        new_state   = transition[0]   
        new_symbols = transition[1]   
        movements   = transition[2]   

        self.write(conf, new_symbols)
        self.move(conf, movements)
        conf.q = new_state

        return conf 

    def run(self, conf: Config) -> None:
        """
        Given a Config, computes all Config until end of program (q = 1) and returns the last Config
        """
        pass

    def run_print(self, conf: Config) -> None:
        """
        Given a Config, computes all Config until end of program (q = 1) and returns the last Config
        Also prints out in a pretty manner how it works
        """
        pass

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
