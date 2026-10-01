from auth import auth
from flask import render_template

@auth.route('/auth')
def auth():
    return render_template('index1.html')

