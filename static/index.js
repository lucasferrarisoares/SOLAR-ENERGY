document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/data')
        .then(response => response.json())
        .then(listdata => {
            const ul = document.getElementById('repo-functions');
            ul.innerHTML = '';
            listdata.forEach(item => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <strong>Data:</strong> ${item.date}<br>
                    <strong>Geração Energética:</strong> ${item.energy_generation} kwh<br>
                    <strong>Temperatura:</strong> ${item.temperature}°<br>
                    <strong>Rendimento:</strong> ${Math.trunc(item.performance)}%<br>
                `;
                ul.appendChild(li);
            });
        })
        .catch(() => {
            document.getElementById('repo-functions').innerHTML = '<li>Erro ao carregar dados.</li>';
        });
});