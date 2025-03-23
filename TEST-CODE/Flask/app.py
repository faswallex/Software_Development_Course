# from flask import Flask, render_template 

# app = Flask(__name__)
# @app.route('/')
# @app.route('/home')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
#  @app.route('/greet', methods=['GET', 'POST'])
# def greet():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         return render_template('greet.html', name=name)
#     return render_template('greet.html', name=None)
 
# if __name__ == '__main__':
#     app.run(debug=True)

# WEEK7PART1
# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/')
# # def home():
# #     return "Welcome to My Flask App!"
# def greet():
#     return render_template('greet.html')


# @app.route('/about')
# def about():
#     return "This is the About Page"

# @app.route('/contact')
# def contact():
#     return "Contact us at contact@example.com"

# if __name__ == '__main__':
#     app.run(debug=True)
    
# WEEK8 SAMPLE

# NOT WORKING
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
     return render_template('index.html')
# def greet():
    # return render_template('greet.html')


@app.route('/about')
def about():
    return "This is the About Page"

@app.route('/contact')
def contact():
    return "Contact us at contact@example.com"

# GET USER INPUT
app.route('/hello', methods=['POST'])
def hello():
    name = request.form['name']
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)

# WEEK8 SAMPLE

# WORKING 
# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         name = request.form['name']  # Get form data
#         return render_template('hello.html', name=name)
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
