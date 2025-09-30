# # TASK 1
#
# cook_book = {}
# with open('recipes.txt', 'rt', encoding='utf-8') as file:
#     dishes = ''
#     for x in file:
#         x = x.strip()
#         if x.isdigit():
#             continue
#         elif x and '|' not in x:
#             cook_book[x] = []
#             dishes = x
#         elif x and '|' in x:
#             a, b, c = x.split(" | ")
#             cook_book.get(dishes).append(dict(ingredient_name=a, quantity=int(b), measure=c))
# # print(cook_book)
#
# # Задача №2:
# def get_shop_list_by_dishes(dishes_list, person_count):
#     shop_list = {}
#     for dish in dishes_list:
#         if dish in cook_book:
#             for ingredient in cook_book[dish]:
#                 if ingredient['ingredient_name'] in shop_list:
#                     shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
#                 else:
#                     shop_list[ingredient['ingredient_name']] = ({'measure': ingredient['measure'], 'quantity':
#                                                                 (ingredient['quantity'] * person_count)})
#         else:
#             print('Такого блюда нет в книге')
#     return shop_list
# # print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


# Задача №3:
import os


cwd = os.getcwd()
dir_with_files = 'C:/NETO/cook_book/files_for_task_3'

# Список имён файлов .txt из указанной дирректории
txt_files = [f for f in os.listdir(dir_with_files) if os.path.isfile(os.path.join(dir_with_files, f)) and f.endswith('.txt')]

# Словарь с именем и кол-вом строк файла
files_info_dict = {}
for txt_file in txt_files:
    with open(os.path.join(cwd, dir_with_files, txt_file), encoding='utf-8') as f:
        lines = f.readlines()
        files_info_dict[txt_file] = (len(lines), lines)

# Сортируем в порядке возрастания кол-ва строк
files_info_tuple = sorted(files_info_dict.items(), key=lambda item: item[1])

# Запись результата в файл
with open('C:/NETO/cook_book/result.txt', 'w', encoding='utf-8') as result:
    for file_info in files_info_tuple:
        result.write(f'{file_info[0]}\n')
        result.write(f'{file_info[1][0]}\n')
        result.writelines(file_info[1][1] + ['\n'])