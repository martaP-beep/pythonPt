# # krotka

# # krotka = (18, 21, 3, 12, 5, 3, 5, 3, 21, 22, 1)
# # print(krotka)
# # # wypisz element o indeksie 2 z krotki
# # print(krotka[2])

# # print(krotka[0:3])
# # krotka_jednoelementowa = (3,)
# # print(krotka_jednoelementowa)

# # # index - pod jakim indeksem znajduje się określona wartości
# # print(krotka.index(3))

# # # count - zliczenie elementów o danej wartości
# # print(krotka.count(3))

# # zbiór

# zbior = {3, 6, 1, 7, 2}
# print(zbior)
# zbior2 = set()
# print(zbior2)

# #dodawanie elementu
# zbior.add(13)
# print(zbior)

# # usuwanie elementu o podanej wartości
# zbior.remove(1)
# print(zbior)

# # usunięcie elementu jeżeli dany elemenet znajduje się w zbiorze
# zbior.discard(0)
# print(zbior)

# # usunięcie i zwrócenie elementu
# usuniety = zbior.pop()
# print(usuniety)
# print(zbior)

# # usunięcie wszystkich elementów
# zbior.clear()
# print(zbior)

# # konwersje pomiędzy strukturami
# zbior  = {1,2,3}
# krotka = (4,5,6)
# lista = [7,8,9,9]

# # zbiór -> lista

# print(list(zbior))
# print(type(list(zbior)))

# # krotka -> lista

# print(list(krotka))
# print(type(list(krotka)))

# # zbiór -> krotka

# print(tuple(zbior))
# print(type(tuple(zbior)))

# # lista -> krotka

# print(tuple(lista))
# print(type(tuple(lista)))

# # krotka -> zbior

# print(set(krotka))
# print(type(set(krotka)))

# # lista -> zbior

# print(set(lista))
# print(type(set(lista)))

# ctrl + /
# 1. Stwórz krotkę, listę, słownik i zbiór zawierający po 3 elementy

krotka = (1,2,3)
lista = [4,5,6]
slownik = {"klucz1": 7,
           "klucz2": 8,
           "klucz3": 9}
zbior = {10,11,12}
# 2. Za pomocą funkcji len() sprawdź długości 
# poszczególnych obiektów
print(len(lista))
print(len(zbior))
print(len(krotka))
print(len(slownik))
# 3. Za pomocą pętli for wypisz wszystkie elementy 
# każdego z obiektów
for i in slownik:
    print(i)
for i in lista:
    print(i)
for i in krotka:
    print(i)
for i in zbior:
    print(i)
# 4. Wypisz wartości słownika zamiast kluczy
for i in slownik.values():
    print(i)
# 5. Wypisz te same elementy w odwrotnej kolejności, 
# czy zawsze jest to możliwe bezpośrednio? 
# W razie problemów skorzystaj z pomocy chataGPT
# print("Lista")

# for i in lista[::-1]:
#     print(i)

# for i in krotka[::-1]:
#     print(i)

# for i in list(slownik)[::-1]:
#     print(i)
# for i in list(zbior)[::-1]:
#     print(i)

for i in reversed(krotka):
    print(i)

for i in reversed(lista):
    print(i)

for i in reversed(slownik):
    print(i)

for i in reversed(zbior):
    print(i)

# 6. Dodaj do listy elementy z krotki, zbioru i wartości słownika
lista.extend(zbior)


# 7. Dodaj do listy 2 liczby - wartość maksymalna i minimalna listy. 
# Do znalezienia największej i najmniejszej wartości 
# nie korzystaj z gotowych funkcji

# 8. Sprawdź długość listy

# 9.Zamień listę na krotkę - krotka2 i sprawdź jej długość.

# 10. Zamień krotkę na zbiór - zbior2 i sprawdź jego długość, 
# z czego wynika różnica?
