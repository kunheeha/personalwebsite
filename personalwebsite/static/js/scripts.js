// Type out function
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
  return letters.length;
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
    browser = "probably Chrome";
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
  return os
}


// Get device type
function getDeviceType(info) {
  let device;
  let operatingSystem;
  if (info.includes("Android")) {
    device = "an Android device";
  } else if (info.includes("iPhone")) {
    device = "an iPhone";
  } else if (info.includes("iPad")) {
    device = "an iPad";
  } else if (info.includes("Mobile")) {
    device = "mobile device";
    operatingSystem = getOperatingSystem(info);
  } else {
    device = "device";
    operatingSystem = getOperatingSystem(info);
  }
  return {
    "device": device,
    "operatingSystem": operatingSystem
  };
}


// Get user info
function getUserInfo() {
  let url = "https://ipinfo.io/json?token=bc1db2f1068cf5";
  let userInfo;
  fetch(url)
    .then(response => response.json())
    .then(data => {
      userInfo = `You are located in ${data.city}, ${data.region}, your public ip is ${data.ip}, and your internet provider seems to be ${data.org}.`;
      typeout(userInfo, document.getElementById("userinfo-text"), 50);
    })
    .catch(error => {
      console.log("ipinfo error: ", error);
    })
}


let pseudoLoadingText = "Getting your info";

function loadPseudoLoadingText(text, element, delay) {
  const letters = text.split("");
  const ellipsisDelay = delay * 4;
  let i = 0;
  let j = 0;
  let k = 0;
  function type() {
    if (i < letters.length) {
      element.append(letters[i]);
      i++;
      setTimeout(type, delay)
    } else {
      function addEllipsis() {
        if (j < 3) {
          element.append(" . ");
          j++;
          setTimeout(addEllipsis, ellipsisDelay);
        } else {
          j = 0;
          function clearEllipsis() {
            element.innerHTML = text;
            k++;
            setTimeout(addEllipsis, ellipsisDelay);
          }
          if (k < 3) {
            clearEllipsis();
          }
        }
      }
      setTimeout(addEllipsis, ellipsisDelay);
    }
  }
  type();
}

const browserInfo = navigator.userAgent;
const screenSize = `${window.screen.width}x${window.screen.height}`;
const operatingSystem = getDeviceType(browserInfo).operatingSystem;

function typeAbout(placeholder, element, delay) {
  loadPseudoLoadingText(placeholder, element, delay);
  let waitTime = delay * placeholder.length + delay * 4**3 + 10;
  function typeSystemInfo() {
    let systemInfo; 
    if (operatingSystem) {
      systemInfo = `You are viewing this website on a ${screenSize} screened ${operatingSystem} ${getDeviceType(browserInfo).device}, and your browser is ${getBrowser(browserInfo)}.`;
    } else {
      systemInfo = `You are viewing this website on ${getDeviceType(browserInfo).device} with a ${screenSize} screen, and your browser is ${getBrowser(browserInfo)}.`;
    }
    element.innerHTML = "";
    waitTime = typeout(systemInfo, element, delay) * delay + 500;
    setTimeout(getUserInfo, waitTime);
  }
  setTimeout(typeSystemInfo, waitTime);
}

typeAbout(pseudoLoadingText, document.getElementById("introduction-text"), 50);


