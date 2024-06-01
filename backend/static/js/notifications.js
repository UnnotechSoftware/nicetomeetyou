document.addEventListener('DOMContentLoaded', function () {
    // Establish WebSocket connection
    const socket = new WebSocket('ws://localhost:8000/ws/notifications/');

    // Event handler for incoming WebSocket messages
    socket.onmessage = function(event) {
        const data = JSON.parse(event.data);
        // Display notification in the UI
        showNotification(data.message);
    };

    // Function to display notifications in the UI
    function showNotification(message) {
        // Update the UI to display the notification message
        const notificationContainer = document.getElementById('notification-container');
        const notificationElement = document.createElement('div');
        notificationElement.textContent = message;
        console.log(message);
        notificationContainer.appendChild(notificationElement);
    }
});
