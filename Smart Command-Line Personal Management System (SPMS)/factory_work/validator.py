import re as regex

def is_name_valid(username):
    pattern = r"^[a-zA-Z][a-zA-Z0-9_]{2,16}$"
    return bool(regex.match(pattern,username))

def is_email_valid(email):
    pattern = r"^[a-z][a-z0-9]{3,20}@[a-z]{2,6}\.(com|org|in)$"
    return bool(regex.match(pattern,email))


def is_password_valid(password):
    pattern = r"^[a-zA-Z0-9~!@#$%^&*()_=+?/<>{}:;\\|-]{8,16}$"
    return bool(regex.match(pattern,password))