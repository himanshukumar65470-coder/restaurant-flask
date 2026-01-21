from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Himanshu Dhaba</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f2f2f2;
        }
        header {
            background: #d35400;
            color: white;
            padding: 25px;
            text-align: center;
        }
        nav {
            background: #222;
            padding: 12px;
            text-align: center;
        }
        nav a {
            color: white;
            margin: 15px;
            text-decoration: none;
            font-weight: bold;
        }
        .container {
            padding: 20px;
        }
        .menu-item {
            background: white;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 8px;
            box-shadow: 0 0 5px rgba(0,0,0,0.1);
        }
        .menu-item h3 {
            margin: 0;
            color: #d35400;
        }
        footer {
            background: #111;
            color: white;
            text-align: center;
            padding: 20px;
            margin-top: 20px;
        }
        .btn {
            display: inline-block;
            background: #d35400;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            margin-top: 10px;
        }
    </style>
</head>

<body>

<header>
    <h1>🍽 Himanshu Dhaba 🍽</h1>
    <p>Fresh Food • Best Taste • Family Restaurant</p>
</header>

<nav>
    <a href="#">Home</a>
    <a href="#">Menu</a>
    <a href="#">About</a>
    <a href="#">Contact</a>
</nav>

<div class="container">
    <h2>🔥 Our Special Menu</h2>

    <div class="menu-item">
        <h3>Paneer Butter Masala</h3>
        <p>₹250</p>
    </div>

    <div class="menu-item">
        <h3>Chicken Biryani</h3>
        <p>₹300</p>
    </div>

    <div class="menu-item">
        <h3>Dal Tadka</h3>
        <p>₹180</p>
    </div>

    <div class="menu-item">
        <h3>Veg Thali</h3>
        <p>₹150</p>
    </div>

    <a class="btn" href="tel:7644088467">📞 Call to Order</a>
</div>

<footer>
    <p>📍 Address: siwan (Bihar), baghra</p>
    <p>📞 Phone: 7644088467</p>
    <p>© 2026 Himanshu Dhaba</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
