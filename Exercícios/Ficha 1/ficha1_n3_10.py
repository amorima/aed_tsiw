'''Implemente um simulador do seu peso noutro Planeta. O programa deverá ler
o seu peso na Terra, assim como o código identificador de planeta (1-6),
calculando o peso respetivo nesse planeta'''

print("Planetas")
print("1 - Mercúrio")
print("2 - Vénus")
print("3 - Marte")
print("4 - Júpiter")
print("5 - Saturno")
print("6 - Urano")
print("7 - Neptuno")
print("\n")

peso=float(input("Indique o seu peso (kg): ")) #Input de peso
codigoPlaneta=float(input("Indique o código do planeta: ")) #Input de código do planeta
print("\n")

match codigoPlaneta:
    case 1:
        pesoPlanetaX=float(peso*(0.37/0.98))
    case 2:
        pesoPlanetaX=float(peso*(0.90/0.98))
    case 3:
        pesoPlanetaX=float(peso*(0.37/0.98))
    case 4:
        pesoPlanetaX=float(peso*(2.53/0.98))
    case 5:
        pesoPlanetaX=float(peso*(1.06/0.98))
    case 6:
        pesoPlanetaX=float(peso*(0.91/0.98))
    case 7:
        pesoPlanetaX=float(peso*(0.91/1.14))

print(f"O seu peso de {peso:.2f} kg no planeta {codigoPlaneta:.0f} seria de {pesoPlanetaX:.2f} kg")

print("\n")