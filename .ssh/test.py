# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


#@app.route('/')
#def hello():
    #return render_template('hello.html')

@app.route('/')
def hello():
    return render_template('sample.html')

def main():
    app.debug = True
    app.run(host='127.0.0.1', port=8080)

if __name__ == '__main__':
    main()