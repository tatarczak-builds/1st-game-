from itemki import Bron, Pancerz, oferta_sklepu, Handlarz, wszystkie_przedmioty
import itemki
from lokacje import zbuduj_swiat
from gracz import Gracz, Thraex, Mirmillon, Retiarius
from walka import walka


def kreator_postaci():
    print("------- STWÓRZ SWOJĄ POSTAĆ ------\n")
    imie = input("Podaj imię swojego bohatera: ")

    print("\nWybierz klasę gladiatora:")
    print("1. Thraex (Agresywny) - Duże obrażenia, średnie HP i zwinność")
    print("2. Mirmillon (Ciężkozbrojny) - Duże HP i mała zwinność")
    print("3. Retiarius (Sieciaż) - Małe HP, duże obrażenia i bardzo duża zwinność")
# wybor klasy gladiatora
    while True:
        wybor = input("Jakim gladiatorem chcesz być? (1-3): ")
        if wybor == "1":
            return Thraex(imie)
        elif wybor == "2":
            return Mirmillon(imie)
        elif wybor == "3":
            return Retiarius(imie)
        else:
            print("\nNieprawidłowy wybór. Proszę wybrać klasę gladiatora (1-3).")


def start_gierki():
    # przywitanie
    print("\n============ WITAJ W STAROŻYTNYM RZYMIE! ============\n")
    print("Jako niewolnik zostałeś przewieziony do Rzymu, by walczyć na arenie.")
    print("Twoim celem jest przetrwać i zdobyć wolność, stając się legendarnym gladiatorem!\n")

# tworzenie gracza i świat
    gracz = kreator_postaci()
    obecna_lokacja = zbuduj_swiat()
    handlarz = Handlarz("Kupiec Binjamin", wszystkie_przedmioty)

    # menu główne
    while True:
        print(
            f"\n-----------------------------Jesteś teraz w: {obecna_lokacja.nazwa}-----------------------------")
        print(obecna_lokacja.opis)
        print("\nCo chcesz zrobić?")
# ------------------------------------------------OPCJE------------------------------------------------
        for kierunek in obecna_lokacja.sciezki.keys():
            print(f"- idz {kierunek}")

    # specjalne activity w danych lokacjach
        # =-=-=-=-=-=-=->LUDUS<-=-=-=-=-=-=-
        if obecna_lokacja.nazwa == "Szkoła Gladiatorów (Ludus)":
            print("- trenuj (Koszty: -2HP, +1 Atak, +1 Zwinność)")
            print("- odpocznij (+5 HP)")
            print("- wykup (Wymagane: 1000g. To twoja szansa na wolność!)")

        # =-=-=-=-=-=-=->FORUM<-=-=-=-=-=-=-
        elif obecna_lokacja.nazwa == "Forum Romanum":
            print("- oferta (Zobacz, co ma do zaoferowania kupiec Binjamin)")
            print(
                "- kup (Otwiera sklep z bronią i pancerzami. Im wyższy poziom, tym lepsze przedmioty!)")
            print("- sprzedaj (Odsprzedaj swoje przedmioty)")

        # =-=-=-=-=-=-=->KOLOSEUM<-=-=-=-=-=-=-
        elif obecna_lokacja.nazwa == "Koloseum":
            print(
                "- walcz (Stajesz do walki na arenie! Im silniejszy przeciwnik, tym większe nagrody!)")

        # =-=-=-=-=-=-=->KATAKUMBY<-=-=-=-=-=-=-
        elif obecna_lokacja.nazwa == "Mroczne Katakumby":
            # TU BEDZIE FABULA KATAKUMB
            pass

        print("- sprawdz statystyki")
        print("- koniec gry (aby zakończyć)")
