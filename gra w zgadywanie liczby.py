#Napisz grę w zgadywanie liczb.
from random import randint

x =randint(1,10)
while True:
    losowa = int(input('została wylosowana liczba od 1 do 10, zgadnij poprawną liczbę'))
    if losowa == x:
        print(f"gratulacje, prawidłowa liczba to {x}")
        break
    else:
        print("podałeś złą liczbę, spróbuj ponownie")