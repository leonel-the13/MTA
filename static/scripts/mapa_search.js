// Script para autocomplete e busca de atrações
// Busca sugestões da API e centraliza o mapa ao selecionar

document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("search-input");
  const resultsBox = document.createElement("div");
  resultsBox.className =
    "absolute z-50 bg-white border border-gray-300 w-full rounded-b shadow-lg max-h-60 overflow-y-auto";
  resultsBox.style.display = "none";
  input.parentNode.appendChild(resultsBox);

  let timeout = null;
  input.addEventListener("input", function () {
    clearTimeout(timeout);
    const query = input.value.trim();
    if (query.length < 2) {
      resultsBox.style.display = "none";
      resultsBox.innerHTML = "";
      return;
    }
    timeout = setTimeout(() => {
      fetch(`/api/atracoes`)
        .then((r) => r.json())
        .then((data) => {
          const filtered = data.filter((a) =>
            a.nome.toLowerCase().includes(query.toLowerCase())
          );
          if (filtered.length === 0) {
            resultsBox.innerHTML =
              '<div class="p-2 text-gray-500">Nenhum resultado</div>';
            resultsBox.style.display = "block";
            return;
          }
          resultsBox.innerHTML = filtered
            .map(
              (a) =>
                `<div class='p-2 hover:bg-blue-100 cursor-pointer' data-lat='${a.latitude}' data-lng='${a.longitude}'><b>${a.nome}</b></div>`
            )
            .join("");
          resultsBox.style.display = "block";
        });
    }, 200);
  });

  resultsBox.addEventListener("click", function (e) {
    const item = e.target.closest("[data-lat]");
    if (!item) return;
    const lat = item.getAttribute("data-lat");
    const lng = item.getAttribute("data-lng");
    // Limpa todos os filtros e aproxima o zoom
    window.location.href = `/mapa?lat=${lat}&lng=${lng}&zoom=13`;
  });

  document.addEventListener("click", function (e) {
    if (!resultsBox.contains(e.target) && e.target !== input) {
      resultsBox.style.display = "none";
    }
  });
});
