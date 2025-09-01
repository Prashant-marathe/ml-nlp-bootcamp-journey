# Building url dynamically
# variable rule


# jinja2 template engine
'''
{{  }} expressions to print output in html
{%  %} conditions, for loops  {% for %} {% endfor %}
{#  #} this is for comments
'''

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>This is home page</h1>'


@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/submit")
def submit():
    if request.method == "POST":
        name = request.form['name']
        return f'Hello {name}'
    return render_template("form.html")

#* Variable Rule: it takes string variables by default. You can use converters like <int:...>, <float:...>, etc to take another variable types
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 55:
        res = "Passed"
    else:
        res = "Failed"

    exp = {
        "res":res,
        "score":score
    }
    return render_template('result.html', exp=exp)


#* using for loop in html template
@app.route("/fruitbasket")
def fruitbasket():
    fruits = ['Apple', 'Banana', 'Cherry', 'Dragonfruit', 'Grapes' , 'Mango', 'Pineapple']
    return render_template('fruits.html', fruits=fruits)

#* using if condition in html template
@app.route("/successif/<int:score>")
def successif(score):
    return render_template('result.html', score=score)

@app.route("/successres")
def successres():
    return render_template('getresults.html')

@app.route("/getresults", methods=['POST', 'GET'])
def getresults():
    if request.method == 'POST':
        maths = float(request.form['maths'])
        english = float(request.form['english'])
        c = float(request.form['c'])
        datascinece = float(request.form['datascinece'])

    average = (maths + english + c + datascinece) / 4
    return redirect('/success', score = average)






if __name__ == "__main__":
    app.run(debug=True)