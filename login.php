<?php
session_start(); // Start the session

$login_error = ""; // Initialize the login error variable

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["school_id"]) && isset($_POST["password"])) {
    $school_id = $_POST["school_id"];
    $password = $_POST["password"];

    // Connect to the database (replace with your database credentials)
    $conn = new mysqli("localhost", "username", "password", "database_name");

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Retrieve user information from the database
    $stmt = $conn->prepare("SELECT id, school_id, password FROM users WHERE school_id = ?");
    $stmt->bind_param("s", $school_id);
    $stmt->execute();
    $stmt->bind_result($user_id, $db_school_id, $hashed_password);
    $stmt->fetch();
    $stmt->close();

    // Verify password
    if ($hashed_password && password_verify($password, $hashed_password)) {
        $_SESSION["user_id"] = $user_id; // Store user ID in the session
        header("Location: home.php"); // Redirect to the home page
        exit();
    } else {
        $login_error = "Invalid school ID or password";
    }

    $conn->close();
}
?>
