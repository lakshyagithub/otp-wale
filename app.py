import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from twilio.rest import Client

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='81')
