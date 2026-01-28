import requests
from fpdf import FPDF
from bs4 import BeautifulSoup

def scrap_pokemon_list():
    url = "https://pokemondb.net/pokedex/game/lets-go-pikachu-eevee"
    response = requests.get(url)
    # print(response.content)

    soup = BeautifulSoup(response.content, "html.parser")
    pokemon_list = []

    cards_list = soup.find("div", class_="infocard-list")
    cards_data = cards_list.find_all("span", class_="infocard-lg-data")

    for data in cards_data:
        name = data.find("a")
        number = data.find("small")
        pokemon_list.append((name.getText(), number.getText()))
        print((name.getText(), number.getText()))
    return pokemon_list





# wywołania funkcji
pokemon_list = scrap_pokemon_list()

pdf = FPDF()
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
for pokemon in pokemon_list:
    pdf.add_page(format="A5")
    pdf.set_font("DejaVu", size=16)
    pdf.text(x=10, y=10, text= f"{pokemon[1]} {pokemon[0]}")

pdf.output("pokedex.pdf")
