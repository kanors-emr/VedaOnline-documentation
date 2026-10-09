/* Homepage hero banner: move the soft spotlight with the cursor. */
(function () {
  "use strict";

  function initBanner(banner) {
    if (banner.getAttribute("data-vo-spot-init") === "true") {
      return;
    }

    var svg = banner.querySelector(".vo-hero-banner__charts");
    var light = banner.querySelector(".vo-hero-banner__spot-light");
    if (!svg || !light || !svg.createSVGPoint) {
      return;
    }

    banner.setAttribute("data-vo-spot-init", "true");
    var point = svg.createSVGPoint();

    banner.addEventListener("mousemove", function (event) {
      var matrix = svg.getScreenCTM();
      if (!matrix) {
        return;
      }
      point.x = event.clientX;
      point.y = event.clientY;
      var local = point.matrixTransform(matrix.inverse());
      light.setAttribute("cx", local.x);
      light.setAttribute("cy", local.y);
    });
  }

  function initAll() {
    var banners = document.querySelectorAll(".vo-hero-banner");
    for (var i = 0; i < banners.length; i++) {
      initBanner(banners[i]);
    }
  }

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(initAll);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAll);
  } else {
    initAll();
  }
})();
