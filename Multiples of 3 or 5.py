'''
Jeśli wymienimy wszystkie liczby naturalne poniżej 10 które są wielokrotnościami  5 lub 3 otrzymamy 3,5,6 i 9.
Suma tych wielokrotności wynosi 23. Znajdź sumę wszystkich wielokrotności liczby 3 lub 5 poniżej 1000.

If we list all the natural numbers below  10 that are multiples of  5 or 3, we get 3 ,5 ,6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
'''

numbers_list = []                     # Tworzę zmienną numbers_list z póstą listą.
for i in range(0, 1000):              # Iteruję po elementach od  0 do.
    if i % 5 == 0 or i % 3 == 0:      # Tworzę warunek jeżeli i jest podzielne bez reszty przez 5 lub przez 3.
        numbers_list.append(i)        # Dodaję i do listy numbers_list

summary = sum(numbers_list)           # Tworzę zmienną do której przypiszę sumę z numbers_list.

print(f"Sumą wszystkich wielokrotności liczby 5 lub 3 poniżej 1000 jest: {summary}")         # Drukuje wynik

