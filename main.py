from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/send_data")
def send_data():
	return "Hello Me"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)

