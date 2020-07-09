from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    submit = SubmitField('Enter')


class UserIDForm(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    submit = SubmitField('Confirm')


class UpdateUserForm(FlaskForm):
    user_id = IntegerField('Enter User ID', validators=[DataRequired()])
    first_name = StringField('New First Name', validators=[DataRequired()])
    age = IntegerField('New Age', validators=[DataRequired()])
    submit = SubmitField('Enter')