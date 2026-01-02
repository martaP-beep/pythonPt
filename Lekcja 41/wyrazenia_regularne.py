import re

napis = "Ala ma kota"

# wynik = re.match(r"Ala", napis)
# print(f"Wyszukiwanie Ala: {wynik}")

# wynik = re.match(r"Kamil", napis)
# print(f"Wyszukiwanie Kamil: {wynik}")

# wynik = re.match(r"kota", napis)
# print(f"Wyszukiwanie kota: {wynik}")

# wynik = re.match(r"ala", napis, re.IGNORECASE)
# print(f"Wyszukiwanie ala: {wynik}")

# napis = "Ala ma 3 Koty i 2 psy"
# wynik = re.search(r"\d+", napis)
# print(f"Wyszukiwanie liczby: {wynik}")

# wynik = re.findall(r"\b[A-Z][a-z]+", napis)
# print(f"Wyszukiwanie wyrazów zapisanych z wielkiej litery: {wynik}")

# wzorzec = "Koty"
# zamiana = "chomiki"
# wynik = re.sub(wzorzec, zamiana, napis)
# print(wynik)

# match, search, findall, sub
#1 Sprawdz czy w tekscie "Uczę się programowania w języku python3" występuje cyfra

wzorzec = r"\d"
napis = "Uczę się programowania w języku python3"
wynik = re.search(wzorzec, napis)
# if wynik is not None:
#     print("W tekście jest cyfra")
# else:
#     print("W tekście nie ma cyfry")

#2 Znajdź wszystkie daty w tekście "Juliusz Słowacki herbu Leliwa (ur. 4 września 1809 w Krzemieńcu, zm. 3 kwietnia 1849 w Paryżu[1]) – polski poeta, dramaturg i epistolograf. Obok Adama Mickiewicza i Zygmunta Krasińskiego określany jako jeden z polskich wieszczów narodowych. Twórca filozofii genezyjskiej (pneumatycznej), epizodycznie związany z mesjanizmem polskim, był też mistykiem. Obok Adama Mickiewicza uznawany powszechnie za największego przedstawiciela polskiego romantyzmu."

napis = "Juliusz Słowacki herbu Leliwa (ur. 4 września 1809 w Krzemieńcu, zm. 3 kwietnia 1849 w Paryżu[1]) – polski poeta, dramaturg i epistolograf. Obok Adama Mickiewicza i Zygmunta Krasińskiego określany jako jeden z polskich wieszczów narodowych. Twórca filozofii genezyjskiej (pneumatycznej), epizodycznie związany z mesjanizmem polskim, był też mistykiem. Obok Adama Mickiewicza uznawany powszechnie za największego przedstawiciela polskiego romantyzmu."

wzorzec = r"\d+\s\w+\s\d{4}"
wynik = re.findall(wzorzec, napis)
# print(wynik)

with open("dane.txt", "r", encoding="utf-8") as file:
    napis = file.read()

print(napis)

wzorzec = r"\w+@\w+.\w+"
wynik = re.findall(wzorzec, napis)
# print(wynik)

#3. Znajdź wszystkie numery telefonów

wzorzec = r"\d{3}-\d{3}-\d{3}"
wynik = re.findall(wzorzec, napis)
print(wynik)