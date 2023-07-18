function send_msg() {
    const input = document.getElementById("friendID");
  
    // Create a container div
    const container = document.createElement('div');
  
    // Append the input element to the container
    container.appendChild(input);
  
    // Create the form element
    const form = document.createElement('form');
    form.action = "communication";
    form.method = "POST";
  
    // Append the container to the form
    form.appendChild(container);
  
    // Create the hidden submit button
    const button = document.createElement('input');
    button.type = 'submit';
    button.value = 'Submit';
    button.style.visibility = 'hidden';
  
    // Append the button to the form
    form.appendChild(button);
  
    // Append the form to the document body
    document.body.appendChild(form);
  
    // Trigger the form submission
    button.click();
  }
  