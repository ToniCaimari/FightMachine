import sys

Recuerdos = []

option = ""
recuerdo = ""
recordar = 0

while option != "q":
    option = input(
        "Qué quieres hacer? \n     1-Crear recuerdo        2-Recordar      q-Salir\n")
    if option == "1":
        recuerdo = input("Crea el recuerdo: \n")
        Recuerdos.append(recuerdo)
    if option == "2":
        recordar = int(input("Qué recuerdo quieres? (1,2,3...)\n"))
        try:
            print(Recuerdos[recordar-1])
        except:
            print("Este recuerdo no existe... :c")
