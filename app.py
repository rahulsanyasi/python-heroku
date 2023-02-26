from flask import Flask

app = Flask(__name__)

@app.route("/")
def show_landing_page() -> str:
    print("Inside the landing page")
    print("Will write more logic later on.")
    return "Hello from Rahul on the landing page v.0.0.2!"

@app.route("/ghar-thane")
def home() -> str:
    print("Inside ghar-thane.")
    print("Will write more logic later on.")
    return "Hello from Rahul inside home Function v.0.0.2!"

@app.route("/store")
def shop() -> str:
    print("Inside shop")
    print("Will write more logic later on.")
    return "Hello from Rahul inside shop Function v.0.0.3!"