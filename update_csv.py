import csv
import os
import random
from datetime import datetime
import pytz

# ============================================================
# NASTAVENÍ – upravte podle potřeby
# ============================================================
CSV_FILE = "Impulsy_ORCA.csv"   # cesta k CSV souboru v repozitáři

def generuj_radky():
    praha = pytz.timezone("Europe/Prague")
    dnes = datetime.now(praha).strftime("%Y.%m.%d %H:%M")
    
    hodnota = random.randint(100, 200)
    druh = random.choice(["Hotovost", "Platební karta", "Věrnostní karta"])
    
    return [{"Datum": dnes, "Hodnota": hodnota, "Druh platby": druh}]

# ============================================================
# Hlavní logika – neměňte
# ============================================================
def main():
    nove_radky = generuj_radky()
    
    soubor_existuje = os.path.isfile(CSV_FILE)
    
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        fieldnames = ["Datum", "Hodnota", "Druh platby"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        # Hlavička jen pokud soubor neexistuje
        if not soubor_existuje:
            writer.writeheader()
        
        for radek in nove_radky:
            writer.writerow(radek)
            print(f"Přidán řádek: {radek}")
    
    print(f"Hotovo! Přidáno {len(nove_radky)} řádků do {CSV_FILE}.")

if __name__ == "__main__":
    main()
