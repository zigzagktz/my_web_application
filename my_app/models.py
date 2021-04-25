from my_app import *

def hello():
    return str(session['username'])

def register(username, password,email):
    if len(username) > 0 and  len(password) >0 and len(email) > 0:
        username = username
        password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
        email = email
        
        conn = sqlite3.connect("students.db")
        cur = conn.cursor() 
        cur.execute("create table if not exists accounts (id integer PRIMARY KEY, email text, username text, password text)")
        cur.execute('select * from accounts')
        result = cur.fetchall()
        if len(result) == 0:
            cur.execute("Insert into accounts VALUES (Null, '{}','{}','{}')".format(email,username,password.decode('utf-8')))
            cur.connection.commit()
            cur.connection.close()
            msg = "registaration success first" 
        else:
            for row in result:
                if row[1] == email:
                    msg = "email exists"
                    break
                elif row[2] == username:
                    msg = "username exists"
                    break
                else:
                    cur.execute("Insert into accounts VALUES (Null, '{}','{}','{}')".format(email,username,password.decode('utf-8')))
                    cur.connection.commit()
                    cur.connection.close()
                    msg = "registeration success"
                    break
    else:
        msg = "Please fill all credentials"
    return msg

def login(email, password):
    email=email
    password=password
    if len(email)>0 and len(password)>0:
        conn = sqlite3.connect("students.db")
        cur = conn.cursor()
        cur.execute("create table if not exists accounts (id integer PRIMARY KEY, email text, username text, password text)")
        cur.execute("SELECT * from accounts where email = '{}' ".format(email))
        account = cur.fetchall()
        cur.connection.close()
        if account and bcrypt.checkpw(password.encode('utf-8'),account[0][3].encode('utf-8')):
            session["loggedin"] = True
            session["id"] = account[0][0]
            session["username"] = account[0][2]  
            session.permanent = True
            msg = "success"
        else:
            msg =  "incorrect" 
    else: 
        msg = "missing"
    return msg, session

def home():
    plot = figure(plot_height=300, plot_width=400)
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [2**v for v in x]     
    plot.line(x, y, line_width=8,color="navy", alpha=0.5)
    script, div = components(plot)  
    try: 
        if session['username']:
            return script, div
            #return jsonify(query.data())
        else:
            return "timeout"
    except:
        return "timeout"

def logout():
    session.pop("loggedin",None)
    session.pop("id",None)
    session.pop("username",None)
    
    msg = "logged out"
    return msg

