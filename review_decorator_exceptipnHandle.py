
import hashlib
import re
class Account :
    def __init__(self, username , password , user_id , phone , email):

        self.username = username
        self.password = password
        self.user_id = user_id
        self.phone = phone 
        self.email = email 

        pass

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self , username):
        username_regex = '^[a-zA-Z]+_[a-zA-Z]+$'
        try :
            if re.search(username_regex , username):
                        self.__username = username
            else : 
                raise  NameError()
        except NameError:
            print('invalid username')
        pass 

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self , password): 
        password_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"
        try :
            if re.search(password_regex , password):
                # hashe_password = hashlib.sha256(password.encode('utf-8').hexdigest())
                self.__password = password
            else : 
                raise  NameError()
        except NameError:
            print('invalid password')
        pass
    
    def show_welcome(func):

        def inner_func(self):
            t = func(self)
            y = t.replace('_', ' ')
            print(f'welcome to our site {y}')

        return inner_func



    @show_welcome
    def welvome(self):
        return self.username
        

    # @property   
    # def user_id(self):
    #     return self.__user_id
        
    # @user_id.setter
    # def user_id(self, user_id):
    #     self.__user_id = user_id

    
    # @property
    # def phone(self):
    #     return self.__phone 

    # @phone.setter
    # def phone(self, phone):
    #     self.__phone = phone


    # @property
    # def email(self): 
    #     return self.__email


    # @email.setter
    # def email(self ,email):
    #     self.__email = email




acc = Account("hossein_samiei" , '9387A4234' , "12Aa3243" , 30495  , "sh@lsdfjn.com")

acc.welvome()

