from flask import Flask, request, render_template

app = Flask(__name__)

# Startseite mit Formular
@app.route('/')
def index():
    return render_template('index.html')

# Route zum Verarbeiten der Formulareingabe
@app.route('/submit', methods=['POST'])
def submit():
    nameInput = request.form.get('nameInput')  # Eingabe aus dem Formular abrufen
    typeSelect = request.form.get('typeSelect')
    feelingInput = request.form.get('feellingInput')
    locationInput = request.form.get('locationInput')
    descriptionInput = request.form.get('descriptionInput')
    
    #return f"Du hast eingegeben: {user_input}"
    input_list = [nameInput, typeSelect, feelingInput, locationInput, descriptionInput]
    return 

if __name__ == '__main__':
    app.run(debug=True)  # Debug-Modus aktivieren
