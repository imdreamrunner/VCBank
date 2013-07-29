import core
from datetime import datetime
import re
import random
import string
import hashlib

def status():
    if 'user_id' in core.session:
        id = core.session.user_id
        return findById(id)
    else:
        return False

def findById(id):
    try:
        return core.db.select('user', where='id = ' + str(id), limit = 1)[0]
    except BaseException:
        return False


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
    if len(firstname) == 0:
        raise Exception(4)
    if len(lastname) == 0:
        raise Exception(5)

    chars = string.ascii_lowercase + string.digits
    salt = ''.join(random.choice(chars) for x in range(16))
    password = hashlib.sha512(password + salt).hexdigest()

    core.db.insert('user',
        email = email,
        password = password,
        firstname = firstname,
        lastname = lastname,
        salt = salt,
        create_time = datetime.now())

def login(email, password):
    user = findByEmail(email)
    if not user:
        raise Exception(2)
    if user.password != hashlib.sha512(password + user.salt).hexdigest():
        raise Exception(3)
    core.session.user_id = user.id

    print core.session.user_id

def loginById(id):
    pass