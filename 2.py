liczba_produktow = int(input("Podaj liczbę produktów: "))
produkty = []
ceny = []

for i in range(liczba_produktow):
    produkt = input(f"Produkt {i+1}: ")
    cena = float(input(f"Cena: "))
    produkty.append(produkt)
    ceny.append(cena)

print("\n=== CENNIK ===")
for numer, (produkt, cena) in enumerate(zip(produkty, ceny), start=1):
    print(f"{numer}. {produkt} - {int(cena)} zł")

suma_cen = sum(ceny)
print(f"Suma cen: {int(suma_cen)} zł")

max_cena = max(ceny)
max_index = ceny.index(max_cena)
najdrozszy_produkt = produkty[max_index]
print(f"Najdrozszy produkt: {najdrozszy_produkt} - {int(max_cena) } zł")
