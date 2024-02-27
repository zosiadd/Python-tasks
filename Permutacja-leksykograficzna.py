'''Permutacja to uporządkowany układ obiektów. Na przykład 3124 jest jedną z możliwych permutacji cyfr 1, 2, 3 i 4.
Jeśli wszystkie permutacje są wymienione numerycznie lub alfabetycznie, nazywamy to porządkiem leksykograficznym.
Permutacje leksykograficzne 0, 1 i 2 to: 012 021 102 120 201 210
Jaka jest milionowa permutacja leksykograficzna cyfr 0, 1, 2, 3, 4, 5, 6, 7, 8 i 9?

A permutation is an ordered arrangement of objects. For example, 3124 is one of the possible permutations of the digits 1, 2, 3 and 4.
If all permutations are listed numerically or alphabetically, this is called lexicographic order.
The lexicographic permutations of 0, 1 and 2 are: 012 021 102 120 201 210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?'''


# Importowanie funkcji factorial potrzebnej do obliczenia silni:
from math import factorial
'''Zdefiniowanie funkcji find_lexicographic_permutation z parametrami n i digits.
Odpowiedzialnej za znalezienie n-tej permutacji leksykograficznej na podstawie liczby n i zbioru cyfr:'''
def find_lexicographic_permutation(n, digits):
    result = []            # Utworzenie zmiennej result z pustą listą.
    digits = list(digits)  # Utworzenie listy cyfr z ciągów znaków w digits.

    n -= 1  # Indeksowanie od zera
    # Pętla iterująca do -1 elementu listy od odtatniej cyfry listy cyfr digits, po jednym kroku iteracji:
    for i in range(len(digits) - 1, -1, -1):
        index = n // factorial(i)             # Do zmiennej index przypisuje dzielenie n przez silnię z elementów listy digits.
        n %= factorial(i)                     # Aktualizuje wartość n, aby odzwierciedlić resztę po podzieleniu przez factorial(i).
        result.append(digits.pop(index))      # Do listy result dodawane są cyfry o indeksie index, cyfry te następnie są usuwane z listy digits.

    return ''.join(result)                    # Zwrócenie wyniku w formie ciągu znaków.


n = 1000000             # Zgodnie z poleceniem szukamy milionowej permutacji.
digits = "0123456789"   # Z cyfr 0123456789
result = find_lexicographic_permutation(n, digits)     # Wywołanie funkcji find_nth_lexicographic_permutation z ustalonymi wartościami n i digits.
print(f"Milionową permutacją leksykograficzną jest liczba: {result}")           # Wydrukowanie wyniku.
