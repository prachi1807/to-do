from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    is_complete = db.Boolean()

@app.route('/')
def index():
    todo_list = ToDo.query.all()
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)


def add():
    """Add new items."""
    title = request.form.get('title')
    new_todo = ToDo(title=title, is_complete=False)
    db.session.add(new_todo)
    db.session.commit()




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # new_todo = ToDo(title='ToDo1', is_complete=False)
        # db.session.add(new_todo)
        # db.session.commit()

    app.run(debug=True)