from my_app import app

app.config.from_object('config.configuration') 

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True) 
