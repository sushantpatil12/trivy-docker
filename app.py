from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    
    return "<html><h1>WELCOME TO LINUX2</h1></html>"

app.run(host="0.0.0.0",port=8080,debug=True)
