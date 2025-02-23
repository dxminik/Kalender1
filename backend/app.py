from flask import Flask, request, render_template
from datetime import datetime, date
from models.model_request_recom import gib_empfehlung

import database.manage_event as me
app = Flask(__name__)

# Startseite mit Formular
@app.route('/')
def index():
    return render_template('index.html')

# Route zum Verarbeiten der Formulareingabe
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    nameInput = data.get('name')
    typeSelect = data.get('type')
    feelingInput = data.get('feeling')
    locationInput = data.get('location')
    descriptionInput = data.get('description')
    dateInput = date.today().strftime("%d-%m-%Y")
    timeInput = datetime.now().time().strftime("%H:%M:%S")
    
    # Empfehlung generieren
    empfehlung = gib_empfehlung(data)

    me.create_event(1, nameInput, typeSelect, dateInput, timeInput, locationInput, descriptionInput, feelingInput, empfehlung)
    
    return {'name': nameInput, 'type': typeSelect, "date": dateInput, "time": timeInput, 'feeling': feelingInput, 'location': locationInput, 'description': descriptionInput}

if __name__ == '__main__':
    app.run(debug=True)  # Debug-Modus aktivieren
