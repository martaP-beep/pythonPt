lista = [2, 4, 1, "kot", 4.2, True, 4/2]

print(lista)

# append - dodawanie nowego elementu
lista.append(13)
print(lista)

# extend - rozszerzenie listy
lista.extend(["pies", 9, 3.13])
print(lista)

# insert - dodawanie elementu pod konkretny indeks
lista.insert(3, "nowy")
print(lista)

# remove - usuwa pierwsze wystąpienie elementu o konkretnej wartości
lista.append(1)
print(lista)
lista.remove(1)
print(lista)

# pop - usuwa element z konkretnego indeksu i go zwraca
usuniety_element = lista.pop(4)
print(lista)
print(f"Usunięty element {usuniety_element}")

# index - zwraca indeks pierwszego znalezionego elementu
lista.append(4)
print(lista)
indeks = lista.index(4)
print(f"Indeks: {indeks}")
print(lista)

# indeks - zwraca indeks pierwszego znalezionego elementu, przeszukując od indeksu 3
indeks = lista.index(4, 3)
print(indeks)

# indeks - zwraca indeks pierwszego znalezionego elementu, przeszukując od indeksu 0 do 2
indeks = lista.index(4, 0, 3)
print(indeks)

# count - zwraca liczbę wystąpień danej wartości w liście
licznik = lista.count(4)
print(licznik)

# sort - sortowanie listy
# najpierw usuwamy elementy innego typu niż liczby
lista.remove("nowy")
lista.remove("kot")
lista.remove("pies")
lista.sort()
print(lista)

# reverse - odwraca kolejność elementó listy
lista.reverse()
print(lista)

# copy - stworzenie kopii listy

kopia_listy = lista.copy()
print(lista)
print(kopia_listy)

lista.append(111)
print(lista)
print(kopia_listy)

# clear - czyszczenie listy
lista.clear()
print(lista)

