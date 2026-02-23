class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeus):
        if nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        elif nopeus < 0:
            self.nykyinen_nopeus = 0
        else:
            self.nykyinen_nopeus = nopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nykyinen_nopeus * tunnit

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko

sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttoauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdytä(120)
polttoauto.kiihdytä(110)

sahkoauto.kulje(3)
polttoauto.kulje(3)

print("Sähköauto, matkamittari:", sahkoauto.kuljettu_matka, "km")
print("Polttomoottoriauto, matkamittari:", polttoauto.kuljettu_matka, "km")
