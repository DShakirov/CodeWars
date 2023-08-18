def codewars_pete_the_baker(recipe, ingridients):
    ans = []
    for goods in recipe.keys():
        if goods not in ingridients.keys():
            return 0
        ans.append(ingridients[goods]//recipe[goods])
    return min(ans)

#print(codewars_pete_the_baker({'apples': 3, 'flour': 300, 'sugar': 150,'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000}))
print(codewars_pete_the_baker({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))