from Flask_App.config.mysql_connection import connectToMySQL


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.thirty = data['thirty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all(cls, query, data=None):
        recipes_from_db = connectToMySQL('recipes_db').query_db(query, data)
        recipes = []
        for r in recipes_from_db:
            recipes.append(cls(r))
        return recipes

    @classmethod
    def save(cls, data=None):
        query = "INSERT INTO recipes (name, thirty, created_at, updated_at, user_id) VALUES(%(name)s, %(thirty)s, NOW(), NOW(), %(user_id)s);"
        recipe_id = connectToMySQL('recipes_db').query_db(query, data)
        return recipe_id

    # @classmethod
    # def remove_recipe(cls, query, data=None):
    #     recipe_id = connectToMySQL('recipes_schema').query_db(query, data)
    #     return recipe_id

    # @classmethod
    # def edit_recipe(cls, query, data=None):
    #     recipe_id = connectToMySQL('recipes_schema').query_db(query, data)
    #     return recipe_id
