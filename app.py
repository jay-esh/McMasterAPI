from flask import Flask, request, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "HACKTOBER"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)

cors  = CORS(app, resources={r"/api/*": {"origin": "*"}})

class Courses(db.Model):
    cousreId = db.Column(db.String(50), primary_key=True)
    courseFullName = db.Column(db.String(150), nullable=False)
    units = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(600), nullable=False)


@app.route('/',methods = ['GET','POST'])
def home():
    return "<h1>Server running...ig, idk</h1>"


if __name__ == "__main__":
    app.run()