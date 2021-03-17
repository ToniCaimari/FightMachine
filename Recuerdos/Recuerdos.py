Recuerdos = []

option = ""
recuerdo = ""
recordar = 0

while option != "q":
    option = input(
        "Qué quieres hacer? \n     1-Crear recuerdo        2-Recordar      3-Olvidar        4-Hacer un diario        q-Salir\n")
    if option == "1":
        recuerdo = input("Crea el recuerdo: \n")
        Recuerdos.append(recuerdo)
    if option == "2":
        recordar = int(input("Qué recuerdo quieres recordar? (1,2,3...)\n"))
        try:
            print(Recuerdos[recordar-1])
        except:
            print("Este recuerdo no existe... :c")
    if option == "3":
        recordar = int(input("Qué recuerdo quieres olvidar? (1,2,3...)\n"))

        try:
            print("El recuerdo nº"+str(recordar) +
                  " se ha borrado, el recuerdo nº"+str(recordar+1)+" ocupará su lugar!")
            Recuerdos.remove(Recuerdos[recordar-1])

        except:
            print("Este recuerdo no existe... :c")
    if option == "4":
        response = ""
        number = 1
        if len(Recuerdos) >= 1:
            for i in Recuerdos:
                response += str(number)+"- "+i + "\n"
                number += 1
        else:
            print("Aún no tienes recuerdos T-T")
        print(response)
