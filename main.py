from flask import Flask, flash, request, redirect, url_for, render_template, jsonify

app = Flask(__name__)

app = Flask(__name__)

@app.route('/')  # Route the Function
def main():  # Run the function
    return render_template('index.html')

app.run(host='0.0.0.0', port=5000,debug=True)