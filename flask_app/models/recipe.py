from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from flask_app.models import recipe

class Recipe:
    # db = 'recipes_db'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_one(cls,data:dict)-> list:
        query = "SELECT * FROM users WHERE id = %(id)s;"
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






    # @staticmethod
    # def validate_recipe(recipe):
    #     is_valid = True

    #     if len(recipe['name']) < 3:
    #         flash("Name must be more than 3 characters.")
    #         is_valid = False

    #     if len(recipe['description']) < 3:
    #         flash("Description must be more than 3 characters.")
    #         is_valid = False

    #     if len(recipe['instructions']) < 3:
    #         flash(f"Instructions must be more than 3 characters.")
    #         is_valid = False

    #     if len(recipe['date_made']) < 1:
    #         flash("Date Made field required.")
    #         is_valid = False

    #     return is_valid

    # @classmethod
    # def save(cls,data):
    #     query = "INSERT INTO recipes (name, description, instructions, under_30, date_made, user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(under_30)s,%(date_made)s,%(user_id)s);"
    #     results = connectToMySQL(cls.db).query_db(query, data)

    #     return results

    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, under_30 = %(under_30)s, date_made = %(date_made)s WHERE id = %(id)s "
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     return results

    # @classmethod
    # def get_all_recipes_id(cls,data):
    #     query = "SELECT * FROM recipes WHERE user_id = %(user_id)s"
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     user_recipes = []
    #     for x in range(0, len(results)):
    #         user_recipes.append(results[x])

    #     return user_recipes

    # @classmethod
    # def get_recipe_info(cls,data):
    #     query = "SELECT * FROM recipes WHERE id = %(id)s"
    #     results = connectToMySQL(cls.db).query_db(query, data)

    #     return cls(results[0])
