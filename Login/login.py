import os 

alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a","b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0","1", "2", "3", "4", "5", "6", "7", "8","9"]
codificacao = ["e" ,"y", "A", "2", "p", "3", "u", "9", "z", "I", "w", "D", "i", "t", "r", "c", "k", "Q", "T", "8", "g", "P", "O", "b", "C", "1", "j", "7", "d", "F", "J", "X", "h", "V", "v", "R", "U", "Z", "4", "B", "K", "l", "m", "x", "W", "o", "6", "0", "q", "E", "L", "5", "a", "s", "n", "M", "Y", "f", "N", "G", "S", "H"]

login = False
name = ""
see_pass = False
def menu():
    print()
    print("-----------Account Program-----------")
    if login == True:
        print("Connected As:",name)
    print("1 - Login")
    print("2 - Register")
    if login == True:
        print("3 - Log out")
    print("0 - Leave")
    print("-------------------------------------")
    print()



opc = -1
while opc != 0:
    menu()
    try:
        opc = int(input("Option: "))
    except ValueError:
        print("Please enter a valid value...")
        input("Press ENTER to continue...")
    if opc > 3:
        print("Please enter a valid value...")
        input("Press ENTER to continue...")
    elif opc == 1 and login == False:
        archive = open("login.txt","r")
        Encoded_Pass = []
        User = input("Enter your username: ")
        if User == "":
            print("\nEnter a Username...")
            input("Press ENTER to continue...")
        else:
            Pass = input("Enter your password: ")
            if Pass == "":
                print("\nEnter a Password ...")
                input("Press ENTER to continue...")
            else:
                line = " "
                while line != "":
                    line = archive.readline()
                    verification = list(line.split(" : "))
                    ver_pass = True
                    if User == verification[0]:
                        for value in range(0,len(Pass),1):
                            if Pass[value] in alfabeto:
                                Encoded_Pass.append(codificacao[alfabeto.index(Pass[value])])
                        for value in range(0,len(verification[1]),1):
                            if verification[1][value] != "\n":
                                if not Encoded_Pass[value] == verification[1][value]:
                                    ver_pass = False
                        if ver_pass == True:
                            login = True
                            name = verification[0]
                    verification.clear()
                    if login == True:
                        print("Signed in...")
                        input("Press ENTER to continue...")
                        break
                if login == False:
                    print("Sorry but make sure you wrote everything right...")
                    input("Press ENTER to continue...")
    elif opc == 1 and login == True:
        print("Sorry but you are already connected...")
        input("Press ENTER to continue...")          
    elif opc == 2 and login == False:
        archive = open("login.txt","a")
        read = open("login.txt","r")
        print("RULES: Username -> No special characters\nPass -> One Capital Letter / Letters and numbers")
        print()
        User = input("Enter your username: ")
        line = " "
        same = False
        special_characters =  ["!", "@", "#", "$", "%", "^", "&", "*", "()", "-", "+", "?", "_", "=", ",", "<", ">", "/",'"']
        ver_special = False
        if User == "":
            print("\nEnter a Username ...")
            input("Press ENTER to continue...")
        else:
            while line != "":
                line = read.readline()

                if User.lower() == line.split(" : ")[0].lower():
                    print("Sorry but your username has already been chosen ...")
                    input("Press ENTER to continue...")
                    same = True
                    read.close()
                    break

            for valor in User:
                if valor in special_characters:
                    ver_special = True
                    break

            if ver_special == True and same == False:
                print("Please enter a valid Username ...")
                input("Press ENTER to continue...")
            elif ver_special == False and same == False:
                Pass = input("Enter your password: ")
                if Pass == "":
                    print("\nEnter a Password...")
                    input("Press ENTER to continue...")
                else:
                    if  Pass.islower() == False and Pass.isupper() == False and Pass.isnumeric() == False and Pass.isalpha() == False:
                        Encoded_Pass = []
                        for value in range(0,len(Pass),1):
                            if Pass[value] in alfabeto:
                                Encoded_Pass.append(codificacao[alfabeto.index(Pass[value])])
                        Pass = ""
                        for value in Encoded_Pass:
                            Pass += value
                        archive.write(User+" : "+Pass+"\n")
                        archive.close()
                        print("Registration Complete...")
                        input("Press ENTER to continue...")
                    else:
                        print("Invalid Password...")
                        input("Press ENTER to continue...")
    elif opc == 2 and login == True:
        print("Sorry but you are already logged in...")
        input("Press ENTER to continue...")

    elif opc == 3 and login == True:
        login = False
        print("Session ended successfully ...")
        input("Press ENTER to continue...")

    elif opc == 3 and login == False:
        print("Please enter a valid option ...")
        input("Press ENTER to continue...")
