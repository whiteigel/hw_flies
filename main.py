def make_cook_book():
        with open("./recipes.txt", "r") as file:
            cook_book = {}
            for line in file:
                course = line.strip()
                ingr_count = int(file.readline().strip())
                course_set = []
                for i in range(ingr_count):
                    ingredient_name, quantity, measure = file.readline().strip().split(" | ")
                    ingr_set = {'ingredient_name': ingredient_name, 'quantity': quantity,'measure': measure}
                    course_set.append(ingr_set)
                cook_book[course] = course_set
                file.readline()
        return cook_book

def create_shop_list(cook_book, courses, person_count):
    shop_list = {}
    for dish in courses:
         for ingr in cook_book[dish]:
            ingr['quantity'] = (int(ingr['quantity']) * int(person_count))
            shop_list_item = {'measure':ingr['measure'],'quantity':ingr['quantity']}
            if ingr['ingredient_name'] not in shop_list:
                shop_list[ingr['ingredient_name']] = shop_list_item
            else:
                shop_list[ingr['ingredient_name']]['quantity'] += shop_list_item['quantity']
    return shop_list

def make_shop_list():
    cook_book = make_cook_book()
    person_count = int(input('Введите число гостей: '))
    courses = input('Введите список блюд через запятую: ').split(", ")
    courses_cap = [name.capitalize() for name in courses]
    shop_list = create_shop_list(cook_book, courses_cap, person_count)
    return f'Вам необходимо купить следующие продукты: {shop_list}'

print(make_shop_list())