warsztat_python = set()
warsztat_ai = set()

while True:
    print("\n1. Zapisz na Python")
    print("2. Zapisz na AI")
    print("3. Wyswietl uczestnikow")
    print("4. Uczestnicy obu warsztatow")
    print("5. Wszyscy unikalni uczestnicy")
    print("0. Zakoncz")

    wybor = int(input("Wybierz opcje: "))

    if wybor == 0:
        break

    elif wybor == 1:
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        uczestnik = (imie, nazwisko)
        warsztat_python.add(uczestnik)

    elif wybor == 2:
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        uczestnik = (imie, nazwisko)
        warsztat_ai.add(uczestnik)

    elif wybor == 3:
        print("Python:")
        for imie, nazwisko in warsztat_python:
            print(f"- {imie} {nazwisko}")
        print("AI:")
        for imie, nazwisko in warsztat_ai:
            print(f"{imie} {nazwisko}")

    elif wybor == 4:
        print("Oba warsztaty:")
        for imie, nazwisko in (warsztat_python & warsztat_ai):
            print(f"{imie} {nazwisko}")

    elif wybor == 5:
        print("Wszyscy:")
        for imie, nazwisko in (warsztat_python | warsztat_ai):
            print(f"{imie} {nazwisko}")


    else:
        print("Nieprawidlowy wybor, spróbuj ponownie.")
