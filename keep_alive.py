import os
from flask import Flask
from threading import Thread
port = os.environ['port']

app = Flask('')

@app.route('/')
def home():
    return "why are u here"

def run():
  app.run(host='0.0.0.0',port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()