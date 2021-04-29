from flask import Flask, render_template,request
import hashlib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('landing.html')

@app.route("/send_data",methods=['POST'])
def send_data():
    first_name=request.form['fname']
    fname_hash=hashlib.md5(first_name.encode()).hexdigest()

    last_name=request.form['lname']
    lname_hash=hashlib.md5(last_name.encode()).hexdigest()

    email=request.form['email']
    email_hash=hashlib.md5(email.encode()).hexdigest()

    password=request.form['password']
    paswd_hash = hashlib.md5(password.encode()).hexdigest()

    gender=request.form['gender']
    gender_hash=hashlib.md5(gender.encode()).hexdigest()

    return "%s  %s  %s  %s  %s"%(fname_hash,lname_hash,email_hash,paswd_hash,gender_hash)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)