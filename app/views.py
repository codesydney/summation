from flask import render_template, render_template, redirect, url_for
from app import app
from .forms import InputForm, ResultForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    inputform = InputForm()
    resultform = ResultForm()
	
    if inputform.validate_on_submit() and inputform.Submit1.data:
        number1 = inputform.Number1.data
        number2 = inputform.Number2.data
        sum = number1 + number2
        return render_template('resultpage.html',   
                              resultform=resultform,
                              number1=number1,
                              number2=number2,
                              sum=sum)                                
    elif resultform.validate_on_submit() and resultform.Submit2.data:	
        return redirect(url_for('index'))
    else:
        return render_template('inputpage.html',
                              inputform=inputform)