# ------------------------------------------------DZIAŁANIA------------------------------------------------
    # bierzemy wpisaną komendę i zmieniamy ją na małe litery
        komenda = input("\n>>>Twój wybór: ").lower()
        if komenda.startswith("idz "):
            # wyciągamy kierunek z komendy(brany tekst od 4 znaku)
            kierunek = komenda[4:]
            if kierunek in obecna_lokacja.sciezki:
                obecna_lokacja = obecna_lokacja.sciezki[kierunek]
            else:
                print("\nNie możesz iść w tym kierunku! Wybierz inną opcję.\n")

        elif komenda == "sprawdz statystyki":
            gracz.statystyki()
        elif komenda == "koniec gry":
            print("\nBogowie Rzymu żegnają Cię. Do zobaczenia!\n")
            break  # przerywa pętlę i kończy program

        # ======LUDUS========
        elif komenda == "trenuj" and obecna_lokacja.nazwa == "Szkoła Gladiatorów (Ludus)":
            gracz.hp -= 2
            gracz.atk += 1
            gracz.zwinnosc += 1
            print(
                f"\nUderzasz w manekina treningowego do utraty tchu. Tracisz 1 HP, ale Twoja siła rośnie! (Obecna siła: {gracz.atk})")

            if gracz.hp <= 0:
                print(
                    "\nIgnorujesz ból i trenujesz dalej. Nagle w klatce piersiowej czujesz ostre kłucie...")
                print("Przetrenowałeś się! Padasz martwy na piasek w Ludusie.")
                print("\n--- KONIEC GRY ---")
                break  # KONIEC GRY ZŁE ZAKOŃCZENIE
            else:
                # jesli więcej niż 0 hp gra toczy się dalej
                print(
                    f"\nTrening przynosi efekty! Twoje umiejętności rosną, ale jesteś trochę zmęczony. (Obecne HP: {gracz.hp}/{gracz.max_hp})")

        elif komenda == "odpocznij" and obecna_lokacja.nazwa == "Szkoła Gladiatorów (Ludus)":
            if gracz.hp >= gracz.max_hp:
                print("\nJesteś już w pełni sił! Nie potrzebujesz odpoczynku.")
            else:
                gracz.hp += 5
                print(
                    f"\nOdpoczynek dodaje Ci sił. Czujesz się lepiej! (Obecne HP: {gracz.hp}/{gracz.max_hp})")

        elif komenda == "wykup" and obecna_lokacja.nazwa == "Szkoła Gladiatorów (Ludus)":
            if gracz.zloto >= 1000:
                print(
                    "\nZłoto lśni w Twoich dłoniach, gdy przekazujesz je strażnikowi. On kiwa głową i otwiera bramę...")
                print("Gratulacje! Udało Ci się wykupić wolność! Jesteś teraz wolnym człowiekiem, gotowym na nowe przygody poza areną!")
                print("\n--- KONIEC GRY ---")
                break  # KONIEC GRY DOBRE ZAKOŃCZENIE
            else:
                print(
                    "\nNie masz wystarczająco złota, aby się wykupić. Musisz zdobyć więcej, walcząc na arenie i zbierając łupy!")

        # ========TARG========
        elif komenda == "oferta" and obecna_lokacja.nazwa == "Forum Romanum":
            oferta = oferta_sklepu(gracz)
            print("\nOferta sklepu:")
            print("-" * 20)
            for przedmiot in oferta:
                print(
                    f">{przedmiot.nazwa} (Cena: {przedmiot.cena} zł, Wymagany lvl: {przedmiot.wymagany_lvl})")

        elif komenda.startswith("kup") and obecna_lokacja.nazwa == "Forum Romanum":
            # wyciągamy nazwę przedmiotu z komendy
            nazwa_przedmiotu = komenda[4:]
            oferta = oferta_sklepu(gracz)
            znaleziony_przedmiot = None
            # szukanie itema na liscie
            for przedmiot in oferta:
                if przedmiot.nazwa.lower() == nazwa_przedmiotu.lower():
                    znaleziony_przedmiot = przedmiot
                    break
            # jak znaleziony to kupic
            if znaleziony_przedmiot:
                handlarz.kupowanie(gracz, znaleziony_przedmiot)
            else:
                print(
                    "\nHandlarz krzywi się: 'Nie mam nawet takiego przedmiotu w ofercie?!'")

        elif komenda.startswith("sprzedaj") and obecna_lokacja.nazwa == "Forum Romanum":
            # wyciągamy nazwę przedmiotu z komendy
            nazwa_przedmiotu = komenda[8:]
            handlarz.sprzedawanie(gracz, nazwa_przedmiotu)

        # ========ARENA========
        elif komenda == "walcz" and obecna_lokacja.nazwa == "Koloseum":
            walka(gracz)

        # error alert
        else:
            print(
                "\nNieznana komenda!\n")


if __name__ == "__main__":
    start_gierki()
