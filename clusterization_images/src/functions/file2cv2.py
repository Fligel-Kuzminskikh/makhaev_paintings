
# конвертация в формат cv2
# возвращает словарь вида {'img':вектор изображения в формате CV2,'title':название}

# filename - полный путь к файлу
def file2cv2(filename):     
     return {'img':cv2.imread(filename), 'title':filename}
