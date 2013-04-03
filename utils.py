# Utils.py 
import os
import webapp2
import re
import jinja2
import cgi
import random
import string
import hashlib

from google.appengine.ext import db # For using databases
from google.appengine.ext import blobstore


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env= jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

# Writing a function to escape html inputed in forms
def escape_html(s):
    return cgi.escape(s, quote = True)

# Hashing and making cookies secure

def hash_str(s):
        return hashlib.md5(s).hexdigest()

def make_secure_val(s):
        return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
        val = h.split('|')[0]
        if h == make_secure_val(val):
                return val
def valid_user(name, pw):
    user = get_user(name)
    if user and user.password_hash == H(pw):
        return user

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)


    


def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt=make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
    # Note check [1] or[0]
    salt = h.split(',')[1]
    return h == make_pw_hash(name, pw, salt)

def users_key(group='default'):
    return db.Key.from_path('users',group)

CRSID_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_crsid(CRSID):
    return CRSID and CRSID_RE.match(CRSID)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)