# 1. Stwórz 2 listy zawierające po 3 liczby. 
# 2. Połącz stworzone wcześniej listy.
# 3. Usuń elementy z indeksami 2 i 5 , który element należy usunąć najpierw?
# 4. Usuń największą i najmniejszą liczbę z listy - NIE UŻYWAJ GOTOWYCH FUNKCJI MIN I MAX
# 5. Dodaj dowolną liczbę do listy
# 6. Posortuj listę
# 7. Utwórz kopię listy
# 8. Odwróć kolejność elementów w kopii
# 9. Dodaj do każdej wartości w pierwszej liście 1, a w drugiej odejmij 1
# 10. Wyświetl obie listy
# komentarz skrót ctrl + /

lista1 = [1,2,3]
lista2 = [4,5,6]



lista1.extend(lista2)
print(lista1)
# zad 3
usuwany_element_5 = lista1.pop(5)
print(usuwany_element_5)
print(lista1)
usuwany_element_2 = lista1.pop(2)
print(usuwany_element_2)
print(lista1)

# print(lista1)