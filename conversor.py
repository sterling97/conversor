def conversor(valor_peso):
    dolares = input('Cuantos dolares tienes?: ')
    dolares = float(dolares)
    pesos = dolares * valor_peso
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print('Tienes $ ' + pesos + ' pesos')


menu = """
Bienvenido al conversor de monedas

1 - Dolares a Pesos dominicanos
2 - Dolares a pesos mexicanos
3 - Dolares a pesos argentinos

Elige una opcion: 

"""

opciones = int(input(menu))

if opciones == 1:
    conversor(58.80)

elif opciones == 2:
    conversor(24)

elif opciones == 3:
    conversor(65)
    
else:
    print('Ingresa una opcion correcta por favor')


