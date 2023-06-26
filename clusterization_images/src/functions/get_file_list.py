
# считать список файлов из всех поддерикторий
# возвращает список имен файлов и уникальные расширения файлов

# path - путь к директории type - str
# name_list - список названий файлов по которому фильтруем type - list
def get_file_list(path, name_list = []):
    rezult = []
    variant = set()
    for root, dirs, files in os.walk(path, topdown = False):        
        for name in files:
            if len(name_list) > 0:
               if not(filter_fille_name(name, name_list)):
                  continue
            
            rezult.append(os.path.join(root, name))
            # если нет расширений у файлов добавляем None, иначе - название расширения
            file_extension = name.split('.')[1] if len(name.split('.')) > 1 else None
            variant.add(file_extension) 
    return rezult, variant
