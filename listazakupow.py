"""
Utwórz listę, która będzie przechowywać produkty zakupione przez użytkownika.
Stwórz funkcję dodającą produkt do listy zakupów.
Stwórz funkcję usuwającą produkt z listy zakupów.
Stwórz funkcję wyświetlającą pełną listę zakupów.
"""
import tkinter as tk
produkty= []
def dodawanieproduktow():
    while True:
        lista_zakupow = input('jakie produkty chcesz zapisac do listy zakupów? zakończ pisząc exit ')
        if lista_zakupow =="exit":
            break
        produkty.append(lista_zakupow)
def usuwanieproduktow():
    while True:
        print("Chcesz usunąć przedmiot z listy zakupów?Jeśli tak wpisz jego nazwę. Wpisz exit żeby wyjść")
        print(produkty)
        usuniecie = input("")
        for i in produkty:
            if usuniecie == i:
                produkty.remove(i)
        if usuniecie =="exit":
            break
def wyswietlanieproduktow():
    print(f'twoja ostateczna lista zakupów to{produkty}')


    dodawanieproduktow()
    usuwanieproduktow()
    wyswietlanieproduktow()
