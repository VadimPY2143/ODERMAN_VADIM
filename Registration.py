import flask_wtf
import wtforms

class RegistrationForm(flask_wtf.FlaskForm):
    email = wtforms.StringField('E-mail', validators=[wtforms.validators.InputRequired()])
    password = wtforms.PasswordField('Password', validators=[wtforms.validators.InputRequired()])
    submit = wtforms.SubmitField('Subscription')
    remember = wtforms.BooleanField('Remember me')