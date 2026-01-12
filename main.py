# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random

# 1. DATABASE DELLE PAROLE
parole_facili = ["sole", "mare", "casa", "pane", "gatto"]
parole_medie = ["python", "computer", "tavolo", "scuola", "calcio"]
parole_difficili = ["programmazione", "universita", "costellazione", "astronomia"]

# 2. SELEZIONE DELLA DIFFICOLTÀ
print("--- GIOCO DELL'IMPICCATO ---")
scelta = input("Scegli la difficoltà (1: Facile, 2: Medio, 3: Difficile): ")

if scelta == "1":
    lista_scelta = parole_facili
elif scelta == "2":
    lista_scelta = parole_medie
else:
    lista_scelta = parole_difficili

parola_segreta = random.choice(lista_scelta)
possibilita = 9
progresso = ["_"] * len(parola_segreta)

# 3. IL CICLO DI GIOCO
while possibilita > 0:
    print("\nParola: " + " ".join(progresso))
    tentativo = input(f"Tentativi: {possibilita}. Inserisci una lettera o prova la parola intera: ").lower()

    # CASO A: L'utente prova a indovinare la parola intera
    if len(tentativo) > 1:
        if tentativo == parola_segreta:
            # Vittoria istantanea: riempiamo tutti i trattini per far scattare il controllo vittoria
            progresso = list(parola_segreta)
            print("Incredibile! Hai indovinato la parola intera!")
        else:
            possibilita -= 1
            print(f"Sbagliato! '{tentativo}' non è la parola corretta.")

    # CASO B: L'utente inserisce una sola lettera
    elif len(tentativo) == 1:
        if tentativo in parola_segreta:
            print(f"Sì, la lettera '{tentativo}' è presente.")
            for i in range(len(parola_segreta)):
                if parola_segreta[i] == tentativo:
                    progresso[i] = tentativo
        else:
            possibilita -= 1
            print(f"No, la lettera '{tentativo}' non c'è.")

    # CASO C: L'utente preme invio senza scrivere nulla
    else:
        print("Non hai inserito nulla!")

    # CONTROLLO VITTORIA
    if "_" not in progresso:
        print("\n" + "=" * 20)
        print(f"COMPLIMENTI! Hai vinto! La parola era: {parola_segreta}")
        print("=" * 20)
        break

    if possibilita == 0:
        print("\n" + "x" * 20)
        print(f"HAI PERSO! La parola era: {parola_segreta}")
        print("x" * 20)

print("\nGrazie per aver giocato!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
