from flask import Flask, request, redirect, render_template_string
import os

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None  # Initialize error variable

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are correct
        if username == 'HENRY_BECKUP__cxeeexx' and password == 'HENRY X SAMAR 786':
            # Redirect to the specified link if login is successful
            return redirect('https://generous-consuelo-zohan-de05fc44.koyeb.app/')
        else:
            error = 'Invalid username or password. Please try again.'

    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Henry Server</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Popins, sans-serif;
            background-image: url('https://i.imgur.com/0pjiKK8.jpeg');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 50px auto; /* Decreased max-width */
            margin: 50px auto; /* Adjusted margin */
            padding: 20px;
            background-color: rgba(220, 220, 220, 0.5); /* Transparent white background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        h1 {
            text-align: center;
            color: white;
            border: 1.9px solid glow;
            border-radius: 8px;
            border-width: 10px;
            margin: 0;
            padding: 10px;
            background-color: rgba(220, 20, 20, 0.5); /* Transparent red background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #fff;
            font-size: 28px;
            margin-bottom: 20px;
            text-shadow: 0 0 10px #000;
        }

        /* Blinking Sukhi Server heading */
        .sukhi-server {
            font-size: 32px;
            color: #ff5e5e;
            animation: blink 1.5s infinite;
            font-weight: bold;
            margin-bottom: 20px;
        }

        @keyframes blink {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0;
            }
        }

        input {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 16px;
            background-color: rgba(255, 255, 255, 0.9);
        }

        form {
        display: flex;
        flex-direction: column; /* Arrange children in a column */
        align-items: center;    /* Center items horizontally */
        }
        
        button {
        width: auto;            /* Change to auto for centered width */
        padding: 12px 20px;     /* Adjust padding for better appearance */
        background-color: #007bff;
        color: #fff;
        border: none;
        cursor: pointer;
        border-radius: 8px;
        margin-top: 15px;
        font-weight: bold;
        font-size: 16px;
        transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #0056b3;
        }

        .admin-contact {
            margin-top: 20px;
            color: #fff;
        }

        .admin-contact a {
            color: #00ff00;
            font-weight: bold;
            text-decoration: none;
        }

        .error-message {
            color: red;
            font-size: 14px;
            margin-top: 10px;
            font-weight: bold;
        }
    </style>
</head>
<body>


    <div class="container">
    <div class="content">
    <h1>Official WEB HENRY X SAMAR</h1>
        <img src="https://i.imgur.com/CVTUtN2.jpeg" style="width: 100%; height: auto; border-radius: 12px;">
        <h1>Beckup CONVO</h1>
        <h2 class="henry-server">HENRY X SAMAR PAID 😈</h2>
        <form action="/" method="POST">  <!-- Changed to / -->
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        {% if error %}
        <div class="error-message">{{ error }}</div>  <!-- Display the error message -->
        {% endif %}
        <div class="admin-contact">
            <p>Need help? <a href="https://wa.me/+919235741670" target="_blank">Contact Admin</a></p>
        </div>
    </div>
</body>
</html>
    ''', error=error)  # Pass the error to the template

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
