with open("./input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

allIngredients = []
allergens = {}
for line in lines:
    
    line = line.split(" (contains ")
    ingredients = set(line[0].split())
    possibleAllergens = line[1].replace(")", "").strip().split(", ")
    allIngredients += ingredients

    for al in possibleAllergens:
        if al not in allergens:
            allergens[al] = ingredients
        
        else:
            allergens[al] = allergens[al] & ingredients

# Part one
dangerousIngredients = set()
for i in allergens.values():
    dangerousIngredients |= i

counter = 0
for i in allIngredients:
    if i not in dangerousIngredients:
        counter += 1
print(counter)

# Part two
finished = False
toRemove = set()
while not finished:
    finished = True
    for al in allergens:

        if len(allergens[al]) > 1:
            finished = False
            temp = allergens[al].copy()

            for allergen in temp:
                if allergen in toRemove:
                    allergens[al].remove(allergen)
        
        elif len(allergens[al]) == 1:
            toRemove |= allergens[al]

allAllergens = sorted(allergens.keys())
result = ""
for al in allAllergens:
    result += list(allergens[al])[0] + ","
result = result[:len(result)-1]

print(result)