from flask import Flask, render_template

# Create a WSGI server
app = Flask(__name__)

# Create Routes
@app.route('/')
def home():
    return '<b>Welcome to the home page.</b>'

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)