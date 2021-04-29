from flask import Flask, render_template,request,redirect
import hashlib
import codecs
import rsa

app = Flask(__name__)

@app.route("/")
def home():
    return "Not Allowed"

@app.route("/send_data",methods=['POST'])
def send_data():
    first_name=request.form['fname']
    fname_hash=codecs.encode(first_name,'rot13')

    last_name=request.form['lname']
    lname_hash=codecs.encode(last_name,'rot13')

    email=request.form['email']
    email_hash=codecs.encode(email,'rot13')

    password=request.form['password']
    paswd_hash = hashlib.md5(password.encode()).hexdigest()

    gender=request.form['gender']
    gender_hash=codecs.encode(gender,'rot13')

    host=request.headers['Referer']

    return redirect(host)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)