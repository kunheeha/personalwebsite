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
