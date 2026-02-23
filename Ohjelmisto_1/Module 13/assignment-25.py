class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nykyinen_nopeus += muutos
        if self.nykyinen_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        elif self.nykyinen_nopeus < 0:
            self.nykyinen_nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nykyinen_nopeus * tunnit

auto = Auto("ABC-123", 142)
auto.kuljettu_matka = 2000
auto.nykyinen_nopeus = 60

auto.kulje(1.5)

print("Kuljettu matka:", auto.kuljettu_matka, "km")
