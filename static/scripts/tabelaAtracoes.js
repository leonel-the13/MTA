fetch("/api/atracoes")
  .then((response) => response.json())
  .then((dados) => {
    if (!dados.length) return;
    const tabela = document.getElementById("tabela-atracoes");
    const thead = tabela.querySelector("thead");
    const tbody = tabela.querySelector("tbody");

    const headerRow = document.createElement("tr");
    Object.keys(dados[0]).forEach((col) => {
      const th = document.createElement("th");
      th.textContent = col;
      headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);

    dados.forEach((row) => {
      const tr = document.createElement("tr");
      Object.values(row).forEach((val) => {
        const td = document.createElement("td");
        td.textContent = val;
        tr.appendChild(td);
      });
      tbody.appendChild(tr);
    });
  });
