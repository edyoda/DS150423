from flask import Flask

app = Flask(__name__)

@app.route("/edyoda/bharati")
def greet():
    return {"greet":"Hello"}

app.run()