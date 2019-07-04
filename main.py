from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods = ['GET'])
def sign_up():
    return render_template("form.html")

@app.route('/validate', methods = ['POST'])
def validate_sign_up():
    user_name = request.form['user_name']
    email_address = request.form['email_address']
    password = request.form['password']
    conf_password = request.form['confirm_password']

    user_error = ''
    email_error = ''
    password_error = ''
    dont_match = ''

    if ' ' in user_name:
        user_error = 'User name should not contain Spaces.'
    if len(user_name) < 3:
        user_error = 'user name should not be shorter than 3 characters.'
    if len(user_name) > 20:
        user_error = 'User name should not be longer than 20 characters.'
    if  '@' not in email_address or  '.' not in email_address or len(email_address) < 3 or len(email_address) > 20:
        if email_address:
            email_error = 'Please input a valid Email address'
    if ' ' in password:
        password_error = 'Password should not contain Spaces.'
    if len(password) < 3:
        password_error = 'Password should not be shorter than 3 characters.'
    if len(password) > 20:
        password_error = 'Password should not be longer than 20 characters.' 
    if password != conf_password:
        dont_match = 'Passwords do not match'
    if len(user_error)  or len(email_error)  or len(password_error)  or len(dont_match):
        user_name=user_name.replace(" ", "-")
        #print("KokoHere")
        #print(user_name)
        return render_template("form.html",user_name=user_name.replace("-", " "),email_address=email_address,user_error=user_error,password_error=password_error,email_error=email_error,
            dont_match=dont_match)
    else:
        return render_template("welcome.html",user_name=user_name)


#@app.route('/welcome', methods =[ 'GET'])
#def welcome():
#    user_name = request.args['user_name']
#    return render_template("/welcome.html",user_name=user_name)


if __name__=='__main__':
    app.run()