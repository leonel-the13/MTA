document.getElementById("menu-btn").addEventListener("click", function () {
  const menu = document.getElementById("mobile-menu");
  if (menu.classList.contains("hidden")) {
    menu.classList.remove("hidden");
    feather.replace();
  } else {
    menu.classList.add("hidden");
  }
});
