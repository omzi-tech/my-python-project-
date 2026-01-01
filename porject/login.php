<?php
// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve username and password from form
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Your authentication logic here (e.g., querying a database)
    // Example: For demonstration purposes, checking against hardcoded values
    $valid_username = 'user';
    $valid_password = 'password';

    if ($username == $valid_username && $password == $valid_password) {
        // Authentication successful
        echo "Login successful. Welcome, $username!";
        // Redirect to a dashboard or another page
        // header('Location: dashboard.php');
        // exit;
    } else {
        // Authentication failed
        echo "Invalid username or password.";
    }
}
?>
