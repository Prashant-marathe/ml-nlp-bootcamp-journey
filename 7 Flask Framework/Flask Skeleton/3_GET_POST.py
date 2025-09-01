from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>This is home page'

# methods is the second parameter in @app.route() it takes http methods. if nothing is given it defaults to GET
@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# using Post request
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)