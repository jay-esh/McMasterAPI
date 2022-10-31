from app import app, db, Courses
import csv


def getKey(str):
    l = str.split()
    key = l[0] + ' ' + l[1]
    return key

# content = content.split("\n", 3)


def parseDesc(str):
    l = str.split("\n", 3)
    courseFullName = l[0]
    units = l[1]
    description = l[2]
    return [courseFullName, units, description]


with app.app_context():
    db.create_all()
    with open('courseData.csv') as f:
        csv_reader = csv.reader(f)
        line_count = 0
        dataadded = 0
        for row in csv_reader:

            print(f'\t \n\n {getKey(row[0])} \n\n {parseDesc(row[1])}')
            line_count += 1

            course = Courses(
                courseId=getKey(row[0]),
                courseFullName=parseDesc(row[1])[0],
                units=parseDesc(row[1])[1],
                description=parseDesc(row[1])[2]
            )
            if ((db.session.query(Courses).filter_by(courseId=course.courseId).first()) is None):
                db.session.add(course)
                db.session.commit()
                dataadded += 1
            # try:
            #     db.session.add(course)
            #     db.session.commit()
            #     dataadded += 1
            # except Exception as e:
            #     print()
            #     print()
            #     print(e)

                # if (course.courseId == "WOMENST 3FF3"):
                #     pass
                # else:
                #     print(e)

        print(f'\n Processed {line_count} lines.')
        print(f'\n Dataadded {dataadded} \n')
