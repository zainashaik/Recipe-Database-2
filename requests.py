#! usr/bin/env python3

"""
All functions across associated url, convert data from JSON format into
something usable, and returns that data as a corresponding object
"""

from urllib import request, parse
import json

from objects import Category, Meal, Area


def get_categories():
    url = "https://www.themealdb.com/api/json/v1/1/list.php?c=list"
    f = request.urlopen(url)
    categories = []

    try:
        data = json.loads(f.read().decode("utf-8"))
        for category_data in data["meals"]:
            category = Category(category_data["strCategory"])

            categories.append(category)
    except(ValueError, KeyError, TypeError):
        print("JSON format error")

    return categories


def get_meals_by_category(category):
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + category
    m = request.urlopen(url)
    meals = []

    try:
        data = json.loads(m.read().decode("utf-8"))
        for meal_data in data["meals"]:
            meal = Meal(meal_data["strMeal"])

            meals.append(meal)
    except(ValueError, KeyError, TypeError):
        print("That category was not found.")

    return meals


def get_areas():
    url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
    a = request.urlopen(url)
    areas = []

    try:
        data = json.loads(a.read().decode("utf-8"))
        for area_data in data["meals"]:
            area = Area(area_data["strArea"])

            areas.append(area)
    except(ValueError, KeyError, TypeError):
        print("JSON format error")

    return areas


def get_meals_by_area(area):
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?a=" + area
    m = request.urlopen(url)
    meals = []

    try:
        data = json.loads(m.read().decode("utf-8"))
        for meal_data in data["meals"]:
            meal = Meal(meal_data["strMeal"])

            meals.append(meal)
    except(ValueError, KeyError, TypeError):
        print("That area was not found.")

    return meals


def get_instructions(meal):
    url = "https://www.themealdb.com/api/json/v1/1/search.php?s=" + parse.quote(meal)
    m = request.urlopen(url)

    instructions = ""

    try:
        data = json.loads(m.read().decode("utf-8"))
        for meal_data in data["meals"]:
            instructions = meal_data["strInstructions"]
    except(ValueError, KeyError, TypeError):
        print("That meal was not found.")

    return instructions


def get_ingredients(meal):
    url = "https://www.themealdb.com/api/json/v1/1/search.php?s=" + parse.quote(meal)
    m = request.urlopen(url)

    ingredients = []
    num = 1
    # ing = "strIngredients" + str(num)

    try:
        data = json.loads(m.read().decode("utf-8"))
        # while ing.startswith("strIngredients")
        for meal_data in data["meals"]:
            while num <= 20:
                ing = "strIngredient" + str(num)
                meas = "strMeasure" + str(num)
                ingredient = meal_data[ing]
                measurement = meal_data[meas]
                if ingredient == "":
                    break
                ingredients.append(measurement + " " + ingredient)
                num += 1
    except(ValueError, KeyError, TypeError):
        print("That meal was not found.")

    return ingredients


def get_meal_by_name(meal):
    url = "https://www.themealdb.com/api/json/v1/1/lookup.php?i=" + parse.quote(meal)
    m = request.urlopen(url)

    meal1 = Meal

    try:
        data = json.loads(m.read().decode("utf-8"))
        for meal_data in data["meals"]:
            meal1 = Meal(meal_data["strMeal"])
    except(ValueError, KeyError, TypeError):
        print("That meal was not found.")

    return meal1


def get_random_meal():
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    m = request.urlopen(url)

    meal = Meal

    try:
        data = json.loads(m.read().decode("utf-8"))
        for meal_data in data["meals"]:
            meal = Meal(meal_data["strMeal"])
    except(ValueError, KeyError, TypeError):
        print("That meal was not found.")

    return meal


# main function for testing the API calls
def main():
    categories = get_categories()

    # Print all the categories
    print("Categories")
    for i in range(len(categories)):
        category = categories[i]
        print(category.get_category())


if __name__ == '__main__':
    main()
