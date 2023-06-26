
# получение ключевых точек
# возвращает словарь вида 
# {'img':вектор изображения формата CV2, 'gray':вектор ч/б изображения формата CV2, 'title':название изображения, 'kp':массив ключевых точек}

#img_info - словарь вида {'img':вектор изображения формата CV2, 'title':название изображения}
def set_sift_dict(img_info):
    name_list = ['img','gray','title','kp']
    img, title = img_info['img'], img_info['title']
    kp, gray = get_sift_kp(img)
    img_dict = dict(zip(name_list,[img, gray, title, kp]))
    
    return img_dict
