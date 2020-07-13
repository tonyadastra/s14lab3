from flask import Flask, render_template, request, redirect, url_for
from models.user import Db, User
from modules.userform import UserForm, UserIDForm, UpdateUserForm
import random
# Quote following line to run at local
from flask_heroku import Heroku
app = Flask(__name__)
# Quote following line to run at local
heroku = Heroku(app)
# Unquote following line to run at local
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/usersdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "s14a-key"
Db.init_app(app)


@app.route('/')
def index():
    # Add Query
    users = User.query.all()
    # Iterate and print
    for user in users:
        User.toString(user)

    return render_template("index.html", users=users)


@app.route('/readuser', methods=['GET', 'POST'])
def readUser():
    form = UserIDForm()
    # If GET
    if request.method == 'GET':
        return render_template('userid.html', form=form)
    # If POST
    else:
        if form.validate_on_submit():
            user_id = request.form['user_id']
            if Db.session.query(User).filter_by(user_id=user_id).scalar() is not None:
                readuser = Db.session.query(User).filter_by(user_id=user_id)
                # Iterate and print
                for user in readuser:
                    User.toString(user)
                return render_template('readuser.html', user_id=user_id, readuser=readuser)
            else:
                return redirect(url_for('error'))
        else:
            return render_template('userid.html', form=form)


# @route /adduser - GET, POST
@app.route('/adduser', methods=['GET', 'POST'])
def addUser():
    form = UserForm()
    # If GET
    if request.method == 'GET':
        return render_template('adduser.html', form=form)
    # If POST
    else:
        if form.validate_on_submit():
            first_name = request.form['first_name']
            age = request.form['age']
            new_user = User(first_name=first_name, age=age)
            Db.session.add(new_user)
            Db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('adduser.html', form=form)


@app.route('/updateuser', methods=['GET', 'POST'])
def updateUser():
    form = UpdateUserForm()
    # If GET
    if request.method == 'GET':
        return render_template('updateuser.html', form=form)
    # If POST
    else:
        if form.validate_on_submit():
            user_id = request.form['user_id']
            first_name = request.form['first_name']
            age = request.form['age']
            if Db.session.query(User).filter_by(user_id=user_id).scalar() is not None:
                Db.session.query(User).filter_by(user_id=user_id).update({'first_name': first_name, 'age': age})
                Db.session.commit()
                return redirect(url_for('index'))
            else:
                return redirect(url_for('error'))
        else:
            return render_template('updateuser.html', form=form)


@app.route('/deleteuser', methods=['GET', 'POST'])
def deleteUser():
    form = UserIDForm()
    # If GET
    if request.method == 'GET':
        return render_template('deleteuser.html', form=form)
    # If POST
    else:
        if form.validate_on_submit():
            user_id = request.form['user_id']
            if Db.session.query(User).filter_by(user_id=user_id).scalar() is not None:
                Db.session.query(User).filter_by(user_id=user_id).delete()
                Db.session.commit()
                return redirect(url_for('index'))
            else:
                return redirect(url_for('error'))

        else:
            return render_template('deleteuser.html', form=form)


# @route /adduser/<first_name>/<age>
@app.route('/adduser/<first_name>/<age>')
def addUserFromUrl(first_name, age):
    Db.session.add(User(first_name=first_name, age=age))
    Db.session.commit()
    return redirect(url_for('index'))


@app.route('/deleteuser/<first_name>/')
def deleteUserFromUrl(first_name):
    Db.session.query(User).filter_by(first_name=first_name).delete()
    Db.session.commit()
    return redirect(url_for('index'))

@app.route('/deleteuser/id/<user_id>/')
def deleteUseridFromUrl(user_id):
    Db.session.query(User).filter_by(user_id=user_id).delete()
    Db.session.commit()
    return redirect(url_for('index'))

# @app.route('/updateuser/<first_name>/<age>')
# def updatdeUserFromUrl(first_name, age):
#     Db.session.query(User).filter_by(first_name=first_name).update({"age": age})
#     Db.session.commit()
#     return redirect(url_for('index'))

@app.route('/random')
def mockDataGenerator():
    for i in range(1, random.randint(74, 704)):
        first_name = "NPC" + str(random.randint(2202, 18906416))
        age = 1000
        new_user = User(first_name=first_name, age=age)
        Db.session.add(new_user)
        Db.session.commit()
    return redirect(url_for('randomPage'))
    # return render_template('random.html')
    # form = UserForm()
    # # If GET
    # if request.method == 'GET':
    #     return render_template('adduser.html', form=form)
    # # If POST
    # else:
    #     if form.validate_on_submit():
    #         first_name = request.form['first_name']
    #         age = request.form['age']
    #         new_user = User(first_name=first_name, age=age)
    #         Db.session.add(new_user)
    #         Db.session.commit()
    #         return redirect(url_for('index'))
    #     else:
    #         return render_template('adduser.html', form=form)

@app.route('/deleteallnpcs')
def deleteAllNPCs():
    Db.session.query(User).filter_by(age=1000).delete()
    Db.session.commit()
    return redirect(url_for('index'))


@app.route('/deleteallusers')
def deleteAllUsers():
    Db.session.query(User).delete()
    Db.session.commit()
    return redirect(url_for('index'))

@app.route('/error')
def error():
    return render_template('usernotfound.html')