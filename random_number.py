# Prośba o podanie górnej granicy przedziału od użytkownika
gorna_granica = int(input("Podaj górną granicę przedziału liczb całkowitych: "))

# Wyświetlenie parzystych liczb w przedziale
print(f"Parzyste liczby w przedziale od 0 do {gorna_granica} to:")

for liczba in range(gorna_granica + 1):
    if liczba % 2 == 0:
        print(liczba)
