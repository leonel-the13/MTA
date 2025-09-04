// Move o conteúdo do mapa Folium para o div correto
document.addEventListener("DOMContentLoaded", function () {
  var foliumHolder = document.getElementById("folium-map-holder");
  var foliumMapDiv = document.getElementById("folium-map");
  if (foliumHolder && foliumMapDiv) {
    foliumMapDiv.innerHTML = "";
    while (foliumHolder.firstChild) {
      foliumMapDiv.appendChild(foliumHolder.firstChild);
    }
    foliumHolder.remove();
  }
  // Corrige links dos popups do Folium para não navegarem
  setTimeout(function () {
    var iframes = document.querySelectorAll("#folium-map iframe");
    iframes.forEach(function (iframe) {
      try {
        var links = iframe.contentDocument.querySelectorAll("a");
        links.forEach(function (link) {
          link.setAttribute("href", "javascript:void(0)");
          link.onclick = function (e) {
            e.preventDefault();
            return false;
          };
        });
      } catch (e) {}
    });
  }, 1000);
});
