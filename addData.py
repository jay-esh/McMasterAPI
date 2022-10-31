from app import app, db
import csv


# with app.app_context():
#     db.create_all()
    # with open('courseData.csv', mode='r') as f: 
    #     csv_reader  = csv.reader(f)
    #     line_count = 0

    #     for row in csv_reader:
    #         print(', '.join(row))


def getKey(str):
    l = str.split()
    key = l[0] + ' ' + l[1]
    return key


with open('courseData.csv') as f:
    csv_reader = csv.reader(f)
    line_count = 0
    for row in csv_reader:
        print(f'\t \n\n {getKey(row[0])} \n\n {row[1]}')
        line_count += 1
    print(f'\n Processed {line_count} lines.')

