from my_app import app

app.config.from_object('config.configuration') 

app.run('0.0.0.0',debug=True)