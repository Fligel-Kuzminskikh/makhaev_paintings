
# возвращает id объекта из пути к файлу картинки и преффикс 1 или 2

# fille_path - путь к файлу
def setImgId(fille_path):  
  fille_name = fille_path.split('/')[-1]
  return fille_name.split('.')[0].split('_')[0], fille_name.split('.')[0].split('_')[1]  

# возвращает id объекта из пути к файлу картинки
# fille_path - путь к файлу
def getImgId(fille_path):    
  return int(setImgId(fille_path)[0])

# возвращает преффикс 1 или 2 объекта из пути к файлу картинки

# fille_path - путь к файлу
def filterImgPreff(fille_path, pref_list = [1, '1']):  
    fille_pref = setImgId(fille_path)[1]
    return fille_pref in pref_list
