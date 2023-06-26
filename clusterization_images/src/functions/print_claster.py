
# выводит на экран изображения принадлежащие к конкретному кластеру

# df - датафрейм с столбцами 'img' (вектор изображения PIL или CV2), 'title' (заголовок), 'labels' (присвоенный класс)
# label - наименование класса,
# sampel_size = 30 - максимальный размер выборки изображений,
# suptitle = '' - заголовок для печати блока изображений,
# cv2_img = False - булеан использовать формат cv2 или нет, 
# name = False -  булеан печатать имя картинки или нет, 
def print_claster(df, label, sampel_size = 30, suptitle = '', cv2_img = False, name = False):
  rezult_df = df[df['labels'] == label].to_dict(orient='records')
  if len(rezult_df) > sampel_size:
     show_img(sample(rezult_df, sampel_size), name = name, suptitle = suptitle, cv2_img = cv2_img)
  else:
     show_img(rezult_df, name = name, suptitle = suptitle, cv2_img = cv2_img)
