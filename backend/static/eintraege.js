const anzeige = document.getElementById('anzeigeContainer');

let eintraege;

fetch('http://127.0.0.1:5000/getEvents', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
}).then((response) => {
    response.json().then((data) => {
        data.forEach((row) => {
            //Div mit Daten erstellen
            let name = row[2]
            let type = row[3]
            let date = row[4]
            let time = row[5]
            let location = row[6]
            let description = row[7]
            let feeling = row[8]
            const div = document.createElement('div');
            div.classList.add('anzeigeEintrag');
            div.innerHTML = `
            <h2 class="anzeigeEintragName">${name}</h2> 
            <p class="anzeigEintragTyp">${type}</p>
            <p class="anzeigeEintragLocation">${location}</p>
            <p class="anzeigeEintragFeeling">${feeling}</p>
            <p class="anzeigeEintragDescription">${description}</p>
            <p class="anzeigeEintragDate">${date}</p>
            <p class="anzeigeEintragTime">${time}</p>
            `;
            anzeige.appendChild(div);
        })
    })
})