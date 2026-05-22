class Przedmiot:
    def __init__(self, nazwa, cena, efekt="", wymagany_lvl=1):
        self.nazwa = nazwa
        self.cena = cena
        self.efekt = efekt
        self.wymagany_lvl = wymagany_lvl


class Bron(Przedmiot):
    def __init__(self, nazwa, cena, bonus_atak, wymagany_lvl=1):
        super().__init__(nazwa, cena, wymagany_lvl=wymagany_lvl)
        self.bonus_atak = bonus_atak


class Pancerz(Przedmiot):
    def __init__(self, nazwa, cena, bonus_hp, wymagany_lvl=1):
        super().__init__(nazwa, cena, wymagany_lvl=wymagany_lvl)
        self.bonus_hp = bonus_hp

# Przedmioty in game


wszystkie_przedmioty = [
    # lvl1
    Bron("Pordzewiały gladius", 10, bonus_atak=4, wymagany_lvl=1),
    Pancerz("Skórzana Zbroja", 15, bonus_hp=10, wymagany_lvl=1),
    # lvl2
    Bron("Stalowy miecz", 50, bonus_atak=10, wymagany_lvl=2),
    Pancerz("Kolczuga", 75, bonus_hp=20, wymagany_lvl=2),
    # lvl3
    Bron("Trójząb czempiona", 200, bonus_atak=20, wymagany_lvl=3),
    Pancerz("Zbroja z Koloseum", 300, bonus_hp=50, wymagany_lvl=3),
    # lvl5
    Bron("Miecz boga wojny", 700, bonus_atak=50, wymagany_lvl=5),
    Pancerz("Zbroja nieśmiertelności", 800, bonus_hp=100, wymagany_lvl=5)
]


def oferta_sklepu(gracz):
    oferta = []
    for przedmiot in wszystkie_przedmioty:
        if gracz.lvl >= przedmiot.wymagany_lvl:
            oferta.append(przedmiot)
    return oferta


class Handlarz():
    def __init__(self, imie, oferta):
        self.imie = imie
        self.oferta = oferta
    # ====kupowanie przez gracza====

    def kupowanie(self, gracz, przedmiot):
        wybrany_item = None
        for item in self.oferta:
            if item.nazwa.lower() == przedmiot.nazwa.lower():
                wybrany_item = item
                break

        if wybrany_item:
            if gracz.zloto >= wybrany_item.cena:
                # kupić item
                gracz.zloto -= wybrany_item.cena
                gracz.ekwipunek.append(wybrany_item)
                print("\nŚwietny wybór! Ten przedmiot na pewno pomoże Ci w walce!")

                # dodać statystyki
                if isinstance(wybrany_item, Bron):
                    gracz.atk += wybrany_item.bonus_atak
                    print(
                        f"Twój atak wzrasta o {wybrany_item.bonus_atak}! (Obecny atak: {gracz.atk})")
                elif isinstance(wybrany_item, Pancerz):
                    gracz.hp += wybrany_item.bonus_hp
                    gracz.max_hp += wybrany_item.bonus_hp
                    print(
                        f"Twoje HP wzrasta o {wybrany_item.bonus_hp}! (Obecne HP: {gracz.hp}/{gracz.max_hp})")

            else:
                print(
                    f"\nHandlarz krzywi się: 'Nie stać Cię, biedaku! Potrzebujesz {wybrany_item.cena}g.'")

        else:
            print("\nHandlarz dziwi się: 'Nie mam nawet takiego przedmiotu w ofercie?!'")

    # ====sprzedawanie przez gracza====
    def sprzedawanie(self, gracz, nazwa_przedmiotu):
        wybrany_przedmiot = None
        for przedmiot in gracz.ekwipunek:
            if przedmiot.nazwa.lower() == nazwa_przedmiotu.lower():
                wybrany_przedmiot = przedmiot
                break
        if wybrany_przedmiot:
            # sprzedać item
            gracz.ekwipunek.remove(wybrany_przedmiot)
            cena_sprzedazy = wybrany_przedmiot.cena // 2
            gracz.zloto += cena_sprzedazy
            print(
                f"\nSprzedano {wybrany_przedmiot.nazwa} za {cena_sprzedazy} sztuk złota.")

            # cofnąć bonusy ze statystyk
            if isinstance(wybrany_przedmiot, Bron):
                gracz.atk -= wybrany_przedmiot.bonus_atak
            elif isinstance(wybrany_przedmiot, Pancerz):
                gracz.max_hp -= wybrany_przedmiot.bonus_hp
                if gracz.hp > gracz.max_hp:
                    gracz.hp = gracz.max_hp
            print(
                f"\n{self.imie} wręcza Ci {cena_sprzedazy} sztuk złota za {wybrany_przedmiot.nazwa}.")
        else:
            print(
                "\nHandlarz patrzy na ciebie jak na świra: 'Przecież nie masz takiego przedmiotu w plecaku!'")
