liczby = [1,2,3,4,5,6,7,8,9,10]
wyniki = []
for i in range(len(liczby)):
    wyniki.append(liczby[i]**2)
# print(wyniki)

# wyniki = []
# for i in liczby:
#     wyniki.append(i**2)
# print(wyniki)
# kwadraty = [i**2 for i in liczby]
# print(kwadraty)

# kwadraty = {i**2 for i in liczby}
# print(kwadraty)

# kwadraty = {i:i**2 for i in liczby}
# print(kwadraty)

# kwadraty = tuple(i**2 for i in liczby)
# print(kwadraty)

# kwadraty = [i**2 for i in liczby if i % 2 == 0]
# print(kwadraty)

panstwa = ["Polska", "Niemcy", "Francja", "Hiszpania"]
stolice = ["Warszawa", "Berlin", "Paryz", "Madryt"]

tekst = [f"{stolica} to stolica: {panstwo}" for panstwo, stolica in zip(panstwa, stolice)]

# print(tekst)

# Zadanie 1
# Na podstawie podanej listy 
slowa = ["ala", "kot", "pies", "kamilslimak",
"zebra", "madam", "Adam"] 
# stwórz listę zawierającą same palindromy
# (wyrażenie brzmiące tak samo czytane od lewej do prawej 
# i od prawej do lewej).

# palindromy = [slowo for slowo in slowa if slowo == slowo[::-1]]
# print(palindromy)

def dzielenie(a, b):
    try:
        a/b
        if a < 0 or b < 0 :
            raise Exception("To nie są liczby dodatnie")
    except Exception as e:
        print(e)
    else:
        print(f"Wynik dzielenia {a} przez {b} to {a/b}")
    finally:
        print("koniec funkcji")

dzielenie(5, 0)

# Zadanie 2 
# Z listy krotek zawierającej długości odcinków 
# stwórz listę zawierającą tylko te krotki, z których 
# można skonstruować trójkąt 
# (warunek - najdłuższy bok musi być krótszy niż suma 
#  dwóch pozostałych).

odcinki = [(1, 3, 5), (2, 2, 3), (3, 1, 8), (3, 4, 5)]