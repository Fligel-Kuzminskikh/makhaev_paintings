
# конвертация в формат cv2
# возвращает словарь вида {'img':вектор изображения в формате PIL,'title':название}

# filename - полный путь к файлу

def file2PIL(filename):  
     return {'img': Image.open(filename), 'title':filename}
