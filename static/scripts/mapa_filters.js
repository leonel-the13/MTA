document.addEventListener("DOMContentLoaded", function () {
  function getQueryParam(param) {
    const urlParams = new URLSearchParams(window.location.search);
    const value = urlParams.get(param);
    if (!value) return [];
    return value.split(",");
  }

  function highlightActiveFilters() {
    const tipos = getQueryParam("tipo");
    const acesses = getQueryParam("acess");
    document.querySelectorAll(".filter-btn").forEach(function (btn) {
      btn.classList.remove("bg-blue-600", "text-white");
      btn.classList.add("bg-white", "text-gray-700");
      if (
        tipos.length &&
        btn.textContent.includes("Hospedagens") &&
        tipos.includes("hospedagem")
      ) {
        btn.classList.add("bg-blue-600", "text-white");
        btn.classList.remove("bg-white", "text-gray-700");
      }
      if (
        tipos.length &&
        btn.textContent.includes("Restaurantes") &&
        tipos.includes("restaurante")
      ) {
        btn.classList.add("bg-blue-600", "text-white");
        btn.classList.remove("bg-white", "text-gray-700");
      }
      if (
        tipos.length &&
        btn.textContent.includes("Atrações") &&
        tipos.includes("atracao")
      ) {
        btn.classList.add("bg-blue-600", "text-white");
        btn.classList.remove("bg-white", "text-gray-700");
      }
      if (
        tipos.length &&
        btn.textContent.includes("Transportes") &&
        tipos.includes("transporte")
      ) {
        btn.classList.add("bg-blue-600", "text-white");
        btn.classList.remove("bg-white", "text-gray-700");
      }
      if (
        acesses.length &&
        btn.textContent.includes("Mobilidade") &&
        acesses.includes("mobilidade")
      ) {
        btn.classList.add("bg-blue-600", "text-white");
        btn.classList.remove("bg-white", "text-gray-700");
      }
      if (
        acesses.length &&
        btn.textContent.includes("Visual") &&
        acesses.includes("visual")
      ) {
        btn.classList.add("bg-blue-600", "text-white");
        btn.classList.remove("bg-white", "text-gray-700");
      }
      if (
        acesses.length &&
        btn.textContent.includes("Auditiva") &&
        acesses.includes("auditiva")
      ) {
        btn.classList.add("bg-blue-600", "text-white");
        btn.classList.remove("bg-white", "text-gray-700");
      }
      if (
        acesses.length &&
        btn.textContent.includes("Outras") &&
        acesses.includes("outras")
      ) {
        btn.classList.add("bg-blue-600", "text-white");
        btn.classList.remove("bg-white", "text-gray-700");
      }
      if (
        !tipos.length &&
        !acesses.length &&
        btn.textContent.includes("Todos")
      ) {
        btn.classList.add("bg-blue-600", "text-white");
        btn.classList.remove("bg-white", "text-gray-700");
      }
    });
  }

  highlightActiveFilters();

  const tipoBtns = Array.from(document.querySelectorAll(".filter-btn")).filter(
    (btn) =>
      ["Hospedagens", "Restaurantes", "Atrações", "Transportes"].some((t) =>
        btn.textContent.includes(t)
      )
  );
  const acessBtns = Array.from(document.querySelectorAll(".filter-btn")).filter(
    (btn) =>
      ["Mobilidade", "Visual", "Auditiva", "Outras"].some((t) =>
        btn.textContent.includes(t)
      )
  );

  let selectedTipo = getQueryParam("tipo")[0] || "";
  let selectedAcess = getQueryParam("acess")[0] || "";

  tipoBtns.forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      const value = btn.textContent.includes("Hospedagens")
        ? "hospedagem"
        : btn.textContent.includes("Restaurantes")
        ? "restaurante"
        : btn.textContent.includes("Atrações")
        ? "atracao"
        : btn.textContent.includes("Transportes")
        ? "transporte"
        : null;
      if (!value) return;
      if (selectedTipo === value) {
        selectedTipo = "";
      } else {
        selectedTipo = value;
      }
      updateUrl();
    });
  });

  acessBtns.forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      const value = btn.textContent.includes("Mobilidade")
        ? "mobilidade"
        : btn.textContent.includes("Visual")
        ? "visual"
        : btn.textContent.includes("Auditiva")
        ? "auditiva"
        : btn.textContent.includes("Outras")
        ? "outras"
        : null;
      if (!value) return;
      if (selectedAcess === value) {
        selectedAcess = "";
      } else {
        selectedAcess = value;
      }
      updateUrl();
    });
  });
  document.querySelectorAll(".filter-btn").forEach(function (btn) {
    if (btn.textContent.includes("Todos")) {
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        selectedTipo = "";
        selectedAcess = "";
        updateUrl();
      });
    }
  });

  function updateUrl() {
    let url = "/mapa";
    const params = [];
    if (selectedTipo) params.push(`tipo=${selectedTipo}`);
    if (selectedAcess) params.push(`acess=${selectedAcess}`);
    if (params.length) url += "?" + params.join("&");
    window.location.href = url;
  }
});
