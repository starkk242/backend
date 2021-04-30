from flask import Flask, render_template,request,redirect
import hashlib
import codecs
import rsa
from db_connect import connect

app = Flask(__name__)

@app.route("/")
def home():
    return "Not Allowed"

@app.route("/send_data",methods=['POST'])
def send_data():
    mydb=connect()
    mycursor=mydb.cursor()
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

    sql="INSERT INTO customers (fname,lname,email,password,gender) values (%s,%s,%s,%s,%s)"
    val=(fname_hash,lname_hash,email_hash,paswd_hash,gender_hash)
    mycursor.execute(sql,val)
    mydb.commit()

    host=request.headers['Referer']
    return redirect(host+"login_page")

@app.route('/auth',methods=["POST"])
def auth():
    mydb=connect()
    mycursor=mydb.cursor()

    email=request.form['email']
    email_hash=codecs.encode(email,'rot13')

    password=request.form['password']
    paswd_hash = hashlib.md5(password.encode()).hexdigest()

    sql='SELECT password from customers where email = %s'
    val=(email_hash,)
    mycursor.execute(sql,val)
    f=mycursor.fetchall()

    if f[0][0]==paswd_hash:
        return "Login Success"
    return "Login Error"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)