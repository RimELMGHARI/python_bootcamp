cookbook= {
    "sandwich":{'ingredients': ['ham', 'bread', 'cheese' ,'tomatoes'],
                'meal': 'lunch',
                'prep_time': '10 min'
                },
    "cake":{'ingredients':['flour', 'sugar' , 'eggs'],
            'meal': 'desert',
            'prep_time':'60 min'
            },
    "salad":{'ingredients': ['avocado', 'arugula', ' tomatoes' ,'spinach'],
            'meal':'lunch',
            'prep_time':'15 min'
            }
    }



def find_recipe(recipeName):
    if recipeName in cookbook:
        print("Recipe for" ,recipeName,":")
        print("Ingredients list:", cookbook[recipeName]['ingredients'],".")
        print("To be eaten for", cookbook[recipeName]['meal'])
        print("Takes", cookbook[recipeName]['prep_time'] ,"minutes of cooking.")
    else:
        print('recipe unavailable')
      
    
def delete_recipe(recipeName):
    if recipeName in cookbook:
        del cookbook[recipeName]
    else:
        print('recipe unavailable')
        
def add_recipe(recipeName, ingredients, meal, prep_time):
    cookbook[recipeName] = {'ingredients':ingredients,
                            'meal':meal,
                            'prep_time':prep_time
                            }
    print(cookbook)
    

def recipenames(cookbook):
    for id in cookbook:
        print("\nrecipe:", id )


print("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook \n5: Quit")
option=int(input("->"))

if option==1:
    print("To add a recipe, please add recipe info:")
    recipeName=input("recipe name:")
    ingredients=input("ingredients:")
    meal=input("meal:")
    prep_time=input("prep time:")
    add_recipe(recipeName, ingredients, meal, prep_time)
    print(cookbook)

elif option==2:
    recipeName=input("To delete a recipe, please enter recipe name:")
    delete_recipe(recipeName)
    print("recipe deleted")
    
elif option==3:
    recipeName=input("Please enter the recipe's name to get its details:")
    find_recipe(recipeName)

elif option==4:
    recipenames(cookbook)

elif option==5:
    print("Cookbook closed.")
    
else:
    print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
