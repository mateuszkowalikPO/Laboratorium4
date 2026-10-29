prog_alarmowy = 50

ilosc_pomiarow = int(input("Podaj liczbe pomiarow: "))
pomiary = []

for i in range(ilosc_pomiarow):
    pomiar = int(input(f"Pomiar {i + 1}: "))
    pomiary.append(pomiar)

pomiary_alarmowe = [x for x in pomiary if x > prog_alarmowy]
pomiary_podwojone = [x * 2 for x in pomiary]

czy_alarm = any(x > prog_alarmowy for x in pomiary)
czy_wszystkie_prawidlowe = all(x <= prog_alarmowy for x in pomiary)

print(f"\nPomiary alarmowe: {pomiary_alarmowe}")
print(f"Pomiary pomnozone przez 2: {pomiary_podwojone}")
print(f"Czy wystapil alarm? {'Tak' if czy_alarm else 'Nie'}")
print(f"Czy wszystkie pomiary sa prawidlowe? {'Tak' if czy_wszystkie_prawidlowe else 'Nie'}")
