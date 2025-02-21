import webbrowser
from spice import Ingredient
from soup import Soup

b = Ingredient("bean", 10)
h = Ingredient("ham", 2)
c = Ingredient("carrot", 3)
cel = Ingredient("celery", 3)
p = Ingredient("pea", 5)


soup = Soup(b, h, c, cel, p)

soup.cook()