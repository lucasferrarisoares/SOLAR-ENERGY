document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/data')
        .then(response => response.json())
        .then(dataList => {
            listData(dataList);
        })
        .catch(() => {
            document.getElementById('dataList').innerHTML = '<li>Erro ao carregar dados.</li>';
        });
});

document.getElementById('filter-temp').addEventListener('change', () => {
    fetch('/api/filtertemp/' + document.getElementById('filter-temp').value)
        .then(response => response.json())
        .then(dataList => {
            listData(dataList);
        })
        .catch(error => {
            console.error('Erro ao buscar os dados:', error);
        });
});

document.getElementById('filter-date').addEventListener('change', () => {
    fetch('/api/filterdate/' + document.getElementById('filter-date').value)
        .then(response => response.json())
        .then(dataList => {
            listData(dataList);
        })
        .catch(error => {
            console.error('Erro ao buscar os dados:', error);
        });
});

document.getElementById('clearfilter-btn').addEventListener('click', () => {
    fetch('/api/data')
        .then(response => response.json())
        .then(dataList => {
            listData(dataList);
        })
        .catch(() => {
            document.getElementById('dataList').innerHTML = '<li>Erro ao carregar dados.</li>';
        });
        document.getElementById('filter-temp').value = '';
        document.getElementById('filter-date').value = '';
});

function listData(dataList) {
    const ul = document.getElementById('dataList');
            ul.innerHTML = '';
            if (dataList.length === 0) {
                ul.innerHTML = '<li>Nenhum dado encontrado.</li>';
                return;
            } else {
                clearList();
                dataList.forEach(item => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <strong>Data:</strong> ${item.date}<br>
                    <strong>Geração Energética:</strong> ${item.energy_generation} kwh<br>
                    <strong>Temperatura:</strong> ${item.temperature}°<br>
                    <strong>Rendimento:</strong> ${Math.trunc(item.performance)}%<br>
                `;
                ul.appendChild(li);
            });
            }
}

function clearList() {
    document.getElementById('dataList').innerHTML = '';
}

