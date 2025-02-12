from openai import OpenAI

client = OpenAI(api_key='')


def gib_empfehlung(daten):
    prompt = f"Basierend auf den folgenden Nutzerdaten {daten}, gib eine Empfehlung für den Benutzer."

    response = client.completions.create(model="gpt-3.5-turbo",
    prompt=prompt,
    max_tokens=150)

    return response.choices[0].text.strip()

benutzerdaten = {
    "name": "Max",
    "alter": 28,
    "interessen": ["Sport", "Technologie", "Reisen"],
    "stimmung" : "hat Lleichte depressionen"
}

empfehlung = gib_empfehlung(benutzerdaten)
print("Empfehlung:", empfehlung)