
        class Korpa:
            def __innit__(self, korpa_id, voce=[], brojj, brojv, brojm):
            self.korpa_id=korpa_id
            self.voce=voce
            self.brojj=brojj
            self.brojv=brojv
            self.brojm=brojm



            def __str__(self):
                return f"korpa_id {self.korpa_id}", f"voce {self.voce}", f"brojj {self.brojj}", f"brojv {self.brojv}", f"brojm {self.brojm}"

            def __add__(self, other):


            def __sub__(self, other):