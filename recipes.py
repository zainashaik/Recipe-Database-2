#! usr/bin/env python3
import requests
import textwrap


def menu():
    print("The Recipes Program")
    print()
    print("COMMAND MENU")
    print("1 - List all Categories")
    print("2 - List all Meals for a Category")
    print("3 - Search Meal by Name")
    print("4 - Random Meal")
    print("5 - List all Areas")
    print("6 - Search Meals by Area")
    print("0 - Exit the program")
    print()


def get_categories(categories):
    # Print all the categories
    print("CATEGORIES")
    for i in range(len(categories)):
        category = categories[i]
        print("  " + category.get_category())


def get_meals_by_category(category):
    meals = requests.get_meals_by_category(category)

    # print all meals per category
    if len(meals) >= 1:
        print(category.upper() + " MEALS")
    for i in range(len(meals)):
        meal = meals[i]
        print("  " + meal.get_meal())


def get_meal_by_name(meal):
    # print meal by name
    print("Recipe: " + meal)
    print()

    # print instructions
    my_wrap = textwrap.TextWrapper(width=80)
    wrap_list = my_wrap.wrap("Instructions: " + requests.get_instructions(meal))
    for line in wrap_list:
        print(line)

    # print ingredients
    print()
    print("Ingredients:")
    print("-----------------------------------------------------------------------------------")
    ingredients = requests.get_ingredients(meal)
    i = 0
    while i < len(ingredients):
        if i+2 < len(ingredients):
            print("{: <30} {: <30} {: <30}".format(str(ingredients[i]), str(ingredients[i + 1]),
                                                   str(ingredients[i + 2])))

        elif i+1 < len(ingredients):
            print("{: <30} {: <30}".format(str(ingredients[i]), str(ingredients[i + 1])))

        else:
            print("{: <30}".format(str(ingredients[i])))
        i += 3

    print()


def get_random_meal():
    print("A random meal was selected just for you!")
    print()

    meal = requests.get_random_meal()
    get_meal_by_name(meal.get_meal())


def get_areas(areas):
    # Print all the areas
    print("AREAS:")
    for i in range(len(areas)):
        area = areas[i]
        print("  " + area.get_category())


def get_meals_by_area(area):
    meals = requests.get_meals_by_area(area)

    # print all meals per categories
    if len(meals) >= 1:
        print(area.upper() + " MEALS")
    for i in range(len(meals)):
        meal = meals[i]
        print("  " + meal.get_meal())


def end():
    print("Thank you for dining with us!")


def main():
    menu()
    categories = requests.get_categories()
    areas = requests.get_areas()

    while True:
        print()
        command = input("Command: ")

        if command == "1":
            print()
            get_categories(categories)
        elif command == "2":
            category = input("Enter a category: ")
            print()
            get_meals_by_category(category)
        elif command == "3":
            name = input("Enter Meal Name: ")
            print()
            get_meal_by_name(name)
        elif command == "4":
            get_random_meal()
        elif command == "5":
            get_areas(areas)
        elif command == "6":
            area = input("Enter an area: ")
            print()
            get_meals_by_area(area)
        elif command == "0":
            break
        else:
            print("Please enter a number from 0 to 6.")

    end()


if __name__ == "__main__":
    main()
