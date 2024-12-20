async function getETA() {
    const trainData = document.getElementById('trainData').value;
    const loading = document.getElementById('loading');
    const result = document.getElementById('result');

    loading.style.display = 'block'; // Show loading spinner
    result.innerText = ''; // Clear previous results

    try {
        const response = await fetch('http://127.0.0.1:5000/get_eta', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ train_data: trainData }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        result.innerText = `ETA: ${data.eta}`;
    } catch (error) {
        console.error('Error fetching ETA:', error);
        result.innerText = 'Error calculating ETA.';
    } finally {
        loading.style.display = 'none'; // Hide loading spinner
    }
}
