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
        if username == 'HENRY_SAMAR' and password == 'HENRY X SAMAR 786':
            # Redirect to the specified link if login is successful
            return redirect('https://apk-serverxdts-projects.vercel.app/')
        else:
            error = 'Invalid username or password. Please try again.'

    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Sukhi Server</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-image: url('https://i.ibb.co/k0FrLnh/Snapinsta-app-446585272-465721035974161-7203544009380796951-n-1080.jpg');
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
        label {
            font-weight: bold;
            color: auto;
            display: block;
            margin: 15px 0 5px;
        }
        .input {
            margin: 10px;
            background-color: rgba(220, 220, 220, 0.5) ;
            border: none;
            outline: none;
            max-width: 360px;
            padding: 20px 30px;
            font-size: 10px;
            border-radius: 9999px;
            box-shadow: inset 2px 5px 10px rgb(5, 5, 5);
            color: #fff;
        }
        input[type="text"], input[type="number"], input[type="file"] {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .submit-btn {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .submit-btn:hover {
            background-color: #b0b300;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: cyan;
        }
    </style>
</head>
<body>

    <div class="container">
    <div class="content">
        <img src="https://i.imgur.com/bSHJtut.png" style="width: 100%; height: auto; border-radius: 12px;">
        <h1>Officail WEB</h1>
        <h2 class="henry-server">HENRY X SAMAR SERVERS</h2>
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
