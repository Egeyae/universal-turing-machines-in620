class MT:
    def ___init___(self,nom,nb_etat, liste_d_etat,nombre_ruban,liste_transi,mot):
        self.nom = nom
        self.nb_etat = nb_etat
        self.liste_etat = liste_d_etat
        self.nb_ruban = nombre_ruban
        self.liste_transi = liste_transi

class Config:
    def ___init___(self, before, under, q):   
        self.before = before
        self.under = under
        self.q = q