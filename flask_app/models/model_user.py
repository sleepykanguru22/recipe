from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash, session
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    # db = "login_reg"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fullname = f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    @classmethod
    def create(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_one(cls,data:dict)-> list:
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False
    
    @classmethod
    def get_one_by_email(cls,data:dict)-> list:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users
    
    @classmethod
    def update_one(cls,data:dict)-> None:
        query = "UPATE users SET first_name = %(first_name)s WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def delete_one(cls,data:dict)-> None:
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validate(data:dict) -> bool:
        is_valid = True
    
        if len(data['first_name'])<1:
            is_valid = False
            flash('required field', 'err_user_first_name')
        
        if len(data['last_name'])<1:
            is_valid = False
            flash('required field', 'err_user_last_name')
        
        if len(data['email'])<1:
            is_valid = False
            flash('required field', 'err_user_email')
        
        elif not EMAIL_REGEX.match(data['email']): 
            flash('Invalid email address!','err_user_email')
            is_valid = False

        else: 
            potential_user = User.get_one_by_email({'email':data['email']})
            if potential_user:
                flash('email address already exsists','err_user_email')
                is_valid = False

        if len(data['password'])<1:
            is_valid = False
            flash('required field', 'err_user_password')
        
        if len(data['confirm_password'])<1:
            is_valid = False
            flash('required field', 'err_user_confirm_password')
        
        elif data['password']!= data['confirm_password']:
            is_valid = False
            flash('passwords do not match ', 'err_user_confirm_password')
        return is_valid

    @staticmethod
    def validate_login(data:dict) -> bool:
        is_valid = True
           
        if len(data['email'])<1:
            is_valid = False
            flash('required field', 'err_user_email_login')
        
        elif not EMAIL_REGEX.match(data['email']): 
            flash('Invalid email address!','err_user_email_login')
            is_valid = False

        else: 
            potential_user = User.get_one_by_email({'email':data['email']})
            if not potential_user:
                flash('email address does not exsists','err_user_email_login')
                is_valid = False
            else:
                if not bcrypt.check_password_hash(potential_user.password, data['password']):
                    flash('invalid email or password', 'err_user_password_login')
                else:
                    session['uuid'] = potential_user.id

        if len(data['password'])<1:
            is_valid = False
            flash('required field', 'err_user_password_login')
        
    
        return is_valid