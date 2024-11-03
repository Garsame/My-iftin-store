function get_data() {
    var my_email = document.getElementById("user_email").value;
    var my_pass = document.getElementById("user_pass").value;

    var error_msg = document.getElementById('pass_err_msg');

    var data = {
        email: my_email,
        password: my_pass
    };

    fetch('/getData_login', {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(data),
        cache: 'no-cache',
        headers: new Headers({
            'content-type': 'application/json'
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Server Response:', data);

        error_msg.style.display = "none";

        if (data.status === 'error') {
            error_msg.style.display = "block";
            error_msg.innerHTML = data.message;
        } else if (data.status === 'success') {
            window.location.href = '/Users/Dashboard';
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('An error occurred during the login process.');
    });
}
