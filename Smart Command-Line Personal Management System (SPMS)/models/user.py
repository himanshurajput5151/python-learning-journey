class User:
    def __init__(self,user_name, email_name, password_name):
        self.__username(user_name)
        self.__email(email_name)
        self.__password(password_name)

    @property
    def __username(self):
        return self.__username

    @__username.setter
    def __username(self, user_name):
        if username_validater(user_name) :
            self.__username = user_name
        else :
            print("Enter valid username!!!")

    @property
    def __email(self):
        return self.__email

    @__email.setter
    def __email(self, email_name):
        if email_validater(email_name):
            self.__email = email_name
        else:
            print("Enter valid Email!!!")


    @property
    def __password(self):
        return self.__password


    @__password.setter
    def __password(self, password_name):
        if password_validater(password_name):
            self.__username = password_name
        else:
            print("Enter valid password!!!")



    def create_username(self,user_name):

