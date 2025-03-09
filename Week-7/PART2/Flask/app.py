from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to My Flask App!"

@app.route('/user/<username>')
def user(username):
    return f"Hello, {username}!"

@app.route('/square/<int:num>')
def square(num):
    result = num * num
    return f"The square of {num} is {result}"

@app.route('/post/<int:post_id>')
def post(post_id):
    return f"Viewing Post {post_id}"

if __name__ == '__main__':
    app.run(debug=True)