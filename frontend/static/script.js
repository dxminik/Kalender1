//Dark-Lightmode
const darkModeButton = document.getElementById('darkModeButton');

darkModeButton.addEventListener('click', (e) => {
    console.log('Dark Mode Button Clicked');
})

//HeaderSearch
const headerSearch = document.getElementById('headerSearch');
const searchButton = document.getElementById('searchButton');

headerSearch.addEventListener('input', (e) => {
    console.log(e.target.value);
})

//FeelingInput
const feelingInput = document.getElementById('feelingInput');
const feelingOutput = document.getElementById('feelingOutput');
let feelingValue = feelingInput.value;


feelingInput.addEventListener('input', (e) => {
    feelingValue = e.target.value;
    feelingOutput.innerHTML = "Ich fühle mich " + feelingValue + "/10"; 
});


