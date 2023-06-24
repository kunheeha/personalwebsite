// Type out
function typeout(text, element, delay) {
  const letters = text.split("");
  let i = 0;
  function type() {
    if (i < letters.length) {
      element.append(letters[i]);
      i++;
      setTimeout(type, delay)
    }
  }
  type();
  return letters.length * delay;
}

// Clear out
function clearout(element) {
  element.innerHTML = "";
}

// Get browser information
function getBrowser(info) {
  let browser;
  // Opera
  if (info.includes("OPR")) {
    browser = "Opera";
  }
  // Microsoft Edge
  else if (info.includes("Edg")) {
    browser = "Microsoft Edge";
  }
  // Firefox
  else if (info.includes("Firefox")) {
    browser = "Firefox";
  }
  // Chrome
  else if (info.includes("Chrome")) {
    browser = "Chrome";
  }
  else if (info.includes("Safari")) {
    browser = "Safari";
  }
  return browser;
}


// Get device operating system
function getOperatingSystem(info) {
  let os;
  let matcher = /\((?<os>[A-Z][A-Za-z0-9]+)(\s|;)/;
    if (matcher.exec(info)) {
      switch (matcher.exec(info).groups.os) {
        case "X11":
          os = "Linux"
          break;
        case "Windows":
          os = "Windows"
          break;
        case "Macintosh":
          os ="MacOS"
          break;
        default:
          os = null;
          break;
      }
    } else {
      os = null;
    }
  return os
}

const browserInfo = navigator.userAgent;

export { typeout, clearout, getBrowser, getOperatingSystem, browserInfo }
