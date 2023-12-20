import random

# Generowanie losowej liczby całkowitej od 1 do 100
wylosowana_liczba = random.randint(1, 100)

# Prośba o zgadnięcie liczby od użytkownika
print("Zgadnij liczbę od 1 do 100:")
zgadywana_liczba = int(input())

# Pętla while do obsługi zgadywania
while zgadywana_liczba != wylosowana_liczba:
    if zgadywana_liczba > wylosowana_liczba:
        print("Za duża! Spróbuj ponownie.")
    else:
        print("Za mała! Spróbuj ponownie.")
    
    # Prośba o ponowne zgadnięcie
    zgadywana_liczba = int(input())

# Wyświetlenie komunikatu o poprawnym zgadnięciu
print(f"Brawo! Zgadłeś liczbę {wylosowana_liczba}!")

