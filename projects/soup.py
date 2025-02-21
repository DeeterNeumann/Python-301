# take an unlimited number of Ingredient() or Spice() objects during instantiation
#  have a .cook() method that returns a search result for a soup recipe using all the added ingredients

from spice import Ingredient
import webbrowser

h = Ingredient("ham", 5)
b = Ingredient("bean", 20)
c = Ingredient("carrot", 3)
cel = Ingredient("celery", 3)
p = Ingredient("pea", 2)

# *args and **kwargs

class Soup():

    def __init__(self, *ingredients: list[Ingredient], servings = 0):
        self.ingredients: list[Ingredient] = ingredients
        self.servings = servings
    
    def cook(self):
        soups_up = ""
        for i in self.ingredients:
            soups_up = soups_up.strip() + " " + i.name
        print(f"Mmmm {soups_up} soup")
        url = f'https://www.google.com/search?q={soups_up}+soup'
        return webbrowser.open_new_tab(url)
        
# soup = Soup([h, b, c, cel, p])

# soup.cook()