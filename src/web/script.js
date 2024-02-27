document.getElementById('fetchButton').addEventListener('click', () => {
    fetch('https://[API Gatewayエンドポイント]/test/todolist')
        .then(response => response.json())
        .then(data => {
            document.getElementById('apiResponse').innerText = JSON.stringify(data);
        })
        .catch(error => {
            console.error('Error fetching data: ', error);
            document.getElementById('apiResponse').innerText = 'Error fetching data. Check console for details.';
        });
});
