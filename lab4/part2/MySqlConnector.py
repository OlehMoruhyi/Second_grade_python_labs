from mysql.connector import *
try:
    connection = connect(
        host="127.0.0.1",
        user="root",
        password="38AS00YfSMtgmZemePTw",
    )

    select1 = "SELECT MAX(id) FROM Teacher"
    cursor = connection.cursor()
    cursor.execute("use Courses")
    cursor.execute(select1)
    teacherID = cursor.fetchall()[0][0]
    if not teacherID:
        teacherID = 0

    select1 = "SELECT MAX(id) FROM LocalCourses"
    select2 = "SELECT MAX(id) FROM OffsiteCourses"

    cursor.execute(select1)
    coursesID = cursor.fetchall()[0][0]
    if not coursesID:
        coursesID = 0
    cursor.execute(select2)
    coursesID1 = cursor.fetchall()[0][0]
    if not coursesID1:
        coursesID1 = 0
    coursesID = max(coursesID, coursesID1)




    del select1, select2, coursesID1
except Error as e:
    print(e)
