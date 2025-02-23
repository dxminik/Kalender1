//Dark-Lightmode
const darkModeButton = document.getElementById('darkModeButton');

darkModeButton.addEventListener('click', (e) => {
    console.log('Dark Mode Button Clicked');
})

//Formular
const form = document.getElementById('mainContentContainer');

//FeelingInput
const feelingInput = document.getElementById('feelingInput');
const feelingOutput = document.getElementById('feelingOutput');
let feelingValue = feelingInput.value;

feelingInput.addEventListener('input', (e) => {
    feelingValue = e.target.value;
    feelingOutput.innerHTML = "Ich fühle mich " + feelingValue + "/10"; 
});

//NameInput
const nameInput = document.getElementById('nameInput');
let nameValue;

nameInput.addEventListener('input', (e) => {
    nameValue = e.target.value;
})

//TypeSelect
const typeSelect = document.getElementById('typeSelect');
let typeValue = typeSelect.value;

typeSelect.addEventListener('change', (e) => {
    typeValue = e.target.value;
})



//LocationInput
const locationInput = document.getElementById('locationInput');
let locationValue = locationInput.value;

locationInput.addEventListener('input', (e) => {
    locationValue = e.target.value;
})

//DescriptionInput
const descriptionInput = document.getElementById('descriptionInput');
let descriptionValue = descriptionInput.value;

descriptionInput.addEventListener('input', (e) => {
    descriptionValue = e.target.value;
})

//SubmitButton
const submitButton = document.getElementById('submitButton');
submitButton.addEventListener('click', async (e) => {
    e.preventDefault();
    console.log(nameValue, feelingValue, typeValue, locationValue, descriptionValue)
    const response = await fetch('http://127.0.0.1:5000/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: nameValue,
            feeling: feelingValue,
            type: typeValue,
            location: locationValue,
            description: descriptionValue
        })
    }).then((response => {
        response.json().then((data) => {
            console.log(data)
            if (data.status === 200) {
                alert('Eintrag erfolgreich !')
            } else {
                alert('Eintrag fehlgeschlagen !')
            }
        })
    }))
})


