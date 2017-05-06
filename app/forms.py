from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired

class InputForm(Form):
	InputFormTitle = StringField("Input two numbers")
	Number1 = IntegerField('Number1', [validators.Required("Enter first number")],render_kw={"placeholder": "","size":"10"})	
	Number2 = IntegerField('Number2', [validators.Required("Enter second number")],render_kw={"placeholder": "","size":"10"})	
	Submit1 = SubmitField('Submit',render_kw={"size":"90"})	    
 
class ResultForm(Form):
    Submit2 = SubmitField('Try again',render_kw={"size":"90"})	 
    