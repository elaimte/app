import mysql.connector
import random
import string
from mysqlx import Error

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hknudxnt@143",
    auth_plugin='mysql_native_password'
)


def IdGenerator():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(50))
    return result_str


def RegisterUser(username,password):
    mycursor = mydb.cursor()



def CreateDatabase(dbname):
    mycursor = mydb.cursor()
    sql = 'CREATE DATABASE {db_name}'
    mycursor.execute(sql.format(db_name=dbname))
    mycursor.close()


def AddTableEducation(dbname):
    db_con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hknudxnt@143",
        auth_plugin='mysql_native_password',
        database=dbname
    )
    db_cursor = db_con.cursor()
    db_cursor.execute(
        "CREATE TABLE education (id INT AUTO_INCREMENT PRIMARY KEY, institute VARCHAR(255), degree VARCHAR(255), cgpa VARCHAR (5))")
    db_cursor.close()


def AddTableExperience(dbname):
    db_con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hknudxnt@143",
        auth_plugin='mysql_native_password',
        database=dbname)
    db_cursor = db_con.cursor()
    db_cursor.execute(
        "CREATE TABLE experience (id INT AUTO_INCREMENT PRIMARY KEY, workplace VARCHAR(255), designation VARCHAR(255), fromd VARCHAR (10), tod VARCHAR (10))")
    db_cursor.close()


def InsertTableEducation(dbname, inst, deg, cgp):
    db_con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hknudxnt@143",
        auth_plugin='mysql_native_password',
        database=dbname
    )
    db_cursor = db_con.cursor()

    sql_insert = "INSERT INTO education ( institute, degree, cgpa) VALUES( \"{}\", \"{}\",\"{}\")".format(inst, deg,
                                                                                                          cgp)
    db_cursor.execute(sql_insert)
    db_con.commit()
    db_cursor.close()


def InsertTableExperience(dbname, wrk, desg, frm, tdd):
    db_con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hknudxnt@143",
        auth_plugin='mysql_native_password',
        database=dbname
    )
    db_cursor = db_con.cursor()

    sql_insert = "INSERT INTO experience ( workplace, designation, fromd, tod) VALUES( \"{}\", \"{}\",\"{}\",\"{}\")".format(
        wrk, desg, frm,
        tdd)
    db_cursor.execute(sql_insert)
    db_con.commit()
    db_cursor.close()


def TableDataEducation(dbname):
    db_con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hknudxnt@143",
        auth_plugin='mysql_native_password',
        database=dbname
    )
    db_cursor = db_con.cursor()
    try:
        db_cursor.execute("select * from education")
        records = db_cursor.fetchall()
        db_cursor.close()
        return records
    except Error as e:
        print(e)
        records = 'null'
    return records


def TableDataExperience(dbname):
    db_con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hknudxnt@143",
        auth_plugin='mysql_native_password',
        database=dbname
    )
    db_cursor = db_con.cursor()
    try:
        db_cursor.execute("select * from experience")
        records = db_cursor.fetchall()
        db_cursor.close()
        return records
    except Error as e:
        print(e)
        records = 'null'
    return records
