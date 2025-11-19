from flask import Flask, send_file, render_template_string
import os

app = Flask(__name__)

# Home page serves index.html
@app.route("/")
def home():
    return send_file("index.html")

# Route to display app.py code
@app.route("/showcode")
def show_code():
    # Make sure app.py exists
    if os.path.exists("app.py"):
        with open("app.py", "r") as f:
            code = f.read()
        # Display code inside <pre> for formatting
        return render_template_string(f"""
            <h2>app.py Code</h2>
            <pre style="background:#f4f4f4;padding:20px;border-radius:8px;white-space:pre-wrap;font-size:15px;">{{{{ code }}}}</pre>
            <a href="/">Back</a>
        """, code=code)
    else:
        return "<h2>app.py not found!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
