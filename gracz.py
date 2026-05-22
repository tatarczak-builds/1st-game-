from itemki import Bron, Pancerz


class Gracz:
    def __init__(self, imie, maks_hp, atk, zwinnosc):
        self.imie = imie
        self.max_hp = maks_hp
        self.hp = maks_hp
        self.atk = atk
        self.zwinnosc = zwinnosc

        self.zloto = 100
        self.chwala = 0

        self.lvl = 1
        self.exp = 0
        self.exp_do_awansu = 100

        self.walki_na_arenie = 0
        self.przechodzien = False

        self.ekwipunek = []

    def statystyki(self):
        print("\n" + "="*30)
        print(f" Twoja postać: {self.imie.upper()} (Poziom {self.lvl})")
        print(f" HP: {self.hp}/{self.max_hp}")
        print(f" Atak: {self.atk}  |  Zwinność: {self.zwinnosc}")
        print(f" Złoto: {self.zloto} | Chwała: {self.chwala}")
        print(f" EXP: {self.exp}/{self.exp_do_awansu}")

        itemy_plecak = []
        for przedmiot in self.ekwipunek:
            itemy_plecak.append(przedmiot.nazwa)
        print(f" Ekwipunek: {itemy_plecak}")
        print("="*30 + "\n")

    def dodaj_exp(self, ilosc):
        self.exp += ilosc
        print(f"\nZdobyłeś {ilosc} EXP!")
        # pętla gdyby dostal expa ze awansuje np o 2 poziomy
        while self.exp >= self.exp_do_awansu:
            self.awansuj()

    def awansuj(self):
        self.lvl += 1  # dodanie levela
        self.exp -= self.exp_do_awansu  # odjecie zuzytych punktow
        # int zeby byla cala liczba a nie np 225,25
        self.exp_do_awansu = int(self.exp_do_awansu * 1.5)

        # przyrost statystyk przy awansie
        self.max_hp += 20
        self.hp = self.max_hp  # leczenie do pełna przy awansie
        self.atk += 2
        self.zwinnosc += 2

        print(
            f"\n*** AWANS! Osiągasz {self.lvl} poziom! Twoje statystyki rosną. ***\n")


# klasy gladiatorów
class Thraex(Gracz):
    # srednie hp, duzy atak, srednia zwinnosc
    def __init__(self, imie):
        super().__init__(imie, maks_hp=20, atk=8, zwinnosc=5)


class Mirmillon(Gracz):
    # duze hp, sredni atak, mala zwinnosc
    def __init__(self, imie):
        super().__init__(imie, maks_hp=30, atk=6, zwinnosc=3)


class Retiarius(Gracz):
    # male hp, duzy atak, bardzo duza zwinnosc(zawsze zazcyna)
    def __init__(self, imie):
        super().__init__(imie, maks_hp=15, atk=10, zwinnosc=8)
