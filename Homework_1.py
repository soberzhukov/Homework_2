def create_cook_book(document):
    with open(document, encoding='utf8') as f:
        cook_book = {}
        while True:
            dish = f.readline().strip('\n')
            cook_book[dish] = []
            list = []
            a = int(f.readline())
            while a != 0:
                ingredient = f.readline().split('|')
                dict_ingredients = {'ingredient_name': ingredient[0].strip(' '), 'quantity': ingredient[1].strip(' '), 'measure': ingredient[2].strip(' \n')}
                list.append(dict_ingredients)
                a -= 1
            cook_book[dish] = list
            if not f.readline():
                break
        return cook_book

print(create_cook_book('recipes.txt'))


