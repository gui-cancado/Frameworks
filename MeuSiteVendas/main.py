from flask import Flask
from flask import send_file
app  = Flask(__name__)

@app.route("/")
def inicio ():
    #return "<h1>Olá Mundo</h1>"
    return send_file("index.html")

app.run(host="0.0.0.0", port=5000, debug=True)
