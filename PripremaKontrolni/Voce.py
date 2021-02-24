
        class Voce:
        def __innit__(self, voce_id, naziv, tip_voca, korpa):
        self.voce_id=voce_id
        self.naziv=naziv
        self.tip_voca=tip_voca
        self.korpa=korpa
        def __str__(self):
            return f"id {self.voce_id}", f"naziv {self.naziv}", f"tip {self.tip_voca}", f"korpa {self.korpa}"


