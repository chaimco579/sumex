# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/mydatabase'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

# Create the application context
with app.app_context():
    # Initialize the database tables
    db.create_all()

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        with app.app_context():
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()

        return redirect(url_for('hello', name=name))

@app.route('/users')
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    with app.app_context():
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
    return redirect(url_for('show_users'))

@app.route('/delete_users', methods=['POST'])
def delete_users():
    if 'delete_user' in request.form:
        user_id = int(request.form['delete_user'])
        with app.app_context():
            user = User.query.get(user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
    return redirect(url_for('show_users'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
