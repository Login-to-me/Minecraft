from flask import Flask, render_template_string, request

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Secure Login</title>
    <style>
        body {
            margin: 0;
            background: #f2f2f2;
            font-family: 'Segoe UI', Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .login-box {
            background: #fff;
            width: 380px;
            padding: 45px;
            border-radius: 6px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.12);
            animation: fadeIn 0.6s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h2 {
            margin: 0 0 25px 0;
            font-weight: 600;
            color: #333;
            font-size: 27px;
        }

        input {
            width: 100%;
            padding: 13px;
            margin-bottom: 18px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 15px;
            outline: none;
            transition: 0.2s;
        }

        input:focus {
            border-color: #0067c0;
            box-shadow: 0 0 4px rgba(0,103,192,0.3);
        }

        button {
            width: 100%;
            padding: 13px;
            font-size: 16px;
            background: #0067c0;
            color: white;
            border: none;
            border-radius: 4px;
            transition: 0.25s;
            font-weight: 500;
            cursor: pointer;
        }

        button:hover {
            background: #0059a3;
        }

        .link {
            display: block;
            margin-top: 15px;
            text-decoration: none;
            color: #0067c0;
            font-size: 14px;
        }

        .link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Sign in</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Email, phone, or username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Sign in</button>
        </form>
        <a class="link" href="#">Forgot password?</a>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        # Demo-only login check
        if user == "admin" and pwd == "1234":
            return "<h1>Login successful!</h1>"
        else:
            return "<h1>Invalid login</h1>"

    return render_template_string(html_page)

if __name__ == "__main__":
    app.run(debug=True)
