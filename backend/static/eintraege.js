const anzeige = document.getElementById('anzeigeContent');

let eintrag = 0;
const anzahlEintraege = 0;

fetch('http://127.0.0.1:5000/getEvents', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
}).then((response) => {
    response.json().then((data) => {
        data.reverse();
        data.forEach((row) => {
            //Div mit Daten erstellen
            let id = row[0]
            let name = row[2]
            let type = row[3]
            let date = row[4]
            let time = row[5]
            let location = row[6]
            let description = row[7]
            let feeling = row[8]
            let empfehlung = row[9]
            const div = document.createElement('div');
            div.classList.add('anzeigeEintrag');
            div.innerHTML = `
            <h2 class="anzeigeName">${name}</h2> 
            <p class="anzeigeTyp">Art des Eintrags: ${type}</p>
            <p class="anzeigeLocation">Standort: ${location}</p>
            <p class="anzeigeFeeling">Wohlbefinden (von 1 bis 10): ${feeling}</p>
            <p class="anzeigeDescription">Beschreibung: ${description}</p>
            <p class="anzeigeEmpfehlung">Empfehlung: ${empfehlung}</p>
            <p class="anzeigeDate">Erstellt am: ${date} ${time}</p> 
            <button class="anzeigeDelete" id="button${id}" value="${id}" onClick="deleteEintrag(${id})"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm400-600H280v520h400v-520ZM360-280h80v-360h-80v360Zm160 0h80v-360h-80v360ZM280-720v520-520Z"/></svg></button>
            `;
            eintrag++;
            anzeige.appendChild(div);
        })
    })
})

function deleteEintrag(id) {
    fetch('http://127.0.0.1:5000/deleteEvent', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id: id
        })
    }).then((response) => {
        response.json().then((data) => {
            console.log(data)
        })
    })
}
