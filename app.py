
from flask import Flask, render_template, request, redirect, url_for
from models import db, Task
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    pending_tasks = Task.query.filter_by(completed=False).order_by(Task.due_date).all()
    completed_tasks = Task.query.filter_by(completed=True).order_by(Task.completed_date.desc()).all()
    return render_template('index.html', pending_tasks=pending_tasks, completed_tasks=completed_tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    due_date = request.form.get('due_date', None)
    due_date = datetime.strptime(due_date, '%Y-%m-%d').date() if due_date else None
    new_task = Task(title=title, due_date=due_date)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = True
    task.completed_date = datetime.now()
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
