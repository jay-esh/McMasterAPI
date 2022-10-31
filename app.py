import json
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
# from flask_swagger_ui import get_swaggerui_blueprint
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "HACKTOBER"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

db = SQLAlchemy(app)
db.init_app(app)

cors = CORS(app, resources={r"/api/*": {"origin": "*"}})

class Courses(db.Model):
    courseId = db.Column(db.String(150), primary_key=True)
    courseFullName = db.Column(db.String(150), nullable=False)
    units = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(2000), nullable=False)

class Home(Resource):
    def get(self):
        return {"about" : "Its a cool api"}

class CourseDetails(Resource):
    def get(self, id):

        course = db.get_or_404(Courses, id.capitalize())
        ans = {
            "courseFullName": course.courseFullName,
            "units": course.units,
            "description": course.description
        }
        return jsonify(ans)

api.add_resource(Home, '/')
api.add_resource(CourseDetails, '/api/<string:id>')


if __name__ == "__main__":
    app.run()
