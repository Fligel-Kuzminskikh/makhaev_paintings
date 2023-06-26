
# получение массива deskriptors ключевых точек
# возвращает массив deskriptors

#img_info - словарь вида 
# {'gray':вектор ч/б изображения формата CV2, 'kp':массив ключевых точек}
def get_sift_des(img_info, sift = cv2.SIFT_create()):  
  gray, kp = img_info['gray'], img_info['kp']
  return sift.compute(gray,kp)[1]
