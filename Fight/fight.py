Fighters = "Chiki, Richi"

Chiki = "1-Puñala', 2-Pistoletaso, 3-¡Ti arranco la cara esa de mono que tiene'!"
Chiki_Hp = 100
Chiki_Fear = 0

Richi = "1-Puñetaso en la nuez, 2-Pistoletaso, 3-¡Tivio a busca' i tivio a mata'! "
Richi_Hp = 100
Richi_Fear = 0

Fighter = ""
player_input = ""

player_input = input("Choose a Fighter: \n" + Fighters+"\n")
Fighter = player_input

while Chiki_Hp > 0 or Richi_Hp > 0:
    if Fighter == "Chiki":
        player_input = input("\nChiki ataca: \n" + Chiki+"\n")
        if player_input == "1":
            Richi_Hp -= (20-Chiki_Fear)
            if Richi_Hp > 0:
                Fighter = "Richi"
                print("\n¡AhOstiaMeAEchoUnEsguince! \n" +
                      Fighter+"'s live is "+str(Richi_Hp))

            else:
                Fighter = "Richi"
                print("X_X" + str(Richi_Hp)+"\n"+Fighter+" died\n :C")
                break
        elif player_input == "2":
            Richi_Hp -= (70-Chiki_Fear)
            if Richi_Hp > 0:
                Fighter = "Richi"
                print("\n¡AAAAAAAAAAAAAAH! \n" +
                      Fighter+"'s live is "+str(Richi_Hp))

            else:
                Fighter = "Richi"
                print("X_X" + str(Richi_Hp)+"\n"+Fighter+" died\n :C")
                break
        elif player_input == "3":
            Richi_Fear += 10
            if Richi_Fear < 40:
                Fighter = "Richi"
                print("\n"+Fighter+"'s Fear: "+str(Richi_Fear)+"\nD:")

            else:
                Fighter = "Richi"
                print("\n"+Fighter+"'s Fear: "+str(Richi_Fear)+"\nD':")

    if Fighter == "Richi":
        player_input = input("\nRichi ataca: \n" + Richi+"\n")
        if player_input == "1":
            Chiki_Hp -= (20-Richi_Fear)
            if Chiki_Hp > 0:
                Fighter = "Chiki"
                print("\n¡AhOstiaMeAEchoUnEsguince! \n" +
                      Fighter+"'s live is "+str(Chiki_Hp))

            else:
                Fighter = "Chiki"
                print("\nX_X" + str(Chiki_Hp)+"\n"+Fighter+" died\n :C")
                break
        elif player_input == "2":
            Chiki_Hp -= (70-Richi_Fear)
            if Chiki_Hp > 0:
                Fighter = "Chiki"
                print("\n¡AAAAAAAAAAAAAAH! \n" +
                      Fighter+"'s live is "+str(Chiki_Hp))

            else:
                Fighter = "Chiki"
                print("\nX_X" + str(Chiki_Hp)+"\n"+Fighter+" died\n :C")
                break

        elif player_input == "3":
            Chiki_Fear += 10
            if Chiki_Fear < 40:
                Fighter = "Chiki"
                print("\n"+Fighter+"'s Fear: "+str(Chiki_Fear)+"\nD:")

            else:
                Fighter = "Chiki"
                print("\n"+Fighter+"'s Fear: "+str(Chiki_Fear)+"\nD':")
