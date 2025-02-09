from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome to Cyber-Sim Dashboard!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
