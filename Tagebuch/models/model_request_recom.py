from openai import OpenAI

client = OpenAI(api_key="sk-...")

def gib_empfehlung(daten):
    prompt = f"Basierend auf den folgenden Nutzerdaten, gib eine Empfehlung für den Benutzer: {daten}"

    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content":  
                            "Du bist ein intelligenter Empfehlungsassistent, der basierend auf"
                            "den kurzen Tagebucheinträgen des Nutzers praktische, einfache und"
                            "umsetzbare Tipps gibt. Deine Empfehlungen sollen alltagsnah, "
                            "hilfreich und auf die aktuelle Stimmung und Interessen des Nutzers "
                            "abgestimmt sein. Halte deine Antworten kurz, motivierend und direkt "
                            "anwendbar – maximal 2-3 Sätze. Falls möglich, gib konkrete kleine "
                            "Handlungsimpulse oder einfache Lösungen für den Tag."},
        {"role": "user", "content": prompt}
    ])

    empfehlung = response.choices[0].message.content
    return empfehlung

