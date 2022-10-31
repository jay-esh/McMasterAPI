from app import app, db, Courses

with app.app_context():
    c = Courses.query.get("COMPSCI 2LC3")
    print(c.description)
    # for i in Courses.query.all():
    #     print(i.courseId)
