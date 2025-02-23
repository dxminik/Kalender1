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

    empfehlung = response.choices[0].message.content
    return empfehlung
