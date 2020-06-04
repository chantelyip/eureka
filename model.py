"""Models for recipes web application."""

from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    location_of_user = db.Column(db.String)
    created_at = db.Column(db.Integer)

    def __repr__(self):
        return f'''<User user_id={self.user_id} username={self.username} email={self.email}
        password = {self.password} location_of_user = {self.location_of_user} created_at = {self.created_at}>''''

class SavedRecipe(db.Model):

    __tablename__ = 'savedrecipes'

    saved_recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, foreign_key=True)
    user_id = db.Column(db.Integer, foreign_key=True)
    saved_at = db.Column(db.String)

    def __repr__(self):
        return f'''<saved recipe id={self.saved_recipe_id} recipe_id={self.recipe_id}
        user id={self.user_id} saved at={self.saved_at}'''

class Recipe(db.Model):

    __tablename__ = 'recipes'

    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String)
    recipe_course = db.Column(db.String)
    prep_time = db.Column(db.Integer)
    cook_time = db.Column(db.Integer)
    total_recipe_time = db.Column(db.Integer)
    recipe_description = db.Column(db.String)
    servings = db.Column(db.Integer)
    image = db.Column(db.String)
    reviews = db.Column(db.String)

    def __repr__(self):
        return f'''<recipe id={self.recipe_id} recipe_name={self.recipe_name}
        recipe course={self.recipe_course} prep time ={self.prep_time}
        cook time = {self.cook_time} total recipe time = {self.total_recipe_time}
        recipe description = {self.recipe_description} servings = {self.servings}
        image = {self.image} reviews = {self.reviews}'''

class RecipeIngredient(db.Model):

    __tablename__ = 'recipeingredients'


    recipe_ingredients = db.Column(db.String, primary_key=True)
    ingredient_id = db.Column(db.Integer, foreign_key=True)
    recipe_id = db.Column(db.String, foreign_key=True)
    measurements = db.Column(db.Integer)

    def __repr__(self):
        return f'''<recipe ingredients ={self.recipe_ingredients} ingredient id = {self.ingredient_id}
        recipe id = {self.recipe_id} measurements = {self.measurements}>''' 

class Ingredient(db.Model):

    __tablename__ = 'ingredients'     

    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String)
    food_group = db.Column(db.String)
    sweet_or_savory = db.Column(db.String)
        
if __name__ == '__main__':
    from server import app

    connect_to_db(app)  





