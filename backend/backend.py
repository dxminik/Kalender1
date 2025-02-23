from datetime import date, datetime

import database.manage_users as mu
import database.manage_event as me
import models.model_request_recom  as mr
import app

def main_loop():
    print("Hallo, mit wem spreche ich?")
    eingabe = input("Ihre ID eingeben")

    # User informationen laden
    loadeduserinfo = mu.get_user_by_id(eingabe)

    #Abfrage ob neuer Tagebucheintrag erstellt werden soll
    print(f"Hallo {loadeduserinfo[1]}, willst du einen neuen Tagebucheintrag erstellen?")
    beendigung = input("Ja(1) | Nein(0)")

    #Soll kein neuer Eintrag erstellt werden schließt sich das Programm
    if beendigung == 0:
        return

    #Abfrage der Daten und des Eintrages
    wohlbefinden = input("Wie fühlst du dich auf einer Skala von 1 bis 10?")
    event_name = input("Wie soll der Eintrag heißen?")
    event_type = input("Was für ein Typ von Event war es?")
    event_date = date.today()
    event_time = datetime.now().time()
    event_location = input("Wo befindest du dich grad")
    event_description = input("Dein Eintrag")

    #empfehlung = input("Willst du eine Empfehlung?\n"
    #                    "Ja(1) | Nein(0)")

    # Soll kein neuer Eintrag erstellt werden schließt sich das Programm
    #if empfehlung == "1":
    benutzerdaten = {
        "name": mu.get_user_by_id(1)[1],
        "geburtstag": mu.get_user_by_id(1)[4],
        "interessen": mu.get_user_by_id(1)[5],
        "stimmung" : wohlbefinden,
        "tagebucheintrag" : event_description
    }
    ki_ausgabe = mr.gib_empfehlung(benutzerdaten)
    print(ki_ausgabe)


main_loop()