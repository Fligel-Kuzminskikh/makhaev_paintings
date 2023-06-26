
# конвертация из BGR в gray

# img - вектор изображенияв формат cv2

def get_gray(img):
   img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
   return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
