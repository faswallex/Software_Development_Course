from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
     return render_template('index.html')
# def greet():
    # return render_template('greet.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

#  GET USER INPUT
@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['name']
    email = request.form['email']
    return render_template('hello.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)