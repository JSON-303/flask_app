from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint


class User:
    """THIS CONSTRUCTOR FUNCTION ACCEPTS A DICTIONARY AS INPUT"""

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    """
    CREATE A CLASS METHOD FOR EACH CRUD QUERY
    """

    @classmethod
    def find_all(cls):
        query = "SELECT * FROM users;"
        list_of_dicts = connectToMySQL("users_schema").query_db(query)
        pprint(list_of_dicts)
        users = []
        for each_user in list_of_dicts:
            user = User(each_user)
            users.append(user)
        return users

    @classmethod
    def create(cls, form_data):
        """
        INSERTS A NEW USER INTO THE DATABASE
        """
        query = """
        INSERT INTO users
        (first_name, last_name, email)
        VALUES
        (%(first_name)s, %(last_name)s, %(email)s);
        """
        user_id = connectToMySQL("users_schema").query_db(query, form_data)
        return user_id

    @classmethod
    def find_by_id(cls, user_id):
        """FINDS ONE USER BY ID IN THE DATABASE"""
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        data = {"user_id": user_id}
        list_of_dicts = connectToMySQL("users_schema").query_db(query, data)
        if len(list_of_dicts) == 0:
            return None
        user = User(list_of_dicts[0])
        return user

    @classmethod
    def update(cls, form_data):
        """Updates a user from a form"""
        query = """
        UPDATE users
        SET
        first_name = %(first_name)s, 
        last_name = %(last_name)s,
        email = %(email)s
        WHERE id = %(user_id)s;
        """
        connectToMySQL("users_schema").query_db(query, form_data)
        return

    @classmethod
    def delete_by_id(cls, user_id):
        """Deletes a user by their id"""
        query = "DELETE FROM users WHERE id = %(user_id)s;"
        data = {"user_id": user_id}
        connectToMySQL("users_schema").query_db(query, data)
        return
