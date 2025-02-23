from flask import Flask, request, render_template
from datetime import datetime

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
    dateInput = datetime.now().date()
    timeInput = datetime.now().time()
    

    me.create_event(1, nameInput, typeSelect, dateInput, timeInput, locationInput, descriptionInput, feelingInput)
    
    return {'name': nameInput, 'type': typeSelect, "date": dateInput, "time": timeInput, 'feeling': feelingInput, 'location': locationInput, 'description': descriptionInput}

if __name__ == '__main__':
    app.run(debug=True)  # Debug-Modus aktivieren
