from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
   return "Welcome Yashas How are you and Welcome Boy and always remember family first"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
