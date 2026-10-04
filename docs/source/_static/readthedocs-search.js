// Use Read the Docs' hosted search when enabled and ready. Otherwise, leave
// Furo's normal Sphinx search available, including in local builds.
(() => {
  let searchEnabled = false;

  const configureSearch = (eventData) => {
    searchEnabled = eventData.data().addons?.search?.enabled === true;
  };

  document.addEventListener("readthedocs-addons-data-ready", (event) => {
    configureSearch(event.detail);
  });

  // Addons may finish loading before this script runs.
  if (window.ReadTheDocsEventData) {
    configureSearch(window.ReadTheDocsEventData);
  }

  const openSearch = (event) => {
    if (
      searchEnabled &&
      document.querySelector("readthedocs-search") &&
      event.target.matches(".sidebar-search-container input[name='q']")
    ) {
      document.dispatchEvent(new CustomEvent("readthedocs-search-show"));
    }
  };

  document.addEventListener("focusin", openSearch);
  document.addEventListener("click", openSearch);
})();
