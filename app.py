import json
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
    courseId = db.Column(db.String(150), primary_key=True)
    courseFullName = db.Column(db.String(150), nullable=False)
    units = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(2000), nullable=False)


@app.route('/',methods = ['GET'])
def home():
    return "<h1>Server running...ig, idk</h1>"

@app.route('/api/<course_id>',methods = ['GET'])
def get_course_details(course_id):
    print(course_id)
    course = db.get_or_404(Courses, course_id)
    ans = {
        "courseFullName": course.courseFullName,
        "units" : course.units,
        "description" : course.description
    }
    return ans

if __name__ == "__main__":
    app.run()