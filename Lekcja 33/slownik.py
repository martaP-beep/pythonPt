# osoba = {
   
#     "imie": "Jan",
#     "nazwisko": "Kowalski",
#     "wiek": 20,
#     "adres": {
#         "ulica": "Gigantowa",
#         "numer": 5,
#         "miasto": "Pythonowo"
#     }


# }

# print(osoba)
# print(osoba["imie"])

# osoba["email"] = "jan@gmail.com"
# print(osoba)

# del osoba["imie"]
# print(osoba)


def sortowanie_babelkowe(lista):

    n = len(lista) # n - liczba elementów listy
    for i in range(n):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
              
    return lista

liczby = [2, 5, 1, 8, 0]
# print(sortowanie_babelkowe(liczby))

def wyszukiwanie_liniowe(lista, wartosc):
    for i in range(len(lista)):
        if lista[i] == wartosc:
            return i 
    return -1    
    
liczby = [2, 5, 1, 8, 0]
print(wyszukiwanie_liniowe(liczby, 8))
print(wyszukiwanie_liniowe(liczby, 15))