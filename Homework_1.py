def cook_book():
    with open('recipes.txt', encoding='utf8') as f:
        cook_book = {}
        while True:
            dish = f.readline().strip('\n')
            cook_book[dish] = []
            list = []
            a = int(f.readline())
            while a != 0:
                ingredient = f.readline().split('|')
                dict_ingredients = {'ingredient_name': ingredient[0].strip(' '), 'quantity': int(ingredient[1].strip(' ')), 'measure': ingredient[2].strip(' \n')}
                list.append(dict_ingredients)
                a -= 1
            cook_book[dish] = list
            if not f.readline():
                break
        return cook_book

#print(cook_book())

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book()[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = {'measure':ingredient['measure'], 'quantity':ingredient['quantity'] * person_count}
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list

print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 1))