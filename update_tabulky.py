import csv
import random
from datetime import datetime
import pytz

IMPULSY_FILE = "Impulsy_ORCA.csv"
TABULKY_FILE = "Tabulky_2.csv"

def get_dnesni_datum():
    praha = pytz.timezone("Europe/Prague")
    return datetime.now(praha).strftime("%Y.%m.%d")

def nacti_impulsy(dnes):
    """Načte záznamy z Impulsy_ORCA.csv za dnešní den a sečte hodnoty podle druhu platby."""
    soucty = {}  # {"Hotovost": 150, "Platební karta": 300, ...}

    with open(IMPULSY_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            datum = row["Datum"][:10].replace("-", ".")  # normalizace na YYYY.MM.DD
            if datum == dnes:
                druh = row["Druh platby"].strip()
                hodnota = int(row["Hodnota"])
                soucty[druh] = soucty.get(druh, 0) + hodnota

    return soucty

def rozdel_na_boxy_prislusenstvi(celkova_hodnota):
    """Náhodně rozdělí hodnotu na Boxy a Příslušenství."""
    boxy = random.randint(0, celkova_hodnota // 10) * 10
    prislusenstvi = celkova_hodnota - boxy
    return boxy, prislusenstvi

def main():
    dnes = get_dnesni_datum()
    soucty = nacti_impulsy(dnes)

    if not soucty:
        print(f"Žádné záznamy pro dnešní datum {dnes} v {IMPULSY_FILE}.")
        return

    nove_radky = []
    for druh, celkem in soucty.items():
        boxy, prislusenstvi = rozdel_na_boxy_prislusenstvi(celkem)
        celkem_kontrola = boxy + prislusenstvi

        # Tržba: 0 pro Věrnostní kartu, jinak = Celkem
        trzba = 0 if druh == "Věrnostní karta" else celkem_kontrola

        nove_radky.append({
            "Přehled plateb": druh,
            "Boxy": boxy,
            "Příslušenství": prislusenstvi,
            "Celkem": celkem_kontrola,
            "Tržba": trzba,
            "Datum": dnes,
        })

    # Načti již existující záznamy pro dnešek
    existujici = set()
    try:
        with open(TABULKY_FILE, newline="", encoding="cp1252") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Datum"].strip() == dnes:
                    existujici.add(row["Přehled plateb"].strip())
    except FileNotFoundError:
        pass

    # Zapiš pouze řádky, které ještě neexistují
    with open(TABULKY_FILE, "a", newline="", encoding="cp1252") as f:
        fieldnames = ["Přehled plateb", "Boxy", "Příslušenství", "Celkem", "Tržba", "Datum"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        for radek in nove_radky:
            if radek["Přehled plateb"] in existujici:
                print(f"Přeskočen (již existuje): {radek['Přehled plateb']}")
                continue
            writer.writerow(radek)
            print(f"Přidán řádek: {radek}")

    print(f"Hotovo! Přidáno {len(nove_radky)} řádků do {TABULKY_FILE}.")

if __name__ == "__main__":
    main()import csv
import random
from datetime import datetime
import pytz

IMPULSY_FILE = "Impulsy_ORCA.csv"
TABULKY_FILE = "Tabulky_2.csv"

def get_dnesni_datum():
    praha = pytz.timezone("Europe/Prague")
    return datetime.now(praha).strftime("%Y.%m.%d")

def nacti_impulsy(dnes):
    """Načte záznamy z Impulsy_ORCA.csv za dnešní den a sečte hodnoty podle druhu platby."""
    soucty = {}  # {"Hotovost": 150, "Platební karta": 300, ...}

    with open(IMPULSY_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            datum = row["Datum"][:10].replace("-", ".")  # normalizace na YYYY.MM.DD
            if datum == dnes:
                druh = row["Druh platby"].strip()
                hodnota = int(row["Hodnota"])
                soucty[druh] = soucty.get(druh, 0) + hodnota

    return soucty

def rozdel_na_boxy_prislusenstvi(celkova_hodnota):
    """Náhodně rozdělí hodnotu na Boxy a Příslušenství."""
    boxy = random.randint(0, celkova_hodnota // 10) * 10
    prislusenstvi = celkova_hodnota - boxy
    return boxy, prislusenstvi

def main():
    dnes = get_dnesni_datum()
    soucty = nacti_impulsy(dnes)

    if not soucty:
        print(f"Žádné záznamy pro dnešní datum {dnes} v {IMPULSY_FILE}.")
        return

    nove_radky = []
    for druh, celkem in soucty.items():
        boxy, prislusenstvi = rozdel_na_boxy_prislusenstvi(celkem)
        celkem_kontrola = boxy + prislusenstvi

        # Tržba: 0 pro Věrnostní kartu, jinak = Celkem
        trzba = 0 if druh == "Věrnostní karta" else celkem_kontrola

        nove_radky.append({
            "Přehled plateb": druh,
            "Boxy": boxy,
            "Příslušenství": prislusenstvi,
            "Celkem": celkem_kontrola,
            "Tržba": trzba,
            "Datum": dnes,
        })

    with open(TABULKY_FILE, "a", newline="", encoding="cp1252") as f:
        fieldnames = ["Přehled plateb", "Boxy", "Příslušenství", "Celkem", "Tržba", "Datum"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        for radek in nove_radky:
            writer.writerow(radek)
            print(f"Přidán řádek: {radek}")

    print(f"Hotovo! Přidáno {len(nove_radky)} řádků do {TABULKY_FILE}.")

if __name__ == "__main__":
    main()
