async function getETA() {
    // Fetch values from input fields
    const distance = document.getElementById('distance').value;
    const speed = document.getElementById('speed').value;

    // Check if values are valid
    if (!distance || !speed) {
        document.getElementById('result').innerText = 'Please enter valid distance and speed.';
        return;
    }

    try {
        const response = await fetch('https://your-app-name.onrender.com/get_eta', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ train_data: `${distance},${speed}` }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        document.getElementById('result').innerText = `ETA: ${data.eta}`;
    } catch (error) {
        console.error('Error fetching ETA:', error);
        document.getElementById('result').innerText = 'Error calculating ETA.';
    }
}
