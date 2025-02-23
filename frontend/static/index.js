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


