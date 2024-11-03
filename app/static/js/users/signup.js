function create_account(event) {
    event.preventDefault();

    var data = {
        first_name: document.getElementById("f_name").value,
        second_name: document.getElementById("s_name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        password: document.getElementById("password").value,
        confirm_password: document.getElementById("confirmPassword").value
    };
    

    // Error message
    var error_msg = document.getElementById('pass_err_msg');
    var success_msg = document.getElementById('success_msg');

    fetch('/getData_signup', {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json()) // Parse JSON response
    .then(data => {
        console.log('Server Response:', data);

        // Hide any previous error message before processing the new response
        error_msg.style.display = "none";

        if (data.status === 'error') {
            error_msg.style.display = "block"; // Make it visible
            error_msg.innerHTML = data.message; // Display the error message from Flask
        } else if (data.status === 'success') {
            // Handle successful login
            // alert('Xogtaadu way saxan tahay , Mahadsanid.');
            success_msg.style.display = "block"; // Make it visible
            success_msg.innerHTML = data.message; // Display the error message from Flask


             // Clear input fields
            document.getElementById("f_name").value = "";
            document.getElementById("s_name").value = "";
            document.getElementById("email").value = "";
            document.getElementById("phone").value = "";
            document.getElementById("password").value = "";
            document.getElementById("confirmPassword").value = "";


            // window.location.href = '/Users/Dashboard'; // Redirect to user dashboard
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('An error occurred during the login process.');
    });
}