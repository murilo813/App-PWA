function salvarNoIndexedDB(tabela, dados) {
    const dbName = 'lojaDB';
    const version = 1;
    let db;

    const request = indexedDB.open(dbName, version);

    request.onupgradeneeded = function (e) {
        db = e.target.result;

        if (!db.objectStoreNames.contains(tabela)) {
            db.createObjectStore(tabela, { keyPath: 'id' });
        }
    };

    request.onsuccess = function (e) {
        db = e.target.result;
        const trans = db.transaction([tabela], 'readwrite');
        const store = trans.objectStore(tabela);

        dados.forEach(item => {
            store.put(item);
        });
    };
}

function carregarDoIndexedDB(tabela) {
    return new Promise((resolve, reject) => {
        const dbName = 'lojaDB';
        const version = 1;
        let db;

        const request = indexedDB.open(dbName, version);

        request.onsuccess = function (e) {
            db = e.target.result;
            const trans = db.transaction([tabela], 'readonly');
            const store = trans.objectStore(tabela);
            const allData = store.getAll();

            allData.onsuccess = function () {
                resolve(allData.result);
            };
            allData.onerror = function () {
                reject('Erro ao carregar dados');
            };
        };
    });
}

function filtrarProduto() {
    const input = document.getElementById('search');
    const filter = input.value.toLowerCase();
    const table = document.querySelector('table');
    const rows = table.getElementsByTagName('tr');

    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName('td');
        let mostrar = false;

        for (let j = 0; j < cells.length; j++) {
            const cell = cells[j];
            if (cell) {
                if (cell.textContent.toLowerCase().indexOf(filter) > -1) {
                    mostrar = true;
                    break;
                }
            }
        }

        if (mostrar) {
            rows[i].style.display = '';
        } else {
            rows[i].style.display = 'none';
        }
    }
}
