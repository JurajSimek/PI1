max_bodov = 30

#funkcia na ziskanie validneho počtu bodov 
def ziskaj_pocet_bodov():
    while True: # nekonečný cyklus 
        try:
            pocet_bodov = int(input(f"Zadaj pocet bodov (0 - {max_bodov}): "))
            if 0 <= pocet_bodov <= max_bodov:
                return pocet_bodov
            else:
                print(f"Počet bodov musí byť v rozsaho od 0 po {max_bodov}. Daj ešte raz!")
        except ValueError:
            print("Neplatný vstup! Zadaj celé číslo")

def vypocitaj_percenta(pocet_bodov):
    return round((pocet_bodov / max_bodov) * 100, 2)

def klasifikacia(percenta):
    if percenta >= 90:
        return "Dostavas znamku jedna"
    elif percenta <= 75:
        return"Dostavas znamku dva"
    elif percenta <= 50:
        return"Dostavas znamku tri"
    elif percenta <= 30:
        return"Dostavas znamku štyri"
    else:
        return"Dostavas znamku pät"

pocet_bodov = ziskaj_pocet_bodov()
percenta = vypocitaj_percenta(pocet_bodov)
hodnotenie = klasifikacia(percenta)
print(f"Počet bodov: {pocet_bodov}, percenta: {percenta}%, Hodnotenie: {hodnotenie}")