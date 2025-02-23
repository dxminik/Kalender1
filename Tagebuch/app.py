from flask import Flask, request, render_template
from datetime import datetime, date
from models.model_request_recom import gib_empfehlung

import database.manage_event as me

app = Flask(__name__)

# Startseite mit Formular
@app.route('/')
def index():
    return render_template('index.html')

# Route zum Anzeigen der Einträge
@app.route('/eintraege')
def eintraege():
    return render_template('eintraege.html')

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
    empfehlung = gib_empfehlung(data)

    me.create_event(1, nameInput, typeSelect, dateInput, timeInput, locationInput, descriptionInput, feelingInput, empfehlung)
    return {"status": 200}

# Route zum Abfragen der Einträge
@app.route('/getEvents', methods=['GET'])
def getEvents():
    return me.get_all_events()


@app.route('/deleteEvent', methods=['POST'])
def deleteEvent():
    data = request.json
    id = data.get('id')
    me.delete_event(id)
    return {"status": 200}


if __name__ == '__main__':
    app.run(debug=True)  # Debug-Modus aktivieren
