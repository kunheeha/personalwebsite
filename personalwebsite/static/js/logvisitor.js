import { typeout, clearout, getBrowser, getOperatingSystem, browserInfo } from "./utils.js";

function getDevice(info) {
  let device;
  if (info.includes("Android")) {
    device = "Android";
  } else if (info.includes("iPhone")) {
    device = "iPhone";
  } else if (info.includes("iPad")) {
    device = "iPad";
  } else if (info.includes("Mobile")) {
    device = "Mobile";
  } else {
    device = "Computer";
  }
  return device;
}


fetch("https://ipinfo.io/json?token=bc1db2f1068cf5")
  .then(response => response.json())
  .then(data => {
    let toSend = {
      ipinfo: "true",
      ip: data.ip,
      browser: getBrowser(browserInfo),
      operatingSystem: getOperatingSystem(browserInfo),
      deviceType: getDevice(browserInfo),
      country: data.country,
      region: data.region,
      city: data.city,
      postal: data.postal,
      timezone: data.timezone,
      page: location.pathname
    }
    fetch('/log-visitor', {
      method: 'POST',
      body: JSON.stringify(toSend),
      headers: new Headers({
        "content-type": "application/json"
      })
    })
  })
  .catch(error => {
    let toSend = {
      ipinfo: "false",
      browser: getBrowser(browserInfo),
      operatingSystem: getOperatingSystem(browserInfo),
      deviceType: getDevice(browserInfo),
      page: location.pathname
    }
    fetch('/log-visitor', {
      method: 'POST',
      body: JSON.stringify(toSend),
      headers: new Headers({
        "content-type": "application/json"
      })
    })
  })
