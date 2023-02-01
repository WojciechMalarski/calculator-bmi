# Napisz program do obliczania BMI (indeksu masy ciała).

#wzrost
#waga
waga = int(input("Wpisz swoją wage(kg): "))
wzrost = float(input("Wpisz swój wzrost(m): "))

bmi = waga / wzrost**2
roundbmi = round(bmi,2)
print(f'Twoje BMI wynosi:{roundbmi}')