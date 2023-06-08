from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'SatsPay Session!'

@app.route('/about')
def about():
    return 'About'

@app.route('/<fiat>')
def dynamic_endpoint(fiat):
    # Access the value of fiat parameter
    return f"Endpoint for {fiat}"
