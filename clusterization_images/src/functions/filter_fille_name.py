
# на вход передается путь к имени файла и список id объектов. id соответствует первой части имени файла
# по маске id_*.jpg
# возвращает булево значение есть id в списке или нет

# fille_path - полный путь к файлу
# id_list - список id
def filter_fille_name(fille_path, id_list):   
    fille_name = fille_path.split('/')[-1]
    return fille_name.split('.')[0].split('_')[0] in id_list
