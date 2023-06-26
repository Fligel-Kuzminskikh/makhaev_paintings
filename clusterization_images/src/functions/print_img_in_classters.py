
# выводит на печать изображения по всем кластерам
# df - датафрейм с столбцами 'img' (вектор изображения PIL или CV2), 'title' (заголовок), 'labels' (присвоенный класс)
# sampel_size = 30 - максимальный размер выборки изображений,
# cv2_img = False - булеан использовать формат cv2 или нет, 
# name = False -  булеан печатать имя картинки или нет, 
def print_img_in_classters(df, cv2_img = False, sampel_size = 30, suptitle = '', name = False):    
    for k in np.unique(df['labels']):
        df_temp = df[df['labels'] == k]
        suptitle = '-'.join([str(k), str(len(df_temp))])
        print_claster(df, k, suptitle = suptitle, sampel_size = sampel_size, cv2_img = cv2_img , name = name)
