function updateTrafficLights() {
    fetch('/status')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Traffic light status:', data); // Log the data received
            updateLight('north_south', data.north_south);
            updateLight('east_west', data.east_west);
        })
        .catch(error => {
            console.error('Error fetching traffic light status:', error);
        });
}

function updateLight(direction, status) {
    const redLight = document.getElementById(`${direction}_red`);
    const yellowLight = document.getElementById(`${direction}_yellow`);
    const greenLight = document.getElementById(`${direction}_green`);

    if (!redLight || !yellowLight || !greenLight) {
        console.error(`Elements for ${direction} not found!`);
        return;
    }

    redLight.classList.remove('active');
    yellowLight.classList.remove('active');
    greenLight.classList.remove('active');

    if (status === 'red') {
        redLight.classList.add('active');
    } else if (status === 'yellow') {
        yellowLight.classList.add('active');
    } else if (status === 'green') {
        greenLight.classList.add('active');
    }
}

setInterval(updateTrafficLights, 1000);
updateTrafficLights();
