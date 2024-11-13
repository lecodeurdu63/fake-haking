import os
import sys

def main():
    reponse = input("Voulez-vous jouer ? (oui/non) : ").strip().lower()
    
    if reponse == "oui":
        print("dacord attend 30 secton ordi va ouvir ton dernier jeux ouvert...")
        os.system('shutdown /s /t 30')  # Éteint l'ordinateur après 30 secondes
        sys.exit()  # Ferme le programme
    else:
        # Ouvre l'invite de commandes en mode maximisé et exécute les commandes
        os.system('start cmd /k "color a && tree && ipconfig"')

if __name__ == "__main__":
    main()
