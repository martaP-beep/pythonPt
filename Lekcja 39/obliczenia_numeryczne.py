import numpy as np

tablica = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(tablica)
print(f"Pierwszy element: {tablica[0][0]}")
print(f"Typ danych: {type(tablica)} ")
print(f"Kształt: {tablica.shape}")

tablica = tablica.reshape(1,9)
print(f"Kształt: {tablica.shape}")
print(tablica)

tab2 = np.array([[1,2,3], [1.1, 2.2, 3.3], ["a", "b", "c"]], dtype="U")

print(tab2)

# np.random.randint(100)
print(np.random.choice([1,3,5,7,9]))

print(np.random.choice([1,3,5,7,9], p=[0.1, 0.3, 0.6, 0.0, 0.0], size =(3,5)))



tab3 = np.array([1,2,3,4,5])
print(f"Tablica przed przetasowaniem: {tab3}")

print(f"Tablica po przetasowaniu: {np.random.shuffle(tab3)}") # none

print(f"Tablica po przetasowaniu: {tab3}") # przetasowana tab

print(f"Permutacja: {np.random.permutation(tab3)}") # nowa przetasowana tablica

#Zadania 
#1.Stwórz listę o wymiarach 3x3 i wypełnij ją losowymi liczbami od 1 do 10
#2.Zmień rozmiar listy na 1x9
#3.Wybierz losową wartość z listy
#4.Przetasuj listę oraz stwórz jej permutacje

#1
tablica = np.random.choice([1,2,3,4,5,6,7,8,9,10], size=(3,3))
print(tablica)

#2
tablica = tablica.reshape(1,9)
print(tablica)

#3
liczba = np.random.choice(tablica[0])
print(liczba)

#4 
# zadanie domowe