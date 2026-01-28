import json
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import dotenv

with open("menu.json", "r", encoding="utf-8") as file:
    menu = json.load(file)
    # print(menu["menu"])
list_of_pizzas = menu["menu"]
list_of_pizzas_names = []

for pizza in list_of_pizzas:
    list_of_pizzas_names.append(pizza["pizza"])

print(list_of_pizzas)
# print(list_of_pizzas_names)

order = []

def main_page():
    # wyświetl menu
    # dodaj pizzę do zamówienia
    # wyślij zamówienie
    # zakończ
    print("Witaj w pizzerii")
    print("Wybierz opcję: ")
    print("1. Wyświetl menu")
    print("2. Dodaj pizzę do zamówienia")
    print("3. Wyślij zamówienie")
    print("4. Zakończ")
    option = input("")

    if option == "1":
        display_menu()
        pass
    elif option == "2":
        add_to_order()
        pass
    elif option == "3":
        send_order()
        pass
    elif option == "4":
        quit()
    else: 
        print("Podano nieprawidłową wartość")


def display_menu():
    for pizza in list_of_pizzas:
        print(f"Pizza: {pizza["pizza"]}")
        print(f"Składniki: {pizza["dodatki"]}")
        print(f"Ceny: mała: {pizza["ceny"]["S"]} zł")
        print(f"średnia: {pizza["ceny"]["M"]} zł")
        print(f"duża: {pizza["ceny"]["L"]} zł")
        print()
    input("Wciśnij enter, aby wrócić na stronę główną")
    main_page()

def add_to_order():
    print("Którą pizzę chcesz zamówisz:")
    for pizza in list_of_pizzas_names:
        print(f"{list_of_pizzas_names.index(pizza) + 1}.{pizza}")
    
    number = int(input("Podaj numer pizzy: "))
    amount = int(input("Ile sztuk? "))
    size = input("Jakie rozmiary chcesz (S/M/L)? ")

    order.append({
        "size": size, "pizza_amount": 
                  amount, "pizza_name": list_of_pizzas_names[number-1]})

    main_page() 


def send_email(message_txt):
    dotenv.load_dotenv()
    subject = "Pizzeria - potwierdzenie zamowienia"
    sender_email = os.getenv('sender_email')
    recipient_email = os.getenv('recipient_email')
    sender_password = os.getenv('sender_password')
    smtp_server = "smtp.wp.pl"
    smtp_port = 465 
   
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email
    body_part = MIMEText(message_txt)
    message.attach(body_part)


    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
       server.login(sender_email, sender_password)
       server.sendmail(sender_email, recipient_email, message.as_string())



def send_order():
    tekst = "Dziękujemy za wybranie pizzerii, oto podsumowanie Twojego zamówienia:\n"
   
    for pizza in order:
        tekst+=f"{pizza['pizza_amount']} x {pizza['pizza_name']}[{pizza['size']}]"
       
    # Koszt: ...... zł
    send_email(tekst)
    print("Zamówienie zostało złożone")
    input("Wciśnij enter aby kontynuować")




main_page()