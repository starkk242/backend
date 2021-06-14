from flask import Flask, render_template,request,redirect
import hashlib
from flask.wrappers import Response
from db_connect import connect

app = Flask(__name__)

@app.route("/")
def home():
    return "Not Allowed"

@app.route("/send_data",methods=['POST'])
def send_data():
    mydb=connect()
    mycursor=mydb.cursor()

    phone_number=request.form['phone_number']
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    paswd_hash = hashlib.md5(password.encode()).hexdigest()

    sql="INSERT INTO customers (phone_number,name,email,password) values (%s,%s,%s,%s)"
    val=(phone_number,name,email,paswd_hash)
    mycursor.execute(sql,val)
    mydb.commit()

    return Response("Registration Complete")

@app.route('/auth',methods=["POST"])
def auth():
    mydb=connect()
    mycursor=mydb.cursor()

    phone_number=request.form['phone_number']

    password=request.form['password']
    paswd_hash = hashlib.md5(password.encode()).hexdigest()

    sql='SELECT password from customers where phone_number = %s'
    val=(phone_number,)
    mycursor.execute(sql,val)
    f=mycursor.fetchall()

    if f[0][0]==paswd_hash:
        return "Login Success"
    return "Login Error"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)