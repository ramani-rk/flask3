from flask import Flask,request,render_template
from flask_wtf import Form
# FORM package is used to create the forms in FLASK.. it is inside in flask_wtf module...

from wtforms import StringField,SubmitField
# In FLASK, We want to import Stringfield for entering texts and Submitfield for submitting the data.

FAI=Flask(__name__)


# In FLASK, there is no inbuild forms. so, we mention methods
@FAI.route('/htmlform',methods=['GET','POST'])
def htmlform():
    if request.method=='POST':

# This request method is not in the package, bcoz it comes with data so we want to import
        FD=request.form
        return FD['un']
    return render_template('htmlform.html')


# This class is used to create Text box & Submit button manually
class NameForm(Form):
    name=StringField()
    submit=SubmitField()


@FAI.route('/webform',methods=['GET','POST'])
def webform():
    NFO=NameForm()

    if request.method=='POST':
        NFDO=NameForm(request.form)

        if NFDO.validate():
            return NFDO.name.data
    return render_template('webform.html',NFO=NFO)

# In return, NFO is context.


if __name__=='__main__':
    FAI.run(debug=True)

    
    # FAI.run(debug=True,host='192.168.1.11',port=5001)

    # This is used for changing the HOST address & Port number for the server