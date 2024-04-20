from flask_wtf import FlaskForm
from wtforms import StringField,  TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class Classe(FlaskForm):
      name = StringField("Name", validators=[DataRequired()])
      submit = SubmitField("Submit")
      
class Etudiant(FlaskForm):
      name = StringField("Name", validators=[DataRequired()])
      nameC = StringField("NameC", validators=[DataRequired()])
      submit = SubmitField("Submit")