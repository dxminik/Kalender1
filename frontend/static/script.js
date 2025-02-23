//Dark-Lightmode
const darkModeButton = document.getElementById('darkModeButton');

darkModeButton.addEventListener('click', (e) => {
    console.log('Dark Mode Button Clicked');
})

//NameInput
const nameInput = document.getElementById('nameInput');
let nameValue = nameInput.value;

nameInput.addEventListener('input', (e) => {
    nameValue = e.target.value;
})

//TypeInput
const typeSelect = document.getElementById('typeSelect');
let typeValue = typeInput.value;

typeSelect.addEventListener('change', (e) => {
    typeValue = e.target.value;
})


//FeelingInput
const feelingInput = document.getElementById('feelingInput');
const feelingOutput = document.getElementById('feelingOutput');
let feelingValue = feelingInput.value;

feelingInput.addEventListener('input', (e) => {
    feelingValue = e.target.value;
    feelingOutput.innerHTML = "Ich fühle mich " + feelingValue + "/10"; 
});

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

submitButton.addEventListener('click', (e) => {
    fetch('127.0.0.1:5000/submit', {
        method: "POST",
        body: JSON.stringify({
            name: nameValue,
            type: typeValue,
            feeling: feelingValue,
            location: locationValue,
            description: descriptionValue
        })
    })
    e.preventDefault();
    
})

