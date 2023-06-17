// Navbar collapse on scroll
function topOffset(element) {
  return element.getBoundingClientRect().top + window.scrollY - document.documentElement.clientTop;
}

function navbarCollapse(navbar) {
  if (topOffset(navbar) > 200) {
    navbar.classList.add('navbar-shrink');
  } else {
    navbar.classList.remove('navbar-shrink');
  }
}

const navbar = document.getElementById('mainNav');

window.onscroll = function(){navbarCollapse(navbar)};

// Prevent #id href links from being added to link
// Navbar links that include "#" in href but not just "#" as href
document.querySelectorAll('a.js-scroll-trigger[href*="#"]:not([href="#"])').forEach(link => {
  link.onclick = function() {
    if (location.pathname.replace(/^\//, "") == link.pathname.replace(/^\//, "")) {
      document.querySelector(link.hash).scrollIntoView({ behavior: "smooth" });
      return false;
    }
  }
});
