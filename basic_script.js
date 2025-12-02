// Basic JavaScript example
document.addEventListener('DOMContentLoaded', function() {
    // Get DOM elements
    const messageElement = document.getElementById('message');
    const buttonElement = document.getElementById('changeBtn');

    // Initial message
    messageElement.textContent = 'Hello from JavaScript!';

    // Button click handler
    buttonElement.addEventListener('click', function() {
        messageElement.textContent = 'You clicked the button!';
    });
});




