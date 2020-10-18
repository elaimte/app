from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from dbcalls import AddTableEducation, AddTableExperience, InsertTableEducation, InsertTableExperience, \
    TableDataEducation, TableDataExperience, IdGenerator, CreateDatabase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'World Ends Here'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///T0.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class User1(db.Model):
    user_id = db.Column(db.String, primary_key=True)
    user_name = db.Column(db.String)
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))
    dbname = db.Column(db.String(200))


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        passkey = request.form['password']
        user_id = User1.query.filter_by(username=username).first()
        if user_id:
            if user_id.password == passkey:
                u_id = user_id.user_id
                session[u_id] = u_id

                print(user_id)

                return redirect('/' + u_id + '/profile')
        else:
            return render_template('Login.html')
    else:
        return render_template('Login.html')


@app.route('/Registration', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('Registeration.html')
    else:
        u_id = IdGenerator()
        username = request.form['username']
        passkey = request.form['password']
        db_name = username + 'Private'
        print(username, passkey, db_name)
        newUser1 = User1(user_id=u_id, username=username, password=passkey, dbname=db_name)
        db.session.add(newUser1)
        db.session.commit()
        CreateDatabase(db_name)
        AddTableEducation(db_name)
        AddTableExperience(db_name)
        session[u_id] = u_id
        print(u_id)
        print('/profile/' + u_id)

        return redirect('/' + u_id + '/profile')


@app.route('/<uid>/profile', methods=['GET', 'POST'])
def do_stuff(uid):
    if uid in session:
        temp_user = User1.query.filter_by(user_id=uid).first()
        user_db = temp_user.dbname
        user_name = temp_user.username
        if request.method == 'POST':
            if request.form["submit"] == 'submit_edu':
                institute_name = request.form["institute_name"]
                degree = request.form["degree"]
                makrs = request.form["makrs"]
                InsertTableEducation(user_db, institute_name, degree, makrs)
                InsertTableEducation(user_db, institute_name, degree, makrs)
                edu_data = TableDataEducation(user_db)
                exp_data = TableDataExperience(user_db)
                if len(exp_data) == 0:
                    exp_data = 'null'
                return render_template('Profile.html', data1=edu_data, data2=exp_data,unmae=user_name)
            if request.form["submit"] == 'submit_exp':
                work_place = request.form["work_place"]
                designation = request.form["designation"]
                from_d = request.form["from_d"]
                to_d = request.form["to_d"]
                InsertTableExperience(user_db, work_place, designation, from_d, to_d)
                exp_data = TableDataExperience(user_db)
                edu_data = TableDataEducation(user_db)
                if len(edu_data) == 0:
                    edu_data = 'null'
                return render_template('Profile.html', data1=edu_data, data2=exp_data, unmae=user_name)
        else:
            edu_data = TableDataEducation(user_db)
            if len(edu_data) == 0:
                edu_data = 'null'
            exp_data = TableDataExperience(user_db)
            if len(exp_data) == 0:
                exp_data = 'null'
            print(exp_data)
            return render_template('Profile.html', data1=edu_data, data2=exp_data,unmae=user_name)
    else:
        redirect('/')


@app.route('/Logout', methods=['POST', 'GET'])
def logout():
    session.clear()
    return redirect("/")


if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)
