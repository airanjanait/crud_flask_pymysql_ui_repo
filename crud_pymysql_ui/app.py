from flask import Flask,render_template,request,redirect
import pymysql
con=pymysql.connect(host="localhost",password="",user="root",database="registration")
app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        full_name=request.form.get("full_name")
        email=request.form.get("email")
        password=request.form.get("password")
        retype_password=request.form.get("retype_password")
        with con.cursor() as cur:
            query="insert into registraion_table(full_name,email,password,retype_password) values(%s,%s,%s,%s)"
            value=(full_name,email,password,retype_password)
            cur.execute(query,value)
    return render_template("register.html")

@app.route("/table")
def table():
    with con.cursor() as cur: 
        query="select * from registraion_table"
        cur.execute(query)
        data=cur.fetchall()
    return render_template("table.html",data=data)



@app.route("/fetchbyid/<re_id>",methods=["POST","GET"])
def fetch(re_id):
    if request.method=="POST":
        full_name=request.form.get("full_name")
        email=request.form.get("email")
        password=request.form.get("password")
        retype_password=request.form.get("retype_password")
        with con.cursor() as cur:   
            query="update registraion_table set full_name=%s,email=%s,password=%s,retype_password=%s where re_id=%s"
            print(query)
            value=(full_name,email,password,retype_password,re_id)
            cur.execute(query,value)
            print(cur.execute)
            con.commit()
            return redirect("/table")
    if request.method=="GET": 
        with con.cursor() as cur: 
            sql="select * from registraion_table where re_id=%s" 
            value=re_id
            cur.execute(sql,value)
            row=cur.fetchone()   
            print(row)
            con.commit()    
        return render_template("update_register.html",row=row)
    

@app.route("/deletebyid/<re_id>")
def delete(re_id):
    with con.cursor() as cur:
        delete="delete from registraion_table where re_id=%s"
        cur.execute(delete,re_id)
        return redirect("/table")


if __name__=="__main__":
    app.run(debug=True)