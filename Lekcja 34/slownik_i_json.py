o_mnie = {
    "imie": "Marta",
    "wiek": 18,
    "miasto": "Wrocław"
}
# print(o_mnie)

gra = {
    "nazwa": "CS",
    "data_wydania": 1999,
    "wydawca": "valve",
    "gatunek": "strzelanka"
}
# print(gra["nazwa"])
# print(gra.get("nazwaz"))

# for value in gra.values():
#     print(value)

# for value in gra.keys():
#     print(value)

# for value in gra.items():
#     print(value)

# gra.setdefault("PEGI", 18)
# print(gra)

# del gra["gatunek"]
# print(gra)

# usuniety = gra.pop("wydawca")
# print(usuniety)
# print(gra)

# usun_ostatni = gra.popitem()
# print(gra)

# gra.clear()
# print(gra)

import pprint
# print(gra)
# pprint.pprint(gra)

import json

with open("spis_gier.json", "r") as plik:
    gry = json.load(plik)

# pprint.pprint(gry["spis_gier"])

gry["spis_gier"].append(gra)
pprint.pprint(gry["spis_gier"])

with open("nowy_spis.json", "w") as plik:
    json.dump(gry, plik, indent= 4, sort_keys=True)