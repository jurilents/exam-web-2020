from flask import Flask, request
from flask import render_template, redirect
from flask_sqlalchemy import SQLAlchemy

# ========================================= #
# ============== CREATING APP ============= #
# ========================================= #

app = Flask(__name__)

# =========== DATABASE SETTINGS =========== #

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///core/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# ========================================= #
# ============ DATABASE MODELS ============ #
# ========================================= #


class TemplateObject(db.Model):
    __tablename__ = 'template'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    # messages = db.relationship('Message', primaryjoin='User.id==Message.owner')

    def __init__(self, name):
        self.name = name.strip()

    def __repr__(self):
        print(f'{self.id}: {self.name}')


def init_db():
    with app.app_context():
        db.create_all()

    objects = [
        TemplateObject("Hello World!!!"),
        TemplateObject("Lorem Ipsum"),
        TemplateObject("Qwerty 1234 4321 123 321")
    ]

    for obj in objects:
        db.session.add(obj)
    db.session.commit()


init_db()


# ========================================= #
# ============== APP ROUTING ============== #
# ========================================= #

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {
        'data': TemplateObject.query.filter().all()
    }
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    return render_template('index.html', result=result)


if __name__ == "__main__":
    app.run()
