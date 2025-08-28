from flask import Flask

'''
app = Flask() : it creates a instance of the Flask class, which will be your WSGI (Web Server Gateway Interface) application.
'''
app = Flask(__name__)

# Create routes
@app.route("/")
def welcome():
    return '<h1>Welcome to this flask course. This is going to be fun.</h1>'

@app.route('/index')
def index():
    return 'welcome to the index page'

@app.route('/contact')
def contact():
    return 'Welcome to the contact page.'





# start the flask app
if __name__ == "__main__":
    app.run(debug=True)