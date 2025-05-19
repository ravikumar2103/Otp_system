document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generateBtn');
    const messageDiv = document.getElementById('message');

    if (generateBtn) {
        generateBtn.addEventListener('click', function() {
            fetch('/generate_otp', {
                method: 'POST'
            })
            .then(response => response.json())
            .then(data => {
                messageDiv.textContent = data.message + ' Identifier: ' + data.identifier;
                // Optionally, you could redirect the user to the verification page
                // window.location.href = '/verify';
            })
            .catch(error => {
                console.error('Error:', error);
                messageDiv.textContent = 'Failed to generate OTP.';
            });
        });
         messageDiv.classList.add('show');

                    // Optionally hide the message after a few seconds
                    setTimeout(() => {
                        messageDiv.classList.remove('show');
                    }, 50000);
    }
});
/*document.addEventListener('DOMContentLoaded', function() {
    const requestForm = document.getElementById('requestForm');
    const messageDiv = document.getElementById('message');

    if (requestForm) {
        requestForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const formData = new FormData(this);

            fetch('/generate_otp', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                messageDiv.textContent = data.message || data.error || 'Something went wrong.';
                messageDiv.className = data.error ? 'error show' : 'success show';
            })
            .catch(error => {
                console.error('Error:', error);
                messageDiv.textContent = 'Failed to send OTP request.';
                messageDiv.className = 'error show';
            });
        });
    }
});*/