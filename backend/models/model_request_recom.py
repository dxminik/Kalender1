from openai import OpenAI


client = OpenAI(api_key='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')


def gib_empfehlung(daten):
    prompt = f"Basierend auf den folgenden Nutzerdaten, gib eine Empfehlung für den Benutzer: {daten}"

    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content":   "Du bist ein hilfreicher Empfehlungsassistent. "
                                        "Deine Aufgabe ist es, dem Benutzer einfache und praktische Tipps zu geben, "
                                        "dazu verarbeitest du seine persönliche Daten und seinen Tagebuch Eintrag."
                                        "um seinen Alltag basierend auf seinen Interessen und seiner Stimmung zu verbessern. "
                                        "Halte die Antwort kurz, prägnant und leicht umsetzbar."},
        {"role": "user", "content": prompt}
    ])

    empfehlungg = response.choices[0].message.content
    return empfehlungg

benutzerdaten = {
    "name": get_user_by_id(1)[1],
    "geburtstag": get_user_by_id(1)[4],
    "interessen": get_user_by_id(1)[5],
    "stimmung" : "2/10",
    "tagebucheintrag" : "Manchmal fühlt es sich an, als würde die Welt gegen einen arbeiten. Heute war einer dieser Tage. "
                        "Es fing schon mies an. Mein Wecker hat nicht geklingelt, weil ich vergessen habe, ihn aufzuladen. Bin dann zehn Minuten vor Unterrichtsbeginn aus dem Bett gefallen. Natürlich kein Frühstück, keine Zeit für eine Dusche – nur reingeschlüpft in das erstbeste T-Shirt, das halb unter dem Bett lag. Mein Bus? Abgefahren. Also durfte ich rennen. Ich war klitschnass, weil es ausgerechnet heute auch noch regnen musste."
                        "In der Schule ging’s direkt weiter: Mathe-Test – total verhauen. Ich hatte die Formeln eigentlich drauf, aber mein Kopf war wie leergefegt. Frau Berger hat mir diesen enttäuschten Blick zugeworfen, und das war fast noch schlimmer als die Note selbst. Ich hasse es, Erwartungen zu enttäuschen."
                        "In der Pause hab ich versucht, mit Nico und den anderen abzuhängen, aber sie haben kaum mit mir geredet. Keine Ahnung, ob ich was falsch gemacht habe, aber das Gefühl ausgeschlossen zu sein, ist nicht neu. Es trifft mich nur jedes Mal ein bisschen härter."
                        "Zu Hause angekommen, wollte ich einfach nur in Ruhe Musik hören. Aber dann kamen die Eltern – mal wieder Streit über irgendeinen Blödsinn, der nicht mal mit mir zu tun hatte. Trotzdem zieht es mich runter."
                        "Ich weiß, morgen ist ein neuer Tag, und theoretisch könnte es besser laufen. Aber heute, Heute war einfach scheiße."
}

empfehlung = gib_empfehlung(benutzerdaten)
print("Empfehlung:", empfehlung)