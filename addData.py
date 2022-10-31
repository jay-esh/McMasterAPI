from app import app, db
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
            for row in csv_reader:

                print(f'\t \n\n {getKey(row[0])} \n\n {parseDesc(row[1])}')
                line_count += 1
            print(f'\n Processed {line_count} lines.')



