import csv
import os
from datetime import date

# ============================================================
# NASTAVENÍ – upravte podle potřeby
# ============================================================
CSV_FILE = "Impulsy_ORCA.csv"   # cesta k CSV souboru v repozitáři

def generuj_radky():
    """
    Vrať seznam nových řádků, které se přidají do CSV.
    Každý řádek je slovník s klíči: Datum, Hodnota, Druh platby
    
    Tuto funkci upravte podle vaší logiky výpočtu!
    """
    dnes = date.today().strftime("%Y-%m-%d")
    
    # PŘÍKLAD – nahraďte vlastní logikou:
    nove_radky = [
        {"Datum": dnes, "Hodnota": 150, "Druh platby": "Karta"},
        # {"Datum": dnes, "Hodnota": 200, "Druh platby": "Hotovost"},
    ]
    return nove_radky

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
