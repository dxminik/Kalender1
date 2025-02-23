from flask import Flask, request, render_template
import database.manage_event as me
app = Flask(__name__)

# Startseite mit Formular
@app.route('/')
def index():
    return render_template('index.html')

# Route zum Verarbeiten der Formulareingabe
@app.route('/submit', methods=['POST'])
def submit():
    nameInput = request.form.get('nameInput')
    typeSelect = request.form.get('typeSelect')
    feelingInput = request.form.get('feellingInput')
    locationInput = request.form.get('locationInput')
    descriptionInput = request.form.get('descriptionInput')
    
    me.create_event(1,nameInput,typeSelect,1231,123,locationInput,descriptionInput)

    return f"Du hast eingegeben: "
 

if __name__ == '__main__':
    app.run(debug=True)  # Debug-Modus aktivieren
