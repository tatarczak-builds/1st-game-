class Lokacja:
    def __init__(self, nazwa, opis):
        self.nazwa = nazwa
        self.opis = opis
        self.sciezki = {}
# to niżej łączy lokacje ze soba

    def dodaj_sciezke(self, kierunek, docelowalokacja):
        self.sciezki[kierunek] = docelowalokacja


def zbuduj_swiat():
    # tworzymy lokacje
    ludus = Lokacja("Szkoła Gladiatorów (Ludus)",
                    "Słychać tu brzęk mieczy i krzyki trenerów. Miejsce, gdzie sypiasz.")
    forum = Lokacja(
        "Forum Romanum", "Serce Rzymu. Gwarny rynek pełen kupców, senatorów i złodziei.")
    koloseum = Lokacja(
        "Koloseum", "Wielka arena. Piasek jest czerwony od krwi. Słychać ryk lwów.")
    katakumby = Lokacja(
        "Mroczne Katakumby", "Zimno tu i ciemno. Podobno kręcą się tu niebezpieczne typy...")
# łączymy je ze sobą
    ludus.dodaj_sciezke("brama", forum)

    forum.dodaj_sciezke("szkola", ludus)
    forum.dodaj_sciezke("arena", koloseum)
    forum.dodaj_sciezke("piwnica", katakumby)

    koloseum.dodaj_sciezke("targ", forum)

    katakumby.dodaj_sciezke("targ", forum)
# zwracamy początkową lokację
    return ludus
