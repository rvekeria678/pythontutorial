from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap4
from dotenv import load_dotenv
import os

#----Constants----#
load_dotenv()
#----Globals----#
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    pswd = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    sbmt = SubmitField(label="Log In")

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
bootstrap = Bootstrap4(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.pswd.data == '12345678':
            return render_template('success.html')
        else: return render_template('denied.html')

    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
