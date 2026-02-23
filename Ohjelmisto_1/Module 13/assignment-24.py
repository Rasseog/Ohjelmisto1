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

auto = Auto("ABC-123", 142)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print("Nopeus kiihdytysten jälkeen:", auto.nykyinen_nopeus, "km/h")

auto.kiihdytä(-200)

print("Nopeus hätäjarrutuksen jälkeen:", auto.nykyinen_nopeus, "km/h")
