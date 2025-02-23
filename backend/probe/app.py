from flask import Flask, request, render_template

app = Flask(__name__)

# Startseite mit Formular
@app.route('/')
def index():
    return render_template('index.html')

# Route zum Verarbeiten der Formulareingabe
@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input')  # Eingabe aus dem Formular abrufen
    return f"Du hast eingegeben: {user_input}"

if __name__ == '__main__':
    app.run(debug=True)  # Debug-Modus aktivieren
