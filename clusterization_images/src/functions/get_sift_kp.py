
# получение ключевых точек sift
# возвращает массив ключевых точек и ч/б изображение в формате вектора CV2

#img - вектор изображения формата CV2
def get_sift_kp(img, sift = cv2.SIFT_create()):    
    gray = get_gray(img) 
    kp_all = sift.detect(gray,None)
    kp = get_sorted_kp(kp_all)

    return kp, gray
