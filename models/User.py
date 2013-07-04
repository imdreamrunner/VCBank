import core
from datetime import datetime
import re

def findByEmail(email):
    try:
        return core.db.select('user', where='email = "' + email + '"', limit = 1)[0]
    except BaseException:
        return False

def create(user):
    email = user['email'].strip()
    password = user['password']
    firstname = user['firstname'].strip()
    lastname = user['lastname'].strip()

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise Exception(2)
    if findByEmail(email):
        raise Exception(3)
    if len(password) < 6:
        raise Exception(4)
    if len(firstname) == 0 or len(lastname) == 0:
        raise Exception(5)
    core.db.insert('user',
        email = email,
        password = password,
        firstname = firstname,
        lastname = lastname,
        create_time = datetime.now())

def login(email, password):
    user = findByEmail(email)
    if not user:
        raise Exception(2)
    if user.password != password:
        raise Exception(3)
    core.session.user_id = user.id

    print core.session.user_id

def loginById(id):
    pass