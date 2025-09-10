from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home Page</h1><p>Welcome to my Flask App!</p>"

@app.route("/about")
def about():
    return "<h1>About</h1><p>This is served from EC2 using Flask.</p>"

@app.route("/contact")
def contact():
    return "<h1>Contact</h1><p>You can reach me at example@email.com</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

