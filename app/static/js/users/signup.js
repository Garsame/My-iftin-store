function create_account(event) {
    event.preventDefault();

    // Input data
    var data = {
        first_name: document.getElementById("f_name").value.trim(),
        second_name: document.getElementById("s_name").value.trim(),
        email: document.getElementById("email").value.trim(),
        phone: document.getElementById("phone").value.trim(),
        password: document.getElementById("password").value,
        confirm_password: document.getElementById("confirmPassword").value
    };

    // Error message elements
    var error_msg = document.getElementById('pass_err_msg');
    var success_msg = document.getElementById('success_msg');
    login_visit_msg =document.getElementById('login_visit_msg');
    error_msg.style.display = "none"; // Hide error by default

    // Basic validation
    if (!data.first_name || !data.second_name || !data.email || !data.phone || !data.password || !data.confirm_password) {
        error_msg.style.display = "block";
        error_msg.innerHTML = "Please fill in all fields.";
        return;
    }

    // Email format validation
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(data.email)) {
        error_msg.style.display = "block";
        error_msg.innerHTML = "Please enter a valid email address.";
        return;
    }

    // Phone number format validation (basic example)
    // var phonePattern = /^\d{10,15}$/; // Adjust the pattern based on your requirement
    // if (!phonePattern.test(data.phone)) {
    //     error_msg.style.display = "block";
    //     error_msg.innerHTML = "Please enter a valid phone number.";
    //     return;
    // }

    // Password match validation
    if (data.password !== data.confirm_password) {
        error_msg.style.display = "block";
        error_msg.innerHTML = "Passwords do not match.";
        return;
    }

    // All validations passed, proceed with the server request
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

        // Clear previous messages
        error_msg.style.display = "none";
        success_msg.style.display = "none";

        if (data.status === 'error') {
            error_msg.style.display = "block"; // Show error
            error_msg.innerHTML = data.message; // Display error message from server
        } else if (data.status === 'success') {
            success_msg.style.display = "block"; // Show success message
            success_msg.innerHTML = data.message;
            login_visit_msg.style.display='block'

            // Clear input fields after success
            document.getElementById("f_name").value = "";
            document.getElementById("s_name").value = "";
            document.getElementById("email").value = "";
            document.getElementById("phone").value = "";
            document.getElementById("password").value = "";
            document.getElementById("confirmPassword").value = "";

            // Optionally redirect to the user dashboard
            // window.location.href = '/Users/Dashboard';
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('An error occurred during the signup process.');
    });
}
