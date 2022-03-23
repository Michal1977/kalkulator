import sys
import logging
logging.basicConfig(level=logging.DEBUG)

action = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:'))
if action <= 4:
    number1 = float(input('Podaj składnik 1.'))
    number2 = float(input('Podaj składnik 2.'))

else:
    print("Zła wartość")
    exit(1)

if action == 1:
    wynik = (number1)+(number2)
    logging.info(f"Dodaję:", number1, number2)
    print("Wynik to:", round(wynik,2))
if action == 2:
    wynik = (number1)-(number2)
    logging.info(f"Odejmuję:", number1, number2)
    print("Wynik to:", round(wynik,2))
if action == 3:
    wynik = (number1)*(number2)
    logging.info(f"Mnożę:", number1, number2)
    print("Wynik to:", round(wynik,2))
if action == 4:
    wynik = (number1)/(number2)
    logging.info(f"Dzielę:", number1, number2)
    print("Wynik to:", round(wynik,2))

