
liczba_pomiarow = int(input("Ile pomiarow chcesz wprowadzic?: "))
pomiary = []
for i in range(liczba_pomiarow):
    pomiar = int(input(f"Pomiar {i+1}: "))
    pomiary.append(pomiar)

print(f"Pierwszy pomiar: {pomiary[0]}")
print(f"Ostatni pomiar: {pomiary[-1]}")

print(f"Pierwsze trzy: {pomiary[:3]}")
print(f"Ostatnie trzy: {pomiary[-3:]}")

print(f"Co drugi pomiar: {pomiary[::2]}")
print(f"Odwrocona lista: {pomiary[::-1]}")

print(f"Oryginal: {pomiary}")

kopia = pomiary.copy()
kopia[0] = 0

print(f"Oryginal: {pomiary}")
print(f"Kopia po zmianie: {kopia}")


