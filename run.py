from app import app
from auth import auth 

app.register_blueprint(auth)


if __name__== '__main__':
    app.run(debug=True)
