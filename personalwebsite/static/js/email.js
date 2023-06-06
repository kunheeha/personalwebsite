const contactForm = document.getElementsByClassName('contact-form')[0];
const displayMsg = document.getElementsByClassName('formMessages')[0];

contactForm.onsubmit = function(event) {
  event.preventDefault();
  displayMsg.classList.add('alert');
  displayMsg.classList.add('alert-info');
  displayMsg.textContent = 'Please wait';
  const formData = new FormData(contactForm);

  fetch('/contact', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    if (data.status) {
      displayMsg.classList.remove('alert-info');
      displayMsg.classList.add('alert-success');
      displayMsg.textContent = 'Your message has been sent. Please check your email';
      contactForm.reset();
    } else if (!data.status) {
      displayMsg.classList.remove('alert-info');
      displayMsg.classList.add('alert-danger');
      displayMsg.textContent = 'Message failed to send. Please check you have filled in the form correctly';
    }
  })
}
