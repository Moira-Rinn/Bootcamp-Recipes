from Flask_App.config.mysql_connection import connectToMySQL


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.date = data['date']
        self.thirty = data['thirty']
        self.description = data['description']
        self.instructions = data['instructions']
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
        query = "INSERT INTO recipes (name, date, thirty, description, instructions, created_at, updated_at, user_id) VALUES (%(name)s, %(date)s, %(thirty)s, %(description)s, %(instructions)s, NOW(), NOW(), %(user_id)s);"
        recipe_id = connectToMySQL('recipes_db').query_db(query, data)
        return recipe_id

    @classmethod
    def edit_recipe(cls, data=None):
        query = "UPDATE recipes SET name=%(name)s, date=%(date)s, thirty= %{thirty}s, description=%(description)s, instructions=%(instructions)s, updated_at = NOW() WHERE id = ;"
        recipe_id = connectToMySQL('recipes_db').query_db(query, data)
        return recipe_id

    @classmethod
    def remove_recipe(cls, query, data=None):
        recipe_id = connectToMySQL('recipes_db').query_db(query, data)
        return recipe_id
