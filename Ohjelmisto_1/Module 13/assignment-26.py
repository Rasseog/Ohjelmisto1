import random

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

autot = []

for i in range(1, 11):
    rekisteri = f"ABC-{i}"
    huippu = random.randint(100, 200)
    autot.append(Auto(rekisteri, huippu))

while True:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_paattyi = True
            break
    else:
        kilpailu_paattyi = False

    if kilpailu_paattyi:
        break

print(f"{'Rekisteri':<8} {'Huippu':>6} {'Nopeus':>6} {'Matka':>10}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<8} {auto.huippunopeus:>6} {auto.nykyinen_nopeus:>6} {auto.kuljettu_matka:>10.1f}")
