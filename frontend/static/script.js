//Dark-Lightmode
const darkModeButton = document.getElementById('darkModeButton');

darkModeButton.addEventListener('click', (e) => {
    console.log('Dark Mode Button Clicked');
})

//FeelingInput
const feelingInput = document.getElementById('feelingInput');
const feelingOutput = document.getElementById('feelingOutput');
let feelingValue = feelingInput.value;


feelingInput.addEventListener('input', (e) => {
    feelingValue = e.target.value;
    feelingOutput.innerHTML = "Ich fühle mich " + feelingValue + "/10"; 
});


