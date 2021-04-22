from my_app import app
from my_app.models import hello
from my_app import models
from my_app import *

@app.route("/")
def hello(): 
    return models.hello()

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    elif request.method=="POST":
        username, password, email = request.form["username"], request.form["password"], request.form["email"]
        message = models.register(username,password,email)
        return render_template("/home.html",msg=message)


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    elif request.method=="POST":
        username = request.form["email"]
        password = request.form["password"]
        message = models.login(username, password)
        if message=="success":
            return  message
            #return redirect(url_for("data"))
            #return redirect(url_for("visual"))
        elif message=="incorrect":
            return "incorrect credentials"
        elif message=="missing":
            return "please fill all credentials"

@app.route("/visual", methods=["GET","POST"])
def visual():
    if models.home() == "timeout":
        return "please loggin again"
    else:
        script, div =  models.home()
        return render_template("home.html",the_script=script, the_div=div)

@app.route("/data/<param>", methods=["GET","POST"])
@cache.memoize(20)
def data(param):
    dataset = fetch_data.data()
    return jsonify(dataset[0:int(param)])

@app.route("/logout", methods=["GET","POST"])
def logout():
    return models.logout()