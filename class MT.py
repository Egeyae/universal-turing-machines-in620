class MT:
    def __init__(self,name,nb_states, state_list,nb_tapes,transi_list):
        self.name = name
        self.nb_state = nb_states
        self.state_list = state_list
        self.nb_tapes = nb_tapes
        self.transi_list = transi_list

    def __str__(self):
        s =f"Name : {self.name} \n"
        s += f"Number of states : {self.nb_states} \n"
        for i in range(len(self.state_list)):
            s += f"\t - {self.state_list[i]}"
        s += f"Number of tape.s : {self.nb_tapes} \n"
        for i in range(len(self.transi_list)):
            s+= f"\t - {self.transi_list[i]} \n"
        return s

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
