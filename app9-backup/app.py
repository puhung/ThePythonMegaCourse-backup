#with request, we could access http request that is being made from the browser and then we can read this request so we can fetch this email address and height.
from os import abort
from flask import Flask, render_template, request,redirect
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import session
from werkzeug.utils import redirect
from send_email import sendEmail
from sqlalchemy.sql import func

app=Flask(__name__)



#setting the value of this dictionary key to this value, so that the app knows wh#Puhung2121ere to look for a database
#this URI is pointing to our local database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://twenet:#puhung2121@localhost/height_collector'

#change this url tp point to the heroku database
#'?sslmode=require' forces the postgresql adopter to require ssl so we can connect the database through cmd
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iggicywkpdhtzp:d9c4c5339624998026a191c1bbe8ed8514534afa24ed15af2dcd2648fd04bdbe@ec2-44-194-112-166.compute-1.amazonaws.com:5432/d5kbe27qmiqevc?sslmode=require'

#create a sqlalchemy object
db = SQLAlchemy(app)

#inheriting from the model class of the SQLAlchemy object
class Data(db.Model):
    #call a class and a table will be created with columns
    __tablename__ = 'data'
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique= True)
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    return render_template("index.html") # with this , we can go the templates folder and get index.html file and render it in the homepage

#implict a get method instead of a post method, thus we also need to define post method
#the email and height are passed to the server as a post method. we also need to capture them inside this success method
@app.route("/success", methods=['GET','POST'])
def success():
    #if the method is post request, we grab that email and return this template
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        

        #we pass the nameof the data class, which is the blueprint that holds the database model to the query
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            #create an object instance of our data class, send the values to the __init__() as parameters. And the data class creates a databse model object 
            data=Data(email,height)
            db.session.add(data)
            #commit the changes to the database
            db.session.commit()
            # a scalar is a number
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            #round the number to 1 decimal point
            average_height = round(average_height, 1)
            # counting the height values that we have in our database table
            count = db.session.query(Data.height_).count()
            sendEmail(email, height, average_height, count)
            return render_template("success.html")
        return render_template("index.html", 
        text = "Seems like we've got something from that email address already!")

#if the script is being executed and not being imported we will execute these lines
if __name__ == '__main__':
    app.debug=True
    app.run()
