from factory_work import validator, file_handler

from models.user import User


def register_user(username,email,password):
    is_name_val =  validator.is_name_valid(username)
    is_email_val = validator.is_email_valid(email)
    is_password_val =  validator.is_password_valid(password)

    if not is_name_val:
        return False, "Username not Valid."
    if not is_email_val:
        return False , "Email not Valid."
    if not is_password_val :
        return False , "Password not Valid."


    duplicate_checker = file_handler.read_json()
    for item in duplicate_checker:
        if item["username"] == username:
            return False, "UserName already Exist"
        if item["email"] == email:
            return False, "Email already Exist"

    user = User(username, email, password)
    user_dict = user.to_dict()

    file_handler.append_json(user_dict)

    return True, "User Created Successfully"


def login_user(username , password):
    load_user_info = file_handler.read_json()
    for item in load_user_info:
        if (item['username'] == username) or (item['email'] == username) :
            if item['password'] == password :
                return True, "User Logged in successfully."
    return False , "Username or Password is wrong."