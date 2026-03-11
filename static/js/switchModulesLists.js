const modulesList = document.getElementById('modulesList');
const stationsList = document.getElementById('stationsList');

const modulesButton = document.getElementById('modulesButton');
const stationsButton = document.getElementById('stationsButton');

modulesButton.addEventListener('click', function() { 
    stationsList.style.display = "none";
    modulesList.style.display = "flex";
});

stationsButton.addEventListener('click', function() { 
    modulesList.style.display = "none";
    stationsList.style.display = "flex";
});