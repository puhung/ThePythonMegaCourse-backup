# import Flask class object from the flask library
#the render_template method of the flask library accessses an html file stored in our python application, file
from flask import Flask, render_template

# instatiating the class the object
app = Flask(__name__)


#you can find this website at " http://localhost:5000/ "
@app.route('/')
#the output of this "home" function will be mapped to the above URL
def home():
    return render_template("home.html") #access an real html file stored in a folder which is called "templates"

#route = decorator. you can find this website at " http://localhost:5000/about/ "
# the ouput of the about() function will be mapped to this URL 
@app.route('/about/')
# this function name, which is "about" function, can not be the same as the above
def about():
    return render_template("about.html")

@app.route('/gallery/')
# this function name, which is "about" function, can not be the same as the above
def gallery():
    return render_template("gallery.html")

# if we excecuted this "script1.py" file, python assigns the name "__main__" to the file => "__name__" == "__main__"
# else we import this "script1.py" from other file, we don't "__name__" !== "__main__"
if __name__ == "__main__":
    app.run(debug = True)
    