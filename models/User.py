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

def findUserSafe(id):
    user = findById(id)
    if user:
        return safeData(user)
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

def getList(order = 'id', where = None):
    return list(getIter(order, where))

def getIter(order = 'id', where = None):
    if where:
        return core.db.select('user', where = where, order = order)
    else:
        return core.db.select('user', order = order)

def getSafe(order = 'id', where = None):
    """
    Remove the password and salt data.
    Convert the datetime format to string (for json decode).
    """
    users = getIter(order, where)
    returnObj = []
    for user in users:
        returnObj.append(safeData(user))
    return returnObj

def safeData(user):
    newUser = {}
    for prop, value in user.iteritems():
        if prop == 'password' or prop == 'salt':
            continue
        if isinstance(value, datetime):
            value = value.strftime("%Y-%m-%d %H:%M:%S")
        newUser[prop] = value
    return newUser

